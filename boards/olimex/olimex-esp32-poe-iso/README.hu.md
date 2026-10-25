---
title: Olimex ESP32-PoE-ISO
slug: olimex-esp32-poe-iso
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe-iso/
image: img/board-01.jpg
image_alt: Az Olimex ESP32-PoE-ISO panel az Ethernet aljzattal és a leválasztott PoE táppal
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Olimex ESP32-PoE-ISO

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Az Olimex ESP32-PoE-ISO panel az Ethernet aljzattal és a leválasztott PoE táppal](img/board-01.jpg)

Az Olimex ESP32-PoE-ISO az ESP32-PoE galvanikusan leválasztott Power over Ethernet táppal: egyetlen hálózati kábel adja a tápját és viszi a kapcsolatát, és egy PC USB-n csatlakoztatva maradhat, miközben a panel PoE-ről fut. A ctrl32-vel kompakt PLC egy kapcsolószekrénybe - létraprogram a chipen, a kezelőoldala bármely böngészőben (WEBview), Modbus TCP a mérők és I/O modulok felé, és MQTT a Home Assistant felé.

**Mire jó:**

- Kis PLC egy kapcsolószekrényben, PoE switchről táplálva
- Modbus TCP átjáró, amely mérőket olvas ki és MQTT-n teszi közzé őket
- Otthonautomatizálás - egy szoba vagy egy kazánház egyetlen kábelen

A panel oldala a katalógusban: [Olimex ESP32-PoE-ISO](https://ctrl32.com/hardware/boards/olimex-esp32-poe-iso/)

![Olimex ESP32-PoE-ISO - lábkiosztás: minden GPIO funkciója a ctrl32-ben](pinout/pinout.png)

## Mire képes a ctrl32 ezen a panelen

<!-- capabilities:start -->
| Funkció | Ezen a panelen | Megjegyzés |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memória | 4 MB flash |  |
| Programméret | 128 változó, 32 riasztás, 128 blokk | a szerkesztő letöltés előtt ellenőrzi |
| Digitális bemenetek / kimenetek | 6 szabad GPIO | 3 ebből csak bemenet |
| Analóg bemenetek | 4 a chipen (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | igen - LAN8710A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus RTU (RS-485) | igen - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus TCP | kliens és szerver |  |
| MQTT | igen | Home Assistant discovery |
| WEBview | igen | a kezelőoldal bármely böngészőben |
| Kijelző / érintés (HMI) | nem | a kezelőoldal a WEBview |
| USB | Micro-USB (CH340T USB-UART) |  |
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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.hu.md) - ugyanez a panel leválasztott táp nélkül
- Olimex ESP32-POE2 - a következő generáció

