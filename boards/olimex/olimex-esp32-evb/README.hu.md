---
title: Olimex ESP32-EVB
slug: olimex-esp32-evb
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-evb/
image: img/board-01.jpg
image_alt: Az Olimex ESP32-EVB panel a két reléjével, az Ethernet aljzattal és a CAN sorkapoccsal
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Olimex ESP32-EVB

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 240x320](https://img.shields.io/badge/HMI-240x320-0891b2)

![Az Olimex ESP32-EVB panel a két reléjével, az Ethernet aljzattal és a CAN sorkapoccsal](img/board-01.jpg)

Az Olimex ESP32-EVB vezérlésre épített ESP32 panel: két relé (10 A / 250 VAC), CAN adó-vevő, Ethernet és Wi-Fi egyetlen panelen. A ctrl32-vel kész PLC - a relék és a gomb egy létraprogram változói, a CAN hajtásokkal és I/O csomópontokkal beszél, a kezelőoldal pedig bármely böngészőben fut (WEBview). Egy opcionális 2,8"-os érintőkijelző az UEXT csatlakozón kis kezelőpanellé teszi.

**Mire jó:**

- Relés vezérlés - fűtés, szivattyúk, világítás - Ethernettel
- CAN master egy hajtáshoz vagy CANopen I/O csomópontokhoz
- Termosztát vagy kis kezelőpanel az opcionális 2,8"-os kijelzővel

A panel oldala a katalógusban: [Olimex ESP32-EVB](https://ctrl32.com/hardware/boards/olimex-esp32-evb/)

![Olimex ESP32-EVB - lábkiosztás: minden GPIO funkciója a ctrl32-ben](pinout/pinout.png)

## Mire képes a ctrl32 ezen a panelen

<!-- capabilities:start -->
| Funkció | Ezen a panelen | Megjegyzés |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memória | 4 MB flash |  |
| Programméret | 128 változó, 32 riasztás, 128 blokk | a szerkesztő letöltés előtt ellenőrzi |
| Digitális bemenetek / kimenetek | 6 szabad GPIO | 2 ebből csak bemenet |
| Analóg bemenetek | 4 a chipen (ADC1) | GPIO32, GPIO33, GPIO34, GPIO36 |
| Ethernet | igen - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 |  |
| Modbus RTU (RS-485) | igen - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus TCP | kliens és szerver |  |
| MQTT | igen | Home Assistant discovery |
| WEBview | igen | a kezelőoldal bármely böngészőben |
| Kijelző / érintés (HMI) | - 240x320, - |  |
| USB | Micro-USB (CH340T USB-UART) |  |
| Tápellátás | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ami nem támogatott

- Bluetooth.
- Az IR vevő és adó - a ctrl32 ezen a panelen nem használja őket.
- A microSD foglalat - a ctrl32 a programot és a képernyőket a chip saját flash memóriájában tartja.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.hu.md) - Ethernet és Power over Ethernet

