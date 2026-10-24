---
title: Olimex ESP32-S3-DevKit-Lipo
slug: olimex-esp32-s3-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-s3-devkit-lipo/
image: img/board-01.jpg
image_alt: Doska Olimex ESP32-S3-DevKit-Lipo s dvomi konektormi USB-C a lištami pinov
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Olimex ESP32-S3-DevKit-Lipo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Doska Olimex ESP32-S3-DevKit-Lipo s dvomi konektormi USB-C a lištami pinov](img/board-01.jpg)

Olimex ESP32-S3-DevKit-Lipo je otvorená doska s ESP32-S3, 8 MB flash, 8 MB PSRAM, Wi-Fi, dvomi portmi USB-C a nabíjačkou Li-Po. S3 s PSRAM je referenčný čip ctrl32: ladder program v plnej veľkosti, stránka operátora v ľubovoľnom prehliadači (WEBview), Modbus TCP a MQTT s TLS - všetko cez Wi-Fi.

**Hodí sa na:**

- Wi-Fi PLC s rezervou - 512 premenných, TLS do cloudového brokera
- Riadenie zálohované batériou, ktoré beží aj počas výpadku napájania
- Vývoj vlastnej dosky na ESP32-S3

Stránka dosky v katalógu: [Olimex ESP32-S3-DevKit-Lipo](https://ctrl32.com/hardware/boards/olimex-esp32-s3-devkit-lipo/)

![Olimex ESP32-S3-DevKit-Lipo - mapa pinov: funkcia každého GPIO v ctrl32](pinout/pinout.png)

## Čo ctrl32 na tejto doske dokáže

<!-- capabilities:start -->
| Vlastnosť | Na tejto doske | Poznámka |
|---|---|---|
| Čip | ESP32-S3 (ESP32-S3-WROOM-1-N8R8) |  |
| Pamäť | 8 MB flash, 8 MB PSRAM |  |
| Veľkosť programu | 512 premenných, 128 alarmov, 1024 blokov | editor ho overí pred nahratím |
| Digitálne vstupy / výstupy | 21 voľných GPIO | pozri mapu pinov |
| Analógové vstupy | 9 na čipe (ADC1) | GPIO1, GPIO2, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 |
| Ethernet | nie |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na voľných pinoch | treba externý prevodník |
| Modbus RTU (RS-485) | áno - na voľných pinoch | treba externý prevodník |
| Modbus TCP | klient aj server |  |
| MQTT | áno (aj TLS) | objavenie v Home Assistant |
| WEBview | áno | stránka operátora v každom prehliadači |
| Displej / dotyk (HMI) | nie | stránka operátora je WEBview |
| USB | USB-C (CH340X USB-UART, Native USB) |  |
| Napájanie | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Čo nie je podporované

- Bluetooth - ESP32-S3 ho má, ctrl32 ho nepoužíva.
- Vstupy snímania batérie a napájania (GPIO5 / GPIO6) sú v ctrl32 voľné piny, nie merač batérie.

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
- [Olimex ESP32-DevKit-LiPo](../olimex-esp32-devkit-lipo/README.sk.md) - verzia s klasickým ESP32

