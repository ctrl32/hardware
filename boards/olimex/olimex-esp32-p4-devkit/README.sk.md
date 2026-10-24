---
title: Olimex ESP32-P4-DevKit
slug: olimex-esp32-p4-devkit
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-devkit/
image: img/board-01.jpg
image_alt: Doska Olimex ESP32-P4-DevKit s konektorom Ethernet a lištami pinov
tags:
- esp32-p4
- ethernet
- olimex
---

# Olimex ESP32-P4-DevKit

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Doska Olimex ESP32-P4-DevKit s konektorom Ethernet a lištami pinov](img/board-01.jpg)

Olimex ESP32-P4-DevKit je malá otvorená doska s ESP32-P4 - najrýchlejším ESP32, dvojjadrovým na 400 MHz s 32 MB PSRAM - a 100 Mb Ethernetom. Nemá Wi-Fi: je to riadenie na kábli. S ctrl32 na nej bežia najväčšie programy, aké ESP32 zvládne - 4096 premenných - so stránkou operátora v ľubovoľnom prehliadači (WEBview), Modbus TCP a MQTT s TLS.

**Hodí sa na:**

- PLC na kábli s veľkým programom a mnohými zariadeniami Modbus
- Brána s rozsiahlou logikou medzi Modbus TCP a MQTT
- Vývoj vlastnej dosky s P4

Stránka dosky v katalógu: [Olimex ESP32-P4-DevKit](https://ctrl32.com/hardware/boards/olimex-esp32-p4-devkit/)

![Olimex ESP32-P4-DevKit - mapa pinov: funkcia každého GPIO v ctrl32](pinout/pinout.png)

## Čo ctrl32 na tejto doske dokáže

<!-- capabilities:start -->
| Vlastnosť | Na tejto doske | Poznámka |
|---|---|---|
| Čip | ESP32-P4 (ESP32-P4NRW32) |  |
| Pamäť | 16 MB flash, 32 MB PSRAM |  |
| Veľkosť programu | 4096 premenných, 512 alarmov, 1024 blokov | editor ho overí pred nahratím |
| Digitálne vstupy / výstupy | 11 voľných GPIO | pozri mapu pinov |
| Analógové vstupy | cez I2C prevodník (ADS1115) |  |
| Ethernet | áno - IP101GRI |  |
| Wi-Fi | nie |  |
| CAN (TWAI) | 1 - na voľných pinoch | treba externý prevodník |
| Modbus RTU (RS-485) | áno - na voľných pinoch | treba externý prevodník |
| Modbus TCP | klient aj server |  |
| MQTT | áno (aj TLS) | objavenie v Home Assistant |
| WEBview | áno | stránka operátora v každom prehliadači |
| Displej / dotyk (HMI) | nie | stránka operátora je WEBview |
| USB | USB-C (Native USB) |  |
| Napájanie | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Čo nie je podporované

- Konektory displeja MIPI DSI a kamery CSI - v ctrl32 táto doska beží bez displeja (stránka operátora je WEBview).
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
- [Makerfabs MaTouch ESP32-P4 7"](../../makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.sk.md) - ESP32-P4 so 7" dotykovou obrazovkou

