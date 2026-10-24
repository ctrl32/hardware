---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Doska Olimex ESP32-P4-PC s konektorom Ethernet, portmi USB a konektorom HDMI
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Doska Olimex ESP32-P4-PC s konektorom Ethernet, portmi USB a konektorom HDMI](img/board-01.jpg)

Olimex ESP32-P4-PC je malý počítač na ESP32-P4 - dvojjadrovom na 400 MHz s 32 MB PSRAM - so 100 Mb Ethernetom, štyrmi portmi USB host, HDMI, zvukom a batériou Li-Po, ktorá ho udrží v chode počas výpadku napájania. S ctrl32 je to riadenie na kábli s najväčším programom, aký ESP32 zvládne - 4096 premenných - so stránkou operátora v ľubovoľnom prehliadači (WEBview), Modbus TCP, MQTT s TLS a CAN alebo RS-485 na voľných pinoch lišty.

**Hodí sa na:**

- PLC na kábli, ktoré prečká výpadok napájania na vlastnej batérii
- Brána s rozsiahlou logikou medzi Modbus TCP, CAN a MQTT
- Riadenie v krabici napájané cez PoE (s rozširujúcim modulom)

Stránka dosky v katalógu: [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC - mapa pinov: funkcia každého GPIO v ctrl32](pinout/pinout.png)

## Čo ctrl32 na tejto doske dokáže

<!-- capabilities:start -->
| Vlastnosť | Na tejto doske | Poznámka |
|---|---|---|
| Čip | ESP32-P4 (ESP32-P4NRW32) |  |
| Pamäť | 16 MB flash, 32 MB PSRAM |  |
| Veľkosť programu | 4096 premenných, 512 alarmov, 1024 blokov | editor ho overí pred nahratím |
| Digitálne vstupy / výstupy | 15 voľných GPIO | pozri mapu pinov |
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
| Napájanie | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Čo nie je podporované

- Výstup HDMI a konektory MIPI DSI / CSI - v ctrl32 táto doska beží bez displeja (stránka operátora je WEBview).
- Porty USB host a zvukový výstup.
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

| Súbor | Čo |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | mapa pinov, vektorová (aj [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | odkiaľ sú fotky, schémy a modely |

## Ďalej

- [Dokumentácia ctrl32](https://ctrl32.com/docs/) - editor, jazyky, každý blok
- [Stiahni editor](https://ctrl32.com/download/)
- [Všetky otestované dosky](../../README.sk.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.sk.md) - to isté ESP32-P4 na menšej doske

