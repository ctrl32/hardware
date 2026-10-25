#!/usr/bin/env python3
"""capabilities.py - fills the "What ctrl32 can do on this board" table of
every board guide from the ctrl32.com hardware catalog.

The table is never written by hand: the board's web page (the Parameters tab)
and its guide must say the same. For every boards/**/README.md whose front
matter names a `hardware:` address, the script reads

  - the board's record from the public catalog API of ctrl32.com
    (chip, module, flash, PSRAM, wireless, power, USB, display, touch), and
  - board.yaml beside the README - the ctrl32 facts of the board (Ethernet PHY,
    CAN, RS-485, the program limits, the free and analog GPIO)

and rewrites only the text between <!-- capabilities:start --> and
<!-- capabilities:end -->.

Rule: every ESP32 has exactly ONE CAN controller (TWAI) - the S3, the C6 and
the P4 too; the ESP32-C2 and the ESP8266 have none. The script enforces it
whatever the catalog says and warns when the catalog disagrees.

Usage:
    python tools/capabilities.py            # rewrite the tables
    python tools/capabilities.py --check    # exit 1 when a table is not current (CI)

A missing catalog value becomes "-" and a warning; it is fixed in the catalog,
never in the guide.
"""
import argparse, glob, json, os, re, sys, urllib.request

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://ctrl32.com/api/v1"
START, END = "<!-- capabilities:start -->", "<!-- capabilities:end -->"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ctrl32-hardware-capabilities"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


_catalog = None


def catalog():
    """canonical address -> {parameter name: [values]} of every board."""
    global _catalog
    if _catalog is None:
        _catalog, page = {}, 1
        # CTRL32_CATALOG_DUMP = a JSON list of board records saved from the
        # API, for a run while ctrl32.com does not answer
        dump = os.environ.get("CTRL32_CATALOG_DUMP")
        while True:
            if dump:
                with open(dump, encoding="utf-8") as f:
                    j = {"results": json.load(f), "pages": 1}
            else:
                j = get(f"{API}/records?bundle=board&page_size=50&page={page}")
            for r in j["results"]:
                vals = {}
                for x in r.get("teaser_rows", []):
                    items = []
                    for it in x.get("items") or []:
                        if isinstance(it, str):
                            items.append(it)
                        elif isinstance(it, dict) and "text" in it:
                            items.append(it["text"])
                    if items:
                        vals[x["name"]] = items
                _catalog[r["canonical_url"]] = vals
            if page >= j["pages"]:
                break
            page += 1
    return _catalog


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def can_rule(chip, controllers):
    c = chip.lower()
    if c.startswith("esp8266") or c.startswith("esp32-c2"):
        want = 0
    elif c.startswith("esp32"):
        want = 1
    else:
        return controllers
    if controllers not in (None, want):
        print(f"  warning: the catalog says {controllers} CAN for {chip} - it is {want}", file=sys.stderr)
    return want


