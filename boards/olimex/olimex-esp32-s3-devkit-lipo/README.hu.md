---
title: Olimex ESP32-S3-DevKit-Lipo
slug: olimex-esp32-s3-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-s3-devkit-lipo/
image: img/board-01.jpg
image_alt: Az Olimex ESP32-S3-DevKit-Lipo panel a két USB-C csatlakozójával és a tüskesoraival
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Olimex ESP32-S3-DevKit-Lipo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Az Olimex ESP32-S3-DevKit-Lipo panel a két USB-C csatlakozójával és a tüskesoraival](img/board-01.jpg)

Az Olimex ESP32-S3-DevKit-Lipo egy nyílt forrású ESP32-S3 panel 8 MB flash-sel, 8 MB PSRAM-mal, Wi-Fi-vel, két USB-C porttal és egy Li-Po töltővel. A PSRAM-os S3 a ctrl32 referencia-chipje: létraprogram teljes programmérettel, a kezelőoldala bármely böngészőben (WEBview), Modbus TCP és MQTT TLS-sel - mindez Wi-Fi-n.

**Mire jó:**

- Wi-Fi-s PLC bővítési tartalékkal - 512 változó, TLS egy felhős bróker felé
- Akkumulátoros vezérlés, amely áramszünetben is tovább fut
- Saját panel fejlesztése ESP32-S3 alapon

A panel oldala a katalógusban: [Olimex ESP32-S3-DevKit-Lipo](https://ctrl32.com/hardware/boards/olimex-esp32-s3-devkit-lipo/)

![Olimex ESP32-S3-DevKit-Lipo - lábkiosztás: minden GPIO funkciója a ctrl32-ben](pinout/pinout.png)

## Mire képes a ctrl32 ezen a panelen

<!-- capabilities:start -->
| Funkció | Ezen a panelen | Megjegyzés |
|---|---|---|
| Chip | ESP32-S3 (ESP32-S3-WROOM-1-N8R8) |  |
| Memória | 8 MB flash, 8 MB PSRAM |  |
| Programméret | 512 változó, 128 riasztás, 1024 blokk | a szerkesztő letöltés előtt ellenőrzi |
| Digitális bemenetek / kimenetek | 21 szabad GPIO | lásd a lábkiosztást |
| Analóg bemenetek | 9 a chipen (ADC1) | GPIO1, GPIO2, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 |
| Ethernet | nem |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus RTU (RS-485) | igen - szabad lábakon | külső adó-vevő kell hozzá |
| Modbus TCP | kliens és szerver |  |
| MQTT | igen (TLS is) | Home Assistant discovery |
| WEBview | igen | a kezelőoldal bármely böngészőben |
| Kijelző / érintés (HMI) | nem | a kezelőoldal a WEBview |
| USB | USB-C (CH340X USB-UART, Native USB) |  |
| Tápellátás | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ami nem támogatott

- Bluetooth - az ESP32-S3-ban megvan, a ctrl32 nem használja.
- Az akkumulátor- és tápfigyelő bemenetek (GPIO5 / GPIO6) a ctrl32-ben szabad lábak, nem töltöttségjelzők.

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
- [Olimex ESP32-DevKit-LiPo](../olimex-esp32-devkit-lipo/README.hu.md) - a klasszikus ESP32 változat

