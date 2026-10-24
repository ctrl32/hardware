---
title: Olimex ESP32-POE2
slug: olimex-esp32-poe2
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe2/
image: img/board-01.jpg
image_alt: Doska Olimex ESP32-POE2 s konektorom Ethernet a napájacími výstupmi
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Olimex ESP32-POE2

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Doska Olimex ESP32-POE2 s konektorom Ethernet a napájacími výstupmi](img/board-01.jpg)

Olimex ESP32-POE2 je ďalšia generácia ESP32-PoE: ESP32 s 8 MB PSRAM, Ethernetom a napájaním cez Ethernet IEEE 802.3at, ktoré napája aj tvoje zariadenia v poli - výstupy 24 V alebo 12 V, 5 V a 3,3 V, spolu až 25 W zo sieťového kábla. S ctrl32 je to PLC v rozvádzači na jednom kábli: ladder logika, WEBview, Modbus TCP a MQTT, s plnou veľkosťou programu klasického ESP32 s PSRAM.

**Hodí sa na:**

- PLC v rozvádzači, ktoré z PoE napája svoje snímače a malý reléový modul
- Brána Modbus TCP s MQTT do Home Assistant
- Automatizácia budovy na jednom kábli na miestnosť

Stránka dosky v katalógu: [Olimex ESP32-POE2](https://ctrl32.com/hardware/boards/olimex-esp32-poe2/)

![Olimex ESP32-POE2 - mapa pinov: funkcia každého GPIO v ctrl32](pinout/pinout.png)

## Čo ctrl32 na tejto doske dokáže

<!-- capabilities:start -->
| Vlastnosť | Na tejto doske | Poznámka |
|---|---|---|
| Čip | ESP32 (ESP32-WROVER-E-N4R8) |  |
| Pamäť | 4 MB flash, 8 MB PSRAM |  |
| Veľkosť programu | 512 premenných, 128 alarmov, 1024 blokov | editor ho overí pred nahratím |
| Digitálne vstupy / výstupy | 5 voľných GPIO | 3 z nich len vstupy |
| Analógové vstupy | 3 na čipe (ADC1) | GPIO34, GPIO36, GPIO39 |
| Ethernet | áno - LAN8710A |  |
| Napájanie cez Ethernet | IEEE 802.3at |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na voľných pinoch | treba externý prevodník |
| Modbus RTU (RS-485) | áno - na voľných pinoch | treba externý prevodník |
| Modbus TCP | klient aj server |  |
| MQTT | áno | objavenie v Home Assistant |
| WEBview | áno | stránka operátora v každom prehliadači |
| Displej / dotyk (HMI) | nie | stránka operátora je WEBview |
| USB | USB-C |  |
| Napájanie | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Čo nie je podporované

- Bluetooth - ESP32 ho má, ctrl32 ho nepoužíva.
- Slot microSD - ctrl32 drží program aj obrazovky vo vlastnej flash pamäti čipu.
- Vstup batérie funguje ako vlastnosť dosky; ctrl32 nečíta stav batérie.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.sk.md) - prvá generácia
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.sk.md) - s oddeleným napájaním PoE

