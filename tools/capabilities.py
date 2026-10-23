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
        while True:
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    stale = 0
    for readme in sorted(glob.glob(os.path.join(ROOT, "boards", "**", "README.md"), recursive=True)):
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
        new_tab = table(web, fx, warn)
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
