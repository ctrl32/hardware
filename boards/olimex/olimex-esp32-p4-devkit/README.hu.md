---
title: Olimex ESP32-P4-DevKit
slug: olimex-esp32-p4-devkit
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-devkit/
image: img/board-01.jpg
image_alt: Az Olimex ESP32-P4-DevKit panel az Ethernet aljzattal és a tüskesorokkal
tags:
- esp32-p4
- ethernet
- olimex
---

# Olimex ESP32-P4-DevKit

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Az Olimex ESP32-P4-DevKit panel az Ethernet aljzattal és a tüskesorokkal](img/board-01.jpg)

Az Olimex ESP32-P4-DevKit egy kis nyílt forrású panel az ESP32-P4-gyel - a leggyorsabb ESP32, két mag 400 MHz-en és 32 MB PSRAM - és 100 Mb-es Ethernettel. Nincs Wi-Fi-je: vezetékes vezérlő. A ctrl32-vel a legnagyobb programokat futtatja, amelyekre egy ESP32 képes - 4096 változó -, a kezelőoldala bármely böngészőben (WEBview), Modbus TCP és MQTT TLS-sel.

**Mire jó:**

- Vezetékes PLC nagy programmal és sok Modbus eszközzel
- Átjáró összetett logikával a Modbus TCP és az MQTT között
- Saját P4-es panel fejlesztése

A panel oldala a katalógusban: [Olimex ESP32-P4-DevKit](https://ctrl32.com/hardware/boards/olimex-esp32-p4-devkit/)

![Olimex ESP32-P4-DevKit - lábkiosztás: minden GPIO funkciója a ctrl32-ben](pinout/pinout.png)

## Mire képes a ctrl32 ezen a panelen

<!-- capabilities:start -->
| Funkció | Ezen a panelen | Megjegyzés |
|---|---|---|
| Chip | ESP32-P4 (ESP32-P4NRW32) |  |
| Memória | 16 MB flash, 32 MB PSRAM |  |
| Programméret | 4096 változó, 512 riasztás, 1024 blokk | a szerkesztő letöltés előtt ellenőrzi |
| Digitális bemenetek / kimenetek | 11 szabad GPIO | lásd a lábkiosztást |
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
| Tápellátás | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Ami nem támogatott

- A MIPI DSI kijelző- és a CSI kameracsatlakozók - ez a panel a ctrl32-ben kijelző nélkül fut (a kezelőoldal a WEBview).
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

-

## Tovább

- [ctrl32 dokumentáció](https://ctrl32.com/docs/) - a szerkesztő, a nyelvek, minden blokk
- [A szerkesztő letöltése](https://ctrl32.com/download/)
- [Minden tesztelt panel](../../README.hu.md)
- [Makerfabs MaTouch ESP32-P4 7"](../../makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.hu.md) - az ESP32-P4 egy 7"-os érintőképernyővel

