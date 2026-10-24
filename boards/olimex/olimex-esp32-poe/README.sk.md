---
title: Olimex ESP32-PoE
slug: olimex-esp32-poe
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/board-01.jpg
image_alt: Doska Olimex ESP32-PoE zhora, s konektorom Ethernet a USB
tags:
- esp32
- ethernet
- poe
- olimex
---

# Olimex ESP32-PoE

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Doska Olimex ESP32-PoE zhora, s konektorom Ethernet a USB](img/board-01.jpg)

Olimex ESP32-PoE je otvorená doska s ESP32, Ethernetom a napájaním cez Ethernet (PoE): jeden sieťový kábel ju napája aj pripája do siete. S ctrl32 sa z nej stane kompaktné PLC do rozvádzača alebo krabice na stenu - ladder program v čipe, stránka operátora v ľubovoľnom prehliadači v sieti (WEBview), Modbus TCP k elektromerom a I/O modulom a MQTT do Home Assistant alebo iného brokera.

**Hodí sa na:**

- Malé PLC v rozvádzači napájané z PoE switchu
- Brána Modbus TCP, ktorá číta elektromery a posiela ich cez MQTT
- Domáca automatizácia - miestnosť alebo kotolňa na jednom kábli

Stránka dosky v katalógu: [Olimex ESP32-PoE](https://ctrl32.com/hardware/boards/olimex-esp32-poe/)

![Olimex ESP32-PoE - mapa pinov: funkcia každého GPIO v ctrl32](pinout/pinout.png)

## Čo ctrl32 na tejto doske dokáže

<!-- capabilities:start -->
| Vlastnosť | Na tejto doske | Poznámka |
|---|---|---|
| Čip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Pamäť | 4 MB flash |  |
| Veľkosť programu | 128 premenných, 32 alarmov, 128 blokov | editor ho overí pred nahratím |
| Digitálne vstupy / výstupy | 6 voľných GPIO | 3 z nich len vstupy |
| Analógové vstupy | 4 na čipe (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | áno - LAN8710A |  |
| Napájanie cez Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na voľných pinoch | treba externý prevodník |
| Modbus RTU (RS-485) | áno - na voľných pinoch | treba externý prevodník |
| Modbus TCP | klient aj server |  |
| MQTT | áno | objavenie v Home Assistant |
| WEBview | áno | stránka operátora v každom prehliadači |
| Displej / dotyk (HMI) | nie | stránka operátora je WEBview |
| USB | Micro-USB (CH340T USB-UART) |  |
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

| Súbor | Čo |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | mapa pinov, vektorová (aj [PNG](pinout/pinout.png)) |
| [olimex-esp32-poe-schematic.pdf](schematics/olimex-esp32-poe-schematic.pdf) | ESP32-PoE schematic Rev M2 |
| [esp32-poe-revm2.zip](schematics/esp32-poe-revm2.zip) | KiCad project |
| [olimex-esp32-poe-user-manual.pdf](datasheets/olimex-esp32-poe-user-manual.pdf) | ESP32-PoE user manual |
| [olimex-esp32-poe.zip](3d/olimex-esp32-poe.zip) | 3D model (STEP, v zip) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | odkiaľ sú fotky, schémy a modely |

## Ďalej

- [Dokumentácia ctrl32](https://ctrl32.com/docs/) - editor, jazyky, každý blok
- [Stiahni editor](https://ctrl32.com/download/)
- [Všetky otestované dosky](../../README.sk.md)
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.sk.md) - tá istá doska s oddeleným napájaním PoE
- [Olimex ESP32-POE2](../olimex-esp32-poe2/README.sk.md) - ďalšia generácia

