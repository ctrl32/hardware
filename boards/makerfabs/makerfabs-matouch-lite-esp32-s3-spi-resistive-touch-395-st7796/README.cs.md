---
title: Makerfabs MaTouch Lite ESP32-S3 3.95"
slug: makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/
image: img/board-01.jpg
image_alt: Deska Makerfabs MaTouch Lite ESP32-S3 s dotykovým displejem 3,95 palce
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

![Deska Makerfabs MaTouch Lite ESP32-S3 s dotykovým displejem 3,95 palce](img/board-01.jpg)

Makerfabs MaTouch Lite je levný dotykový panel: displej 3,95" 320 x 480 s odporovým dotykem na ESP32-S3 s PSRAM a Wi-Fi. S ctrl32 je to HMI a PLC v jednom - obrazovky nakreslené v editoru na skle, ladder program vedle nich, tytéž hodnoty v libovolném prohlížeči (WEBview), Modbus TCP, CAN a MQTT. Odporový dotyk funguje i v rukavicích.

**Hodí se na:**

- Malý operátorský panel na stroji, ovládaný v rukavicích
- Nástěnný termostat nebo regulátor místnosti
- Displej CAN pro vozidlo nebo měnič

Stránka desky v katalogu: [Makerfabs MaTouch Lite ESP32-S3 3.95"](https://ctrl32.com/hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/)

![Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | ESP32-S3 (esp32s3_wroom_1_n16r8) |  |
| Paměť | 16 MB flash, 8 MB PSRAM |  |
| Velikost programu | 512 proměnných, 128 alarmů, 512 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | 4 volných GPIO | viz mapa pinů |
| Analogové vstupy | 4 na čipu (ADC1) | GPIO4, GPIO5, GPIO6, GPIO7 |
| Ethernet | ne |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 | potřebuje externí převodník |
| Modbus RTU (RS-485) | ano | na volných pinech, potřebuje externí převodník |
| Modbus TCP | klient i server |  |
| MQTT | ano (i TLS) | objevení v Home Assistant |
| WEBview | ano | stránka operátora v každém prohlížeči |
| Displej / dotyk (HMI) | 3.95" 320x480, NS2009 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Napájení | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Co není podporováno

- Bluetooth.
- Slot microSD - ctrl32 drží program i obrazovky ve flash paměti desky.

## Návod

| Krok | Stránka |
|---|---|
| 1 | [Hardware a zapojení](hardware.cs.md) - co je potřeba, napájení, mapa pinů |
| 2 | [Nahrání runtime](install.cs.md) - editor, deska, první nahrání |
| 3 | [Nastavení](configure.cs.md) - síť, vstupy a výstupy, komunikace |
| 4 | [Vzorové projekty](examples/README.cs.md) - všechno, co deska umí, připravené k otevření |
| - | [Řešení problémů](troubleshooting.cs.md) |

## Soubory

-

## Dále

- [Dokumentace ctrl32](https://ctrl32.com/docs/) - editor, jazyky, každý blok
- [Stáhni editor](https://ctrl32.com/download/)
- [Všechny otestované desky](../../README.cs.md)
- [Makerfabs MaTouch ESP32-P4 7"](../makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.cs.md) - větší sourozenec

