---
title: Makerfabs MaTouch Lite ESP32-S3 3.95"
slug: makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/
image: img/board-01.jpg
image_alt: A Makerfabs MaTouch Lite ESP32-S3 panel a 3,95 hüvelykes érintőkijelzőjével
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Makerfabs MaTouch Lite ESP32-S3 3.95"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 320x480](https://img.shields.io/badge/HMI-320x480-0891b2)

![A Makerfabs MaTouch Lite ESP32-S3 panel a 3,95 hüvelykes érintőkijelzőjével](img/board-01.jpg)

A Makerfabs MaTouch Lite egy olcsó érintőpanel: 3,95"-os, 320 x 480-as kijelző rezisztív érintéssel egy PSRAM-os, Wi-Fi-s ESP32-S3-on. A ctrl32-vel HMI és PLC egyben - a szerkesztőben rajzolt képernyők a kijelzőn, mellettük létraprogram, ugyanazok az értékek bármely böngészőben (WEBview), Modbus TCP, CAN és MQTT. A rezisztív érintés kesztyűben is működik.

**Mire jó:**

- Kis kezelőpanel egy gépen, kesztyűben kezelve
- Fali termosztát vagy helyiségszabályozó
- CAN kijelző egy járműhöz vagy egy hajtáshoz

A panel oldala a katalógusban: [Makerfabs MaTouch Lite ESP32-S3 3.95"](https://ctrl32.com/hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/)

![Makerfabs MaTouch Lite ESP32-S3 3.95" - lábkiosztás: minden GPIO funkciója a ctrl32-ben](pinout/pinout.png)

## Mire képes a ctrl32 ezen a panelen

<!-- capabilities:start -->
| Funkció | Ezen a panelen | Megjegyzés |
|---|---|---|
| Chip | ESP32-S3 (esp32s3_wroom_1_n16r8) |  |
| Memória | 16 MB flash, 8 MB PSRAM |  |
| Programméret | 512 változó, 128 riasztás, 512 blokk | a szerkesztő letöltés előtt ellenőrzi |
| Digitális bemenetek / kimenetek | 4 szabad GPIO | lásd a lábkiosztást |
| Analóg bemenetek | 4 a chipen (ADC1) | GPIO4, GPIO5, GPIO6, GPIO7 |
| Ethernet | nem |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 | külső adó-vevő kell hozzá |
| Modbus RTU (RS-485) | igen | szabad lábakon, külső adó-vevő kell hozzá |
| Modbus TCP | kliens és szerver |  |
| MQTT | igen (TLS is) | Home Assistant discovery |
| WEBview | igen | a kezelőoldal bármely böngészőben |
| Kijelző / érintés (HMI) | 3.95" 320x480, NS2009 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Tápellátás | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ami nem támogatott

- Bluetooth.
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
- [Makerfabs MaTouch ESP32-P4 7"](../makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.hu.md) - a nagy testvér

