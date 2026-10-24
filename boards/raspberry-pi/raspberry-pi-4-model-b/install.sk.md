---
title: Nahratie runtime ctrl32 do dosky Raspberry Pi 4 Model B
slug: install
sidebar_position: 30
image: img/install-03-prepare.png
image_alt: Editor ctrl32 pripravuje dosku Raspberry Pi 4 Model B
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
- install
---

# Nahratie runtime ctrl32

Linux runtime ctrl32 je program v doske, ktorý vykonáva tvoj projekt - cyklus PLC, obrazovku na monitore, WEBview, OPC UA a zbernice. Editor ho nainštaluje cez sieť; nepíše sa žiadny linuxový príkaz.

## 1. Zapíš kartu

Nahraj na kartu **Raspberry Pi OS Lite (64-bit)** pomocou Raspberry Pi
Imager. *Lite* je zámer: runtime kreslí obrazovku sám a desktop
nepotrebuje. V nastaveniach Imagera pred zápisom nastav:

- **hostname**, podľa ktorého Pi v sieti spoznáš,
- **používateľa** a jeho **heslo**,
- **zapnuté SSH**,
- Wi-Fi len vtedy, ak Pi nebude na kábli.

Vlož kartu do Pi, pripoj Ethernet a monitor a zapni ho.

![Raspberry Pi 4 Model B](img/board-01.jpg)

## 2. Vytvor projekt

Spusti editor ctrl32 a vyber **New project** (Ctrl+N). Zadaj **názov** projektu, pod **Linux** vyber **Raspberry Pi** a stlač **Create project**.

![Sprievodca New project s vybraným Raspberry Pi](img/install-02-new-project.png)

Ak chceš začať hotovým príkladom, otvor [projekt all-in-one](examples/all-in-one/README.sk.md) (**File → Open**).

## 3. Priprav dosku

Vyber **Online → Prepare a Linux device**. Zadaj **adresu** dosky, **používateľa** a **heslo** z kroku 1 a stlač **Look at the device**: editor sa prihlási, zistí, čo je doska zač, a vypíše, čo urobí - pozretie nič nemení. Potom stlač **Prepare it**: editor skopíruje runtime, nainštaluje ho ako službu, spustí ho a počká, kým odpovie. Odvtedy doska spúšťa runtime pri každom štarte.

![Prepare a Linux device: čo je doska zač a kroky, ktoré editor urobí](img/install-03-prepare.png)

Nechaj zaškrtnuté **Do not ask for the password again**: editor uloží do dosky vlastný kľúč a pri ďalších návštevách stačí adresa. Heslo sa použije raz a nikde sa neuloží.

Pod plánom je **Operating system of this device** - to, čo patrí k Pi a
nie k projektu: CAN HAT (jeden riadok na každý čip CAN na SPI), uvoľnenie
sériového portu pre RS-485 HAT, I2C, pevná adresa a real-time jadro pre
EtherCAT. Zaškrtni, čo tvoje Pi nesie; každý zaškrtnutý riadok je jeden
krok a Pi sa reštartuje, len keď sa zmenilo nastavenie štartu.

## 4. Nahraj projekt

Zadaj adresu dosky do výberu portu na paneli nástrojov a stlač tlačidlo nahrania (F5). Runtime projekt načíta a na monitore sa objaví obrazovka.

![Panel nástrojov: výber portu a tlačidlo nahrania](img/install-05-download.png)

## 5. Over, že beží

- **ONLINE** (ikona zástrčky) ukáže živé hodnoty v rungoch, premenných aj na obrazovke.
- **WEBview**: `http://<adresa>:8080` v prehliadači v tej istej sieti.
- **OPC UA**: `opc.tcp://<adresa>:4840` - každá premenná je uzol, `ns=1;s=<meno>`.

![Bežiaci ladder program - zelená znamená, že prúd tečie](img/install-06-running.png)

| Port | Čo tam beží |
|---|---|
| 8080 | WEBview, nahratie programu, hľadanie zariadenia |
| 4840 | server OPC UA |
| 3232 | online spojenie editora |

Niečo nejde? Pozri [Riešenie problémov](troubleshooting.sk.md).

*Screenshoty: editor ctrl32 1.07.*

---

[← Hardvér a zapojenie](hardware.sk.md) | [Prehľad](README.sk.md) | [Nastavenie →](configure.sk.md)
