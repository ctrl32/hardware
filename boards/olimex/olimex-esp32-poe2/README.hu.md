---
title: Olimex ESP32-POE2
slug: olimex-esp32-poe2
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe2/
image: img/board-01.jpg
image_alt: Az Olimex ESP32-POE2 panel az Ethernet aljzattal és a tápkimenetekkel
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Olimex ESP32-POE2

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Az Olimex ESP32-POE2 panel az Ethernet aljzattal és a tápkimenetekkel](img/board-01.jpg)

Az Olimex ESP32-POE2 az ESP32-PoE következő generációja: egy ESP32 8 MB PSRAM-mal, Ethernettel és IEEE 802.3at szerinti Power over Ethernettel, amely a terepi eszközeidet is táplálja - 24 V-os vagy 12 V-os, 5 V-os és 3,3 V-os kimenetek, akár 25 W a hálózati kábelből. A ctrl32-vel egy kapcsolószekrényes PLC egyetlen kábelen: létralogika, WEBview, Modbus TCP és MQTT, a PSRAM-os klasszikus ESP32 teljes programméretével.

**Mire jó:**

- Szekrény-PLC, amely PoE-ről táplálja az érzékelőit és egy kis relémodult
- Modbus TCP átjáró MQTT-vel a Home Assistant felé
- Épületautomatizálás, szobánként egy kábellel

A panel oldala a katalógusban: [Olimex ESP32-POE2](https://ctrl32.com/hardware/boards/olimex-esp32-poe2/)

![Olimex ESP32-POE2 - lábkiosztás: minden GPIO funkciója a ctrl32-ben](pinout/pinout.png)

## Mire képes a ctrl32 ezen a panelen

<!-- capabilities:start -->
| Funkció | Ezen a panelen | Megjegyzés |
|---|---|---|
| Chip | ESP32 (ESP32-WROVER-E-N4R8) |  |
| Memória | 4 MB flash, 8 MB PSRAM |  |
| Programméret | 512 változó, 128 riasztás, 1024 blokk | a szerkesztő letöltés előtt ellenőrzi |
| Digitális bemenetek / kimenetek | 5 szabad GPIO | 3 ebből csak bemenet |
| Analóg bemenetek | 3 a chipen (ADC1) | GPIO34, GPIO36, GPIO39 |
| Ethernet | igen - LAN8710A |  |
| Power over Ethernet | IEEE 802.3at |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus RTU (RS-485) | igen - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus TCP | kliens és szerver |  |
| MQTT | igen | Home Assistant discovery |
| WEBview | igen | a kezelőoldal bármely böngészőben |
| Kijelző / érintés (HMI) | nem | a kezelőoldal a WEBview |
| USB | USB-C |  |
| Tápellátás | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Ami nem támogatott

- Bluetooth - az ESP32-ben megvan, a ctrl32 nem használja.
- A microSD foglalat - a ctrl32 a programot és a képernyőket a chip saját flash memóriájában tartja.
- Az akkumulátorbemenet a panel saját funkciójaként működik; a ctrl32 nem olvassa ki az akkumulátor töltöttségét.

## Az útmutató

| Lépés | Oldal |
|---|---|
| 1 | [Hardver és bekötés](hardware.hu.md) - amire szükséged van, tápellátás, lábkiosztás |
| 2 | [A runtime telepítése](install.hu.md) - a szerkesztő, a panel, az első feltöltés |
| 3 | [Beállítás](configure.hu.md) - hálózat, I/O, kommunikáció |
| 4 | [Példaprojektek](examples/README.hu.md) - minden, amire a panel képes, megnyitásra készen |
| - | [Hibaelhárítás](troubleshooting.hu.md) |

## Fájlok

-

## Tovább

- [ctrl32 dokumentáció](https://ctrl32.com/docs/) - a szerkesztő, a nyelvek, minden blokk
- [A szerkesztő letöltése](https://ctrl32.com/download/)
- [Minden tesztelt panel](../../README.hu.md)
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.hu.md) - az első generáció
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.hu.md) - leválasztott PoE táppal

