---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Az Olimex ESP32-P4-PC panel az Ethernet aljzattal, az USB portokkal és a HDMI csatlakozóval
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Az Olimex ESP32-P4-PC panel az Ethernet aljzattal, az USB portokkal és a HDMI csatlakozóval](img/board-01.jpg)

Az Olimex ESP32-P4-PC egy kis számítógép az ESP32-P4-en - két mag 400 MHz-en és 32 MB PSRAM - 100 Mb-es Ethernettel, négy USB host porttal, HDMI-vel, hanggal és egy Li-Po akkumulátorral, amely áramszünetben is működésben tartja. A ctrl32-vel vezetékes vezérlő a legnagyobb programmal, amelyet egy ESP32 futtat - 4096 változó -, a kezelőoldala bármely böngészőben (WEBview), Modbus TCP, MQTT TLS-sel, és CAN vagy RS-485 a tüskesora szabad lábain.

**Mire jó:**

- Vezetékes PLC, amely a saját akkumulátorán vészeli át az áramszünetet
- Átjáró összetett logikával a Modbus TCP, a CAN és az MQTT között
- Vezérlés egy dobozban, PoE-ről táplálva (a bővítménnyel)

A panel oldala a katalógusban: [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC - lábkiosztás: minden GPIO funkciója a ctrl32-ben](pinout/pinout.png)

## Mire képes a ctrl32 ezen a panelen

<!-- capabilities:start -->
| Funkció | Ezen a panelen | Megjegyzés |
|---|---|---|
| Chip | ESP32-P4 (ESP32-P4NRW32) |  |
| Memória | 16 MB flash, 32 MB PSRAM |  |
| Programméret | 4096 változó, 512 riasztás, 1024 blokk | a szerkesztő letöltés előtt ellenőrzi |
| Digitális bemenetek / kimenetek | 15 szabad GPIO | lásd a lábkiosztást |
| Analóg bemenetek | I2C ADC-n keresztül (ADS1115) |  |
| Ethernet | igen - IP101GRI |  |
| Wi-Fi | nem |  |
| CAN (TWAI) | 1 - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus RTU (RS-485) | igen - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus TCP | kliens és szerver |  |
| MQTT | igen (TLS is) | Home Assistant discovery |
| WEBview | igen | a kezelőoldal bármely böngészőben |
| Kijelző / érintés (HMI) | nem | a kezelőoldal a WEBview |
| USB | USB-C (Native USB) |  |
| Tápellátás | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Ami nem támogatott

- A HDMI kimenet és a MIPI DSI / CSI csatlakozók - ez a panel a ctrl32-ben kijelző nélkül fut (a kezelőoldal a WEBview).
- Az USB host portok és a hangkimenet.
- A microSD foglalat - a ctrl32 a programot és a képernyőket a panel flash memóriájában tartja.

## Az útmutató

| Lépés | Oldal |
|---|---|
| 1 | [Hardver és bekötés](hardware.hu.md) - amire szükséged van, tápellátás, lábkiosztás |
| 2 | [A runtime telepítése](install.hu.md) - a szerkesztő, a panel, az első feltöltés |
| 3 | [Beállítás](configure.hu.md) - hálózat, I/O, kommunikáció |
| 4 | [Példaprojektek](examples/README.hu.md) - minden, amire a panel képes, megnyitásra készen |
| - | [Hibaelhárítás](troubleshooting.hu.md) |

## Fájlok

| Fájl | Mi |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | a lábkiosztás, vektoros (és [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | honnan származnak a fotók, a kapcsolási rajzok és a modellek |

## Tovább

- [ctrl32 dokumentáció](https://ctrl32.com/docs/) - a szerkesztő, a nyelvek, minden blokk
- [A szerkesztő letöltése](https://ctrl32.com/download/)
- [Minden tesztelt panel](../../README.hu.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.hu.md) - ugyanaz az ESP32-P4 egy kisebb panelen

