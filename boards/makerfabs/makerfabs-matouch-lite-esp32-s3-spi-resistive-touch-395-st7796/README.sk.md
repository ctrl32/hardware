---
title: Makerfabs MaTouch Lite ESP32-S3 3.95"
slug: makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/
image: img/board-01.jpg
image_alt: Doska Makerfabs MaTouch Lite ESP32-S3 s dotykovým displejom 3,95 palca
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

![Doska Makerfabs MaTouch Lite ESP32-S3 s dotykovým displejom 3,95 palca](img/board-01.jpg)

Makerfabs MaTouch Lite je lacný dotykový panel: displej 3,95" 320 x 480 s odporovým dotykom na ESP32-S3 s PSRAM a Wi-Fi. S ctrl32 je to HMI aj PLC v jednom - obrazovky nakreslené v editore na skle, ladder program vedľa nich, tie isté hodnoty v ľubovoľnom prehliadači (WEBview), Modbus TCP, CAN a MQTT. Odporový dotyk funguje aj v rukaviciach.

**Hodí sa na:**

- Malý operátorský panel na stroji, ovládaný v rukaviciach
- Nástenný termostat alebo regulátor miestnosti
- Displej CAN pre vozidlo alebo menič

Stránka dosky v katalógu: [Makerfabs MaTouch Lite ESP32-S3 3.95"](https://ctrl32.com/hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/)

![Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa pinov: funkcia každého GPIO v ctrl32](pinout/pinout.png)

## Čo ctrl32 na tejto doske dokáže

<!-- capabilities:start -->
| Vlastnosť | Na tejto doske | Poznámka |
|---|---|---|
| Čip | ESP32-S3 (esp32s3_wroom_1_n16r8) |  |
| Pamäť | 16 MB flash, 8 MB PSRAM |  |
| Veľkosť programu | 512 premenných, 128 alarmov, 512 blokov | editor ho overí pred nahratím |
| Digitálne vstupy / výstupy | 4 voľných GPIO | pozri mapu pinov |
| Analógové vstupy | 4 na čipe (ADC1) | GPIO4, GPIO5, GPIO6, GPIO7 |
| Ethernet | nie |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 | treba externý prevodník |
| Modbus RTU (RS-485) | áno | na voľných pinoch, treba externý prevodník |
| Modbus TCP | klient aj server |  |
| MQTT | áno (aj TLS) | objavenie v Home Assistant |
| WEBview | áno | stránka operátora v každom prehliadači |
| Displej / dotyk (HMI) | 3.95" 320x480, NS2009 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Napájanie | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Čo nie je podporované

- Bluetooth.
- Slot microSD - ctrl32 drží program aj obrazovky vo flash pamäti dosky.

## Návod

| Krok | Stránka |
|---|---|
| 1 | [Hardvér a zapojenie](hardware.sk.md) - čo treba, napájanie, mapa pinov |
| 2 | [Nahratie runtime](install.sk.md) - editor, doska, prvé nahratie |
| 3 | [Nastavenie](configure.sk.md) - sieť, vstupy a výstupy, komunikácia |
| 4 | [Vzorové projekty](examples/README.sk.md) - všetko, čo doska dokáže, pripravené na otvorenie |
| - | [Riešenie problémov](troubleshooting.sk.md) |

## Súbory

-

## Ďalej

- [Dokumentácia ctrl32](https://ctrl32.com/docs/) - editor, jazyky, každý blok
- [Stiahni editor](https://ctrl32.com/download/)
- [Všetky otestované dosky](../../README.sk.md)
- [Makerfabs MaTouch ESP32-P4 7"](../makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.sk.md) - väčší súrodenec

