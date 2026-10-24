---
title: LaskaKit ESPlan
slug: laskakit-esplan
sidebar_position: 10
hardware: /hardware/boards/laskakit-esplan/
image: img/board-01.jpg
image_alt: Doska LaskaKit ESPlan s konektorom Ethernet, svorkou RS-485 a napájacou svorkou
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# LaskaKit ESPlan

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Doska LaskaKit ESPlan s konektorom Ethernet, svorkou RS-485 a napájacou svorkou](img/board-01.jpg)

LaskaKit ESPlan je priemyselná doska s ESP32: 10/100 Ethernet, rozhranie RS-485 s ochranou a prepínateľným zakončením, Wi-Fi a široké napájanie 7-40 V na skrutkovej svorke (alebo PoE s prídavným modulom). S ctrl32 je to Modbus RTU master alebo slave v rozvádzači - ladder program v čipe, zariadenia RS-485 čítané a zapisované, hodnoty na Modbus TCP, MQTT a na stránke operátora (WEBview).

**Hodí sa na:**

- Modbus RTU master pre elektromery, snímače a meniče, na napájaní 24 V
- Brána Modbus RTU / TCP s vlastnou logikou
- Automatizácia budov v rozvádzači

Stránka dosky v katalógu: [LaskaKit ESPlan](https://ctrl32.com/hardware/boards/laskakit-esplan/)

![LaskaKit ESPlan - mapa pinov: funkcia každého GPIO v ctrl32](pinout/pinout.png)

## Čo ctrl32 na tejto doske dokáže

<!-- capabilities:start -->
| Vlastnosť | Na tejto doske | Poznámka |
|---|---|---|
| Čip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Pamäť | 4 MB flash |  |
| Veľkosť programu | 128 premenných, 32 alarmov, 128 blokov | editor ho overí pred nahratím |
| Digitálne vstupy / výstupy | 5 voľných GPIO | 2 z nich len vstupy |
| Analógové vstupy | 2 na čipe (ADC1) | GPIO35, GPIO39 |
| Ethernet | áno - LAN8720A |  |
| Napájanie cez Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na voľných pinoch | treba externý prevodník |
| Modbus RTU (RS-485) | áno |  |
| Modbus TCP | klient aj server |  |
| MQTT | áno | objavenie v Home Assistant |
| WEBview | áno | stránka operátora v každom prehliadači |
| Displej / dotyk (HMI) | nie | stránka operátora je WEBview |
| USB | USB-C (CH9102 USB-UART) |  |
| Napájanie | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Čo nie je podporované

- Bluetooth - ESP32 ho má, ctrl32 ho nepoužíva.
- Slot microSD - ctrl32 drží program aj obrazovky vo vlastnej flash pamäti čipu.

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