def table(web, fx, warn):
    def w(name, joiner=", "):
        v = web.get(name)
        if not v:
            warn.append(name)
            return "-"
        return joiner.join(v)

    lim = fx.get("limits") or {}
    rows = [("Chip", w("hw_platform_ref") + (f" ({fx['module']})" if fx.get("module") else ""), "")]
    if not fx.get("linux"):
        mem = w("hw_flash_ref") + " flash"
        if web.get("hw_psram_ref"):
            mem += ", " + ", ".join(web["hw_psram_ref"]) + " PSRAM"
        rows.append(("Memory", mem, ""))
    rows.append(("Program size", f"{lim.get('variables', '-')} variables, {lim.get('alarms', '-')} alarms, "
                                 f"{lim.get('blocks', '-')} blocks", "checked by the editor before a download"))
    free, adc = fx.get("free_gpio") or [], fx.get("analog_gpio") or []
    if fx.get("linux"):
        rows.append(("Digital inputs / outputs", "through I/O modules", "Modbus, CANopen, EtherCAT"))
    else:
        ins = fx.get("input_only_gpio") or []
        note = f"{len(ins)} of them inputs only" if ins else "see the pin map"
        rows.append(("Digital inputs / outputs", f"{len(free)} free GPIO", note))
        rows.append(("Analog inputs", f"{len(adc)} on the chip (ADC1)" if adc else "through an I2C ADC (ADS1115)",
                     ", ".join(f"GPIO{g}" for g in adc) if adc else ""))
    eth = fx.get("ethernet")
    rows.append(("Ethernet", "yes" + (f" - {eth}" if eth and eth != "yes" else "") if eth else "no", ""))
    power = web.get("hw_power_source_ref") or []
    poe = [p for p in power if "PoE" in p]
    if poe:
        rows.append(("Power over Ethernet", poe[0].replace("PoE", "").strip(" ()") or "yes", ""))
    rows.append(("Wi-Fi", next((x for x in web.get("hw_wireless_ref", []) if "Wi-Fi" in x), "no"), ""))
    can = fx.get("can") or {}
    n = can_rule(w("hw_platform_ref"), can.get("controllers"))
    if fx.get("linux"):
        rows.append(("CAN", "through a CAN HAT or a USB adapter", "SocketCAN, up to 4 buses"))
    elif can.get("routed"):
        rows.append(("CAN (TWAI)", str(n), "" if (fx.get("can") or {}).get("transceiver") else "needs an external transceiver"))
    elif fx.get("wired_buses"):
        rows.append(("CAN (TWAI)", f"{n} - on free pins", "needs an external transceiver"))
    else:
        rows.append(("CAN (TWAI)", f"{n} on the chip - not brought out on this board", ""))
    rs = fx.get("rs485")
    if fx.get("linux"):
        rows.append(("Modbus RTU (RS-485)", "yes", "a USB dongle or a HAT"))
    elif rs:
        rows.append(("Modbus RTU (RS-485)", "yes",
                     "" if fx.get("rs485_transceiver") else "on free pins, needs an external transceiver"))
    elif fx.get("wired_buses"):
        rows.append(("Modbus RTU (RS-485)", "yes - on free pins", "needs an external transceiver"))
    else:
        rows.append(("Modbus RTU (RS-485)", "no transceiver on the board", ""))
    rows.append(("Modbus TCP", "client and server", ""))
    rows.append(("MQTT", "yes" + (" (TLS too)" if fx.get("linux") or "ESP32-S3" in w("hw_platform_ref") or
                                  "ESP32-P4" in w("hw_platform_ref") else ""), "Home Assistant discovery"))
    rows.append(("WEBview", "yes", "the operator page in any browser"))
    if fx.get("linux"):
        rows.append(("OPC UA server", "yes", ""))
        rows.append(("EtherCAT master", "yes", "on a second Ethernet port"))
    disp = fx.get("display")
    if disp:
        rows.append(("Display / touch (HMI)", f"{w('hw_display_size_ref')} {disp[0]}x{disp[1]}, "
                                              f"{(fx.get('touch') or w('hw_touch_ref'))}", ""))
    elif fx.get("linux"):
        rows.append(("Display (HMI)", "HDMI or a DSI panel", "or headless with WEBview"))
    else:
        rows.append(("Display / touch (HMI)", "no", "the operator page is WEBview"))
    rows.append(("USB", w("hw_usb_connector_ref") + (f" ({w('hw_usb_uart_ref')})" if web.get("hw_usb_uart_ref") else ""), ""))
    rows.append(("Power", w("hw_supply_voltage_ref"), ""))
    out = ["| Feature | On this board | Notes |", "|---|---|---|"]
    out += [f"| {a} | {b} | {c} |" for a, b, c in rows]
    return "\n".join(out)


