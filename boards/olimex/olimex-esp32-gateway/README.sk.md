---
title: Olimex ESP32-GATEWAY
slug: olimex-esp32-gateway
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-gateway/
image: img/board-01.jpg
image_alt: Doska Olimex ESP32-GATEWAY s konektorom Ethernet a USB-C
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Olimex ESP32-GATEWAY

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Doska Olimex ESP32-GATEWAY s konektorom Ethernet a USB-C](img/board-01.jpg)

Olimex ESP32-GATEWAY je kompaktná doska s ESP32, 100 Mb Ethernetom a Wi-Fi - dosť malá do rozbočovacej krabice. S ctrl32 je to brána s vlastnou logikou: zariadenia Modbus TCP čítané a posielané cez MQTT, ladder program v čipe a jeho stránka operátora v ľubovoľnom prehliadači (WEBview).

**Hodí sa na:**

- Brána Modbus TCP do MQTT s vlastnou logikou
- Malý riadiaci systém v rozbočovacej krabici, na Ethernete
- Domáca automatizácia - čítanie elektromerov, spínanie cez I/O moduly Modbus

Stránka dosky v katalógu: [Olimex ESP32-GATEWAY](https://ctrl32.com/hardware/boards/olimex-esp32-gateway/)

![Olimex ESP32-GATEWAY - mapa pinov: funkcia každého GPIO v ctrl32](pinout/pinout.png)

## Čo ctrl32 na tejto doske dokáže

<!-- capabilities:start -->
| Vlastnosť | Na tejto doske | Poznámka |
|---|---|---|
| Čip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Pamäť | 4 MB flash |  |
| Veľkosť programu | 128 premenných, 32 alarmov, 128 blokov | editor ho overí pred nahratím |
| Digitálne vstupy / výstupy | 3 voľných GPIO | 1 z nich len vstupy |
| Analógové vstupy | 2 na čipe (ADC1) | GPIO33, GPIO34 |
| Ethernet | áno - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na voľných pinoch | treba externý prevodník |
| Modbus RTU (RS-485) | áno - na voľných pinoch | treba externý prevodník |
| Modbus TCP | klient aj server |  |
| MQTT | áno | objavenie v Home Assistant |
| WEBview | áno | stránka operátora v každom prehliadači |
| Displej / dotyk (HMI) | nie | stránka operátora je WEBview |
| USB | USB-C (CH340 USB-UART) |  |
| Napájanie | 5 V USB |  |
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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.sk.md) - Ethernet a napájanie cez Ethernet