# The translated tables (README.<lang>.md): the same rows, the fixed words of
# the table in the language - the catalog's own values (USB-C, Wi-Fi 2.4 GHz,
# the chip names) stay as the catalog writes them. Longer phrases first.
WORDS = {
    "sk": [
        ("| Feature | On this board | Notes |", "| Vlastnosť | Na tejto doske | Poznámka |"),
        ("checked by the editor before a download", "editor ho overí pred nahratím"),
        ("Digital inputs / outputs", "Digitálne vstupy / výstupy"),
        ("through I/O modules", "cez I/O moduly"),
        ("free GPIO", "voľných GPIO"), ("of them inputs only", "z nich len vstupy"),
        ("see the pin map", "pozri mapu pinov"),
        ("Analog inputs", "Analógové vstupy"), ("on the chip (ADC1)", "na čipe (ADC1)"),
        ("through an I2C ADC (ADS1115)", "cez I2C prevodník (ADS1115)"),
        ("Program size", "Veľkosť programu"), (" variables,", " premenných,"), (" alarms,", " alarmov,"),
        (" blocks |", " blokov |"),
        ("Power over Ethernet", "Napájanie cez Ethernet"),
        ("through a CAN HAT or a USB adapter", "cez CAN HAT alebo USB adaptér"),
        ("SocketCAN, up to 4 buses", "SocketCAN, až 4 zbernice"),
        ("on the chip - not brought out on this board", "na čipe - doska ho nevyvádza"),
        ("needs an external transceiver", "treba externý prevodník"),
        ("on free pins", "na voľných pinoch"),
        ("no transceiver on the board", "doska nemá prevodník"),
        ("a USB dongle or a HAT", "USB prevodník alebo HAT"),
        ("client and server", "klient aj server"),
        ("Home Assistant discovery", "objavenie v Home Assistant"),
        ("the operator page in any browser", "stránka operátora v každom prehliadači"),
        ("OPC UA server", "Server OPC UA"), ("on a second Ethernet port", "na druhom porte Ethernet"),
        ("Display / touch (HMI)", "Displej / dotyk (HMI)"), ("Display (HMI)", "Displej (HMI)"),
        ("HDMI or a DSI panel", "HDMI alebo panel DSI"), ("or headless with WEBview", "alebo bez displeja s WEBview"),
        ("the operator page is WEBview", "stránka operátora je WEBview"),
        ("(TLS too)", "(aj TLS)"),
        ("| Chip |", "| Čip |"), ("| Memory |", "| Pamäť |"), ("| Power |", "| Napájanie |"),
        ("| yes", "| áno"), ("yes - ", "áno - "), ("| no |", "| nie |"),
    ],
    "cs": [
        ("| Feature | On this board | Notes |", "| Vlastnost | Na této desce | Poznámka |"),
        ("checked by the editor before a download", "editor ji ověří před nahráním"),
        ("Digital inputs / outputs", "Digitální vstupy / výstupy"),
        ("through I/O modules", "přes I/O moduly"),
        ("free GPIO", "volných GPIO"), ("of them inputs only", "z nich jen vstupy"),
        ("see the pin map", "viz mapa pinů"),
        ("Analog inputs", "Analogové vstupy"), ("on the chip (ADC1)", "na čipu (ADC1)"),
        ("through an I2C ADC (ADS1115)", "přes I2C převodník (ADS1115)"),
        ("Program size", "Velikost programu"), (" variables,", " proměnných,"), (" alarms,", " alarmů,"),
        (" blocks |", " bloků |"),
        ("Power over Ethernet", "Napájení přes Ethernet"),
        ("through a CAN HAT or a USB adapter", "přes CAN HAT nebo USB adaptér"),
        ("SocketCAN, up to 4 buses", "SocketCAN, až 4 sběrnice"),
        ("on the chip - not brought out on this board", "na čipu - deska ho nevyvádí"),
        ("needs an external transceiver", "potřebuje externí převodník"),
        ("on free pins", "na volných pinech"),
        ("no transceiver on the board", "deska nemá převodník"),
        ("a USB dongle or a HAT", "USB převodník nebo HAT"),
        ("client and server", "klient i server"),
        ("Home Assistant discovery", "objevení v Home Assistant"),
        ("the operator page in any browser", "stránka operátora v každém prohlížeči"),
        ("OPC UA server", "Server OPC UA"), ("on a second Ethernet port", "na druhém portu Ethernet"),
        ("Display / touch (HMI)", "Displej / dotyk (HMI)"), ("Display (HMI)", "Displej (HMI)"),
        ("HDMI or a DSI panel", "HDMI nebo panel DSI"), ("or headless with WEBview", "nebo bez displeje s WEBview"),
        ("the operator page is WEBview", "stránka operátora je WEBview"),
        ("(TLS too)", "(i TLS)"),
        ("| Chip |", "| Čip |"), ("| Memory |", "| Paměť |"), ("| Power |", "| Napájení |"),
        ("| yes", "| ano"), ("yes - ", "ano - "), ("| no |", "| ne |"),
    ],
    "de": [
        ("| Feature | On this board | Notes |", "| Merkmal | Auf diesem Board | Hinweise |"),
        ("checked by the editor before a download", "der Editor prüft es vor dem Download"),
        ("Digital inputs / outputs", "Digitale Ein-/Ausgänge"),
        ("through I/O modules", "über E/A-Module"),
        ("free GPIO", "freie GPIO"), ("of them inputs only", "davon nur Eingänge"),
        ("see the pin map", "siehe Pin-Belegung"),
        ("Analog inputs", "Analogeingänge"), ("on the chip (ADC1)", "auf dem Chip (ADC1)"),
        ("through an I2C ADC (ADS1115)", "über einen I2C-ADC (ADS1115)"),
        ("Program size", "Programmgröße"), (" variables,", " Variablen,"), (" alarms,", " Alarme,"),
        (" blocks |", " Bausteine |"),
        ("Power over Ethernet", "Power over Ethernet"),
        ("through a CAN HAT or a USB adapter", "über ein CAN-HAT oder einen USB-Adapter"),
        ("SocketCAN, up to 4 buses", "SocketCAN, bis zu 4 Busse"),
        ("on the chip - not brought out on this board", "auf dem Chip - auf diesem Board nicht herausgeführt"),
        ("needs an external transceiver", "braucht einen externen Transceiver"),
        ("on free pins", "an freien Pins"),
        ("no transceiver on the board", "kein Transceiver auf dem Board"),
        ("a USB dongle or a HAT", "ein USB-Adapter oder ein HAT"),
        ("client and server", "Client und Server"),
        ("Home Assistant discovery", "Home-Assistant-Discovery"),
        ("the operator page in any browser", "die Bedienseite in jedem Browser"),
        ("OPC UA server", "OPC-UA-Server"), ("on a second Ethernet port", "an einem zweiten Ethernet-Port"),
        ("Display / touch (HMI)", "Display / Touch (HMI)"), ("Display (HMI)", "Display (HMI)"),
        ("HDMI or a DSI panel", "HDMI oder ein DSI-Panel"), ("or headless with WEBview", "oder ohne Display mit WEBview"),
        ("the operator page is WEBview", "die Bedienseite ist WEBview"),
        ("(TLS too)", "(auch TLS)"),
        ("| Chip |", "| Chip |"), ("| Memory |", "| Speicher |"), ("| Power |", "| Versorgung |"),
        ("| yes", "| ja"), ("yes - ", "ja - "), ("| no |", "| nein |"),
    ],
    "pl": [
        ('| Feature | On this board | Notes |', '| Funkcja | Na tej płytce | Uwagi |'),
        ('checked by the editor before a download', 'edytor sprawdza to przed wgraniem'),
        ('Digital inputs / outputs', 'Wejścia / wyjścia cyfrowe'),
        ('through I/O modules', 'przez moduły I/O'),
        ('free GPIO', 'wolnych GPIO'),
        ('of them inputs only', 'z nich tylko wejścia'),
        ('see the pin map', 'zobacz mapę pinów'),
        ('Analog inputs', 'Wejścia analogowe'),
        ('on the chip (ADC1)', 'w układzie (ADC1)'),
        ('through an I2C ADC (ADS1115)', 'przez przetwornik I2C (ADS1115)'),
        ('Program size', 'Rozmiar programu'),
        (' variables,', ' zmiennych,'),
        (' alarms,', ' alarmów,'),
        (' blocks |', ' bloków |'),
        ('Power over Ethernet', 'Zasilanie przez Ethernet (PoE)'),
        ('through a CAN HAT or a USB adapter', 'przez CAN HAT lub adapter USB'),
        ('SocketCAN, up to 4 buses', 'SocketCAN, do 4 magistral'),
        ('on the chip - not brought out on this board', 'w układzie - ta płytka go nie wyprowadza'),
        ('needs an external transceiver', 'wymaga zewnętrznego transceivera'),
        ('on free pins', 'na wolnych pinach'),
        ('no transceiver on the board', 'brak transceivera na płytce'),
        ('a USB dongle or a HAT', 'adapter USB lub HAT'),
        ('client and server', 'klient i serwer'),
        ('Home Assistant discovery', 'wykrywanie w Home Assistant'),
        ('the operator page in any browser', 'strona operatora w każdej przeglądarce'),
        ('OPC UA server', 'Serwer OPC UA'),
        ('on a second Ethernet port', 'na drugim porcie Ethernet'),
        ('Display / touch (HMI)', 'Wyświetlacz / dotyk (HMI)'),
        ('Display (HMI)', 'Wyświetlacz (HMI)'),
        ('HDMI or a DSI panel', 'HDMI lub panel DSI'),
        ('or headless with WEBview', 'lub bez wyświetlacza z WEBview'),
        ('the operator page is WEBview', 'strona operatora to WEBview'),
        ('(TLS too)', '(także TLS)'),
        ('| Chip |', '| Układ |'),
        ('| Memory |', '| Pamięć |'),
        ('| Power |', '| Zasilanie |'),
        ('| yes', '| tak'),
        ('yes - ', 'tak - '),
        ('| no |', '| nie |'),
    ],
    "it": [
        ('| Feature | On this board | Notes |', '| Funzione | Su questa scheda | Note |'),
        ('checked by the editor before a download', "l'editor lo verifica prima del download"),
        ('Digital inputs / outputs', 'Ingressi / uscite digitali'),
        ('through I/O modules', 'tramite moduli I/O'),
        ('free GPIO', 'GPIO liberi'),
        ('of them inputs only', 'di cui solo ingressi'),
        ('see the pin map', 'vedi la mappa dei pin'),
        ('Analog inputs', 'Ingressi analogici'),
        ('on the chip (ADC1)', 'sul chip (ADC1)'),
        ('through an I2C ADC (ADS1115)', 'tramite un ADC I2C (ADS1115)'),
        ('Program size', 'Dimensione del programma'),
        (' variables,', ' variabili,'),
        (' alarms,', ' allarmi,'),
        (' blocks |', ' blocchi |'),
        ('Power over Ethernet', 'Power over Ethernet'),
        ('through a CAN HAT or a USB adapter', 'tramite un CAN HAT o un adattatore USB'),
        ('SocketCAN, up to 4 buses', 'SocketCAN, fino a 4 bus'),
        ('on the chip - not brought out on this board', 'sul chip - non portato fuori su questa scheda'),
        ('needs an external transceiver', 'serve un transceiver esterno'),
        ('on free pins', 'su pin liberi'),
        ('no transceiver on the board', 'nessun transceiver sulla scheda'),
        ('a USB dongle or a HAT', 'un adattatore USB o un HAT'),
        ('client and server', 'client e server'),
        ('Home Assistant discovery', 'rilevamento in Home Assistant'),
        ('the operator page in any browser', 'la pagina operatore in qualsiasi browser'),
        ('OPC UA server', 'Server OPC UA'),
        ('on a second Ethernet port', 'su una seconda porta Ethernet'),
        ('Display / touch (HMI)', 'Display / touch (HMI)'),
        ('Display (HMI)', 'Display (HMI)'),
        ('HDMI or a DSI panel', 'HDMI o un pannello DSI'),
        ('or headless with WEBview', 'oppure senza display con WEBview'),
        ('the operator page is WEBview', 'la pagina operatore è WEBview'),
        ('(TLS too)', '(anche TLS)'),
        ('| Chip |', '| Chip |'),
        ('| Memory |', '| Memoria |'),
        ('| Power |', '| Alimentazione |'),
        ('| yes', '| sì'),
        ('yes - ', 'sì - '),
        ('| no |', '| no |'),
    ],
    "es": [
        ('| Feature | On this board | Notes |', '| Característica | En esta placa | Notas |'),
        ('checked by the editor before a download', 'el editor lo comprueba antes de una descarga'),
        ('Digital inputs / outputs', 'Entradas / salidas digitales'),
        ('through I/O modules', 'mediante módulos de E/S'),
        ('free GPIO', 'GPIO libres'),
        ('of them inputs only', 'de ellos solo entradas'),
        ('see the pin map', 'consulta el mapa de pines'),
        ('Analog inputs', 'Entradas analógicas'),
        ('on the chip (ADC1)', 'en el chip (ADC1)'),
        ('through an I2C ADC (ADS1115)', 'mediante un ADC I2C (ADS1115)'),
        ('Program size', 'Tamaño del programa'),
        (' variables,', ' variables,'),
        (' alarms,', ' alarmas,'),
        (' blocks |', ' bloques |'),
        ('Power over Ethernet', 'Power over Ethernet'),
        ('through a CAN HAT or a USB adapter', 'mediante un HAT CAN o un adaptador USB'),
        ('SocketCAN, up to 4 buses', 'SocketCAN, hasta 4 buses'),
        ('on the chip - not brought out on this board', 'en el chip - esta placa no lo saca'),
        ('needs an external transceiver', 'necesita un transceptor externo'),
        ('on free pins', 'en pines libres'),
        ('no transceiver on the board', 'la placa no tiene transceptor'),
        ('a USB dongle or a HAT', 'un adaptador USB o un HAT'),
        ('client and server', 'cliente y servidor'),
        ('Home Assistant discovery', 'descubrimiento en Home Assistant'),
        ('the operator page in any browser', 'la página del operador en cualquier navegador'),
        ('OPC UA server', 'Servidor OPC UA'),
        ('on a second Ethernet port', 'en un segundo puerto Ethernet'),
        ('Display / touch (HMI)', 'Pantalla / táctil (HMI)'),
        ('Display (HMI)', 'Pantalla (HMI)'),
        ('HDMI or a DSI panel', 'HDMI o un panel DSI'),
        ('or headless with WEBview', 'o sin pantalla con WEBview'),
        ('the operator page is WEBview', 'la página del operador es WEBview'),
        ('(TLS too)', '(también TLS)'),
        ('| Chip |', '| Chip |'),
        ('| Memory |', '| Memoria |'),
        ('| Power |', '| Alimentación |'),
        ('| yes', '| sí'),
        ('yes - ', 'sí - '),
        ('| no |', '| no |'),
    ],
    "fr": [
        ('| Feature | On this board | Notes |', '| Fonction | Sur cette carte | Remarques |'),
        ('checked by the editor before a download', "vérifié par l'éditeur avant un téléchargement"),
        ('Digital inputs / outputs', 'Entrées / sorties numériques'),
        ('through I/O modules', "via des modules d'E/S"),
        ('free GPIO', 'GPIO libres'),
        ('of them inputs only', 'dont entrées seules'),
        ('see the pin map', 'voir le brochage'),
        ('Analog inputs', 'Entrées analogiques'),
        ('on the chip (ADC1)', 'sur la puce (ADC1)'),
        ('through an I2C ADC (ADS1115)', 'via un convertisseur A/N I2C (ADS1115)'),
        ('Program size', 'Taille du programme'),
        (' variables,', ' variables,'),
        (' alarms,', ' alarmes,'),
        (' blocks |', ' blocs |'),
        ('Power over Ethernet', 'Power over Ethernet'),
        ('through a CAN HAT or a USB adapter', 'via un HAT CAN ou un adaptateur USB'),
        ('SocketCAN, up to 4 buses', "SocketCAN, jusqu'à 4 bus"),
        ('on the chip - not brought out on this board', 'sur la puce - non sorti sur cette carte'),
        ('needs an external transceiver', 'nécessite un transceiver externe'),
        ('on free pins', 'sur des broches libres'),
        ('no transceiver on the board', 'pas de transceiver sur la carte'),
        ('a USB dongle or a HAT', 'un adaptateur USB ou un HAT'),
        ('client and server', 'client et serveur'),
        ('Home Assistant discovery', 'découverte Home Assistant'),
        ('the operator page in any browser', 'la page opérateur dans tout navigateur'),
        ('OPC UA server', 'Serveur OPC UA'),
        ('on a second Ethernet port', 'sur un second port Ethernet'),
        ('Display / touch (HMI)', 'Écran / tactile (HMI)'),
        ('Display (HMI)', 'Écran (HMI)'),
        ('HDMI or a DSI panel', 'HDMI ou un écran DSI'),
        ('or headless with WEBview', 'ou sans écran avec WEBview'),
        ('the operator page is WEBview', 'la page opérateur est WEBview'),
        ('(TLS too)', '(TLS aussi)'),
        ('| Chip |', '| Puce |'),
        ('| Memory |', '| Mémoire |'),
        ('| Power |', '| Alimentation |'),
        ('| yes', '| oui'),
        ('yes - ', 'oui - '),
        ('| no |', '| non |'),
    ],
    "hu": [
        ('| Feature | On this board | Notes |', '| Funkció | Ezen a panelen | Megjegyzés |'),
        ('checked by the editor before a download', 'a szerkesztő letöltés előtt ellenőrzi'),
        ('Digital inputs / outputs', 'Digitális bemenetek / kimenetek'),
        ('through I/O modules', 'I/O modulokon keresztül'),
        ('free GPIO', 'szabad GPIO'),
        ('of them inputs only', 'ebből csak bemenet'),
        ('see the pin map', 'lásd a lábkiosztást'),
        ('Analog inputs', 'Analóg bemenetek'),
        ('on the chip (ADC1)', 'a chipen (ADC1)'),
        ('through an I2C ADC (ADS1115)', 'I2C ADC-n keresztül (ADS1115)'),
        ('Program size', 'Programméret'),
        (' variables,', ' változó,'),
        (' alarms,', ' riasztás,'),
        (' blocks |', ' blokk |'),
        ('Power over Ethernet', 'Power over Ethernet'),
        ('through a CAN HAT or a USB adapter', 'CAN HAT-on vagy USB adapteren keresztül'),
        ('SocketCAN, up to 4 buses', 'SocketCAN, akár 4 busz'),
        ('on the chip - not brought out on this board', 'a chipen - ez a panel nem vezeti ki'),
        ('needs an external transceiver', 'külső adó-vevő kell hozzá'),
        ('on free pins', 'szabad lábakon'),
        ('no transceiver on the board', 'a panelen nincs adó-vevő'),
        ('a USB dongle or a HAT', 'USB adapter vagy HAT'),
        ('client and server', 'kliens és szerver'),
        ('Home Assistant discovery', 'Home Assistant discovery'),
        ('the operator page in any browser', 'a kezelőoldal bármely böngészőben'),
        ('OPC UA server', 'OPC UA szerver'),
        ('on a second Ethernet port', 'egy második Ethernet porton'),
        ('Display / touch (HMI)', 'Kijelző / érintés (HMI)'),
        ('Display (HMI)', 'Kijelző (HMI)'),
        ('HDMI or a DSI panel', 'HDMI vagy DSI kijelző'),
        ('or headless with WEBview', 'vagy kijelző nélkül, WEBview-val'),
        ('the operator page is WEBview', 'a kezelőoldal a WEBview'),
        ('(TLS too)', '(TLS is)'),
        ('| Chip |', '| Chip |'),
        ('| Memory |', '| Memória |'),
        ('| Power |', '| Tápellátás |'),
        ('| yes', '| igen'),
        ('yes - ', 'igen - '),
        ('| no |', '| nem |'),
    ],
    "ro": [
        ('| Feature | On this board | Notes |', '| Funcție | Pe această placă | Note |'),
        ('checked by the editor before a download', 'verificat de editor înainte de descărcare'),
        ('Digital inputs / outputs', 'Intrări / ieșiri digitale'),
        ('through I/O modules', 'prin module I/O'),
        ('free GPIO', 'GPIO libere'),
        ('of them inputs only', 'dintre ele doar intrări'),
        ('see the pin map', 'vezi harta pinilor'),
        ('Analog inputs', 'Intrări analogice'),
        ('on the chip (ADC1)', 'pe cip (ADC1)'),
        ('through an I2C ADC (ADS1115)', 'printr-un ADC I2C (ADS1115)'),
        ('Program size', 'Mărimea programului'),
        (' variables,', ' variabile,'),
        (' alarms,', ' alarme,'),
        (' blocks |', ' blocuri |'),
        ('Power over Ethernet', 'Power over Ethernet'),
        ('through a CAN HAT or a USB adapter', 'printr-un HAT CAN sau un adaptor USB'),
        ('SocketCAN, up to 4 buses', 'SocketCAN, până la 4 magistrale'),
        ('on the chip - not brought out on this board', 'pe cip - placa nu îl scoate'),
        ('needs an external transceiver', 'necesită un transceiver extern'),
        ('on free pins', 'pe pini liberi'),
        ('no transceiver on the board', 'placa nu are transceiver'),
        ('a USB dongle or a HAT', 'un adaptor USB sau un HAT'),
        ('client and server', 'client și server'),
        ('Home Assistant discovery', 'descoperire în Home Assistant'),
        ('the operator page in any browser', 'pagina operatorului în orice browser'),
        ('OPC UA server', 'Server OPC UA'),
        ('on a second Ethernet port', 'pe un al doilea port Ethernet'),
        ('Display / touch (HMI)', 'Afișaj / touch (HMI)'),
        ('Display (HMI)', 'Afișaj (HMI)'),
        ('HDMI or a DSI panel', 'HDMI sau un afișaj DSI'),
        ('or headless with WEBview', 'sau fără afișaj, cu WEBview'),
        ('the operator page is WEBview', 'pagina operatorului este WEBview'),
        ('(TLS too)', '(și TLS)'),
        ('| Chip |', '| Cip |'),
        ('| Memory |', '| Memorie |'),
        ('| Power |', '| Alimentare |'),
        ('| yes', '| da'),
        ('yes - ', 'da - '),
        ('| no |', '| nu |'),
    ],
    "tr": [
        ('| Feature | On this board | Notes |', '| Özellik | Bu kartta | Notlar |'),
        ('checked by the editor before a download', 'editör yüklemeden önce kontrol eder'),
        ('Digital inputs / outputs', 'Dijital girişler / çıkışlar'),
        ('through I/O modules', 'G/Ç modülleri üzerinden'),
        ('free GPIO', 'boş GPIO'),
        ('of them inputs only', 'tanesi yalnızca giriş'),
        ('see the pin map', 'pin haritasına bakın'),
        ('Analog inputs', 'Analog girişler'),
        ('on the chip (ADC1)', 'çip üzerinde (ADC1)'),
        ('through an I2C ADC (ADS1115)', 'bir I2C ADC üzerinden (ADS1115)'),
        ('Program size', 'Program boyutu'),
        (' variables,', ' değişken,'),
        (' alarms,', ' alarm,'),
        (' blocks |', ' blok |'),
        ('Power over Ethernet', 'Power over Ethernet'),
        ('through a CAN HAT or a USB adapter', 'bir CAN HAT veya USB adaptörü üzerinden'),
        ('SocketCAN, up to 4 buses', 'SocketCAN, 4 veri yoluna kadar'),
        ('on the chip - not brought out on this board', 'çip üzerinde - bu kartta dışarı çıkarılmamış'),
        ('needs an external transceiver', 'harici bir alıcı-verici gerektirir'),
        ('on free pins', 'boş pinlerde'),
        ('no transceiver on the board', 'kartta alıcı-verici yok'),
        ('a USB dongle or a HAT', 'bir USB adaptörü veya bir HAT'),
        ('client and server', 'istemci ve sunucu'),
        ('Home Assistant discovery', 'Home Assistant keşfi (discovery)'),
        ('the operator page in any browser', 'her tarayıcıda operatör sayfası'),
        ('OPC UA server', 'OPC UA sunucusu'),
        ('on a second Ethernet port', 'ikinci bir Ethernet portunda'),
        ('Display / touch (HMI)', 'Ekran / dokunmatik (HMI)'),
        ('Display (HMI)', 'Ekran (HMI)'),
        ('HDMI or a DSI panel', 'HDMI veya bir DSI panel'),
        ('or headless with WEBview', 'ya da WEBview ile ekransız'),
        ('the operator page is WEBview', "operatör sayfası WEBview'dur"),
        ('(TLS too)', '(TLS de)'),
        ('| Chip |', '| Çip |'),
        ('| Memory |', '| Bellek |'),
        ('| Power |', '| Besleme |'),
        ('| yes', '| evet'),
        ('yes - ', 'evet - '),
        ('| no |', '| hayır |'),
    ],
    "uk": [
        ('| Feature | On this board | Notes |', '| Функція | На цій платі | Примітки |'),
        ('checked by the editor before a download', 'редактор перевіряє перед завантаженням'),
        ('Digital inputs / outputs', 'Цифрові входи / виходи'),
        ('through I/O modules', 'через модулі вводу/виводу'),
        ('free GPIO', 'вільних GPIO'),
        ('of them inputs only', 'з них лише входи'),
        ('see the pin map', 'див. карту пінів'),
        ('Analog inputs', 'Аналогові входи'),
        ('on the chip (ADC1)', 'на чипі (ADC1)'),
        ('through an I2C ADC (ADS1115)', 'через I2C АЦП (ADS1115)'),
        ('Program size', 'Розмір програми'),
        (' variables,', ' змінних,'),
        (' alarms,', ' аварійних сигналів,'),
        (' blocks |', ' блоків |'),
        ('Power over Ethernet', 'Power over Ethernet'),
        ('through a CAN HAT or a USB adapter', 'через CAN HAT або USB-адаптер'),
        ('SocketCAN, up to 4 buses', 'SocketCAN, до 4 шин'),
        ('on the chip - not brought out on this board', 'на чипі - на цій платі не виведено'),
        ('needs an external transceiver', 'потрібен зовнішній трансивер'),
        ('on free pins', 'на вільних пінах'),
        ('no transceiver on the board', 'на платі немає трансивера'),
        ('a USB dongle or a HAT', 'USB-адаптер або HAT'),
        ('client and server', 'клієнт і сервер'),
        ('Home Assistant discovery', 'виявлення в Home Assistant'),
        ('the operator page in any browser', 'сторінка оператора в будь-якому браузері'),
        ('OPC UA server', 'Сервер OPC UA'),
        ('on a second Ethernet port', 'на другому порту Ethernet'),
        ('Display / touch (HMI)', 'Дисплей / сенсор (HMI)'),
        ('Display (HMI)', 'Дисплей (HMI)'),
        ('HDMI or a DSI panel', 'HDMI або панель DSI'),
        ('or headless with WEBview', 'або без дисплея з WEBview'),
        ('the operator page is WEBview', 'сторінка оператора - WEBview'),
        ('(TLS too)', '(також TLS)'),
        ('| Chip |', '| Чип |'),
        ('| Memory |', "| Пам'ять |"),
        ('| Power |', '| Живлення |'),
        ('| yes', '| так'),
        ('yes - ', 'так - '),
        ('| no |', '| ні |'),
    ],
}


def localize(tab, lang):
    for en, tr in WORDS.get(lang, []):
        tab = tab.replace(en, tr)
    return tab


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    stale = 0
    readmes = glob.glob(os.path.join(ROOT, "boards", "**", "README.md"), recursive=True)
    readmes += glob.glob(os.path.join(ROOT, "boards", "**", "README.*.md"), recursive=True)
    for readme in sorted(readmes):
        m = re.match(r"README\.([a-z]{2})\.md$", os.path.basename(readme))
        lang = m.group(1) if m else "en"
        text = open(readme, encoding="utf-8").read()
        fmd = front_matter(text)
        addr = fmd.get("hardware")
        if not addr or START not in text or "/examples/" in readme.replace("\\", "/"):
            continue
        fxp = os.path.join(os.path.dirname(readme), "board.yaml")
        fx = yaml.safe_load(open(fxp, encoding="utf-8")) if os.path.exists(fxp) else {}
        web = catalog().get(addr)
        if web is None:
            print(f"{readme}: {addr} is not in the catalog", file=sys.stderr)
            stale += 1
            continue
        warn = []
        new_tab = localize(table(web, fx, warn), lang)
        for x in warn:
            print(f"  warning: {os.path.relpath(readme, ROOT)}: the catalog has no {x}", file=sys.stderr)
        new = re.sub(re.escape(START) + r".*?" + re.escape(END), START + "\n" + new_tab + "\n" + END, text, flags=re.S)
        if new != text:
            stale += 1
            if a.check:
                print(f"{os.path.relpath(readme, ROOT)}: the capability table is not current")
            else:
                with open(readme, "w", encoding="utf-8", newline="\n") as f:
                    f.write(new)
                print(f"updated {os.path.relpath(readme, ROOT)}")
    if a.check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
