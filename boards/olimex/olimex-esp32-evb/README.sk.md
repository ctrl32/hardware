---
title: Olimex ESP32-EVB
slug: olimex-esp32-evb
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-evb/
image: img/board-01.jpg
image_alt: Doska Olimex ESP32-EVB s dvoma relé, konektorom Ethernet a svorkou CAN
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Olimex ESP32-EVB

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 240x320](https://img.shields.io/badge/HMI-240x320-0891b2)

![Doska Olimex ESP32-EVB s dvoma relé, konektorom Ethernet a svorkou CAN](img/board-01.jpg)

Olimex ESP32-EVB je doska s ESP32 stavaná na riadenie: dve relé (10 A / 250 VAC), prevodník CAN, Ethernet a Wi-Fi na jednej doske. S ctrl32 je to hotové PLC - relé a tlačidlo sú premenné ladder programu, CAN sa rozpráva s meničmi a I/O uzlami a stránka operátora beží v ľubovoľnom prehliadači (WEBview). Voliteľný 2,8" dotykový displej na konektore UEXT z nej spraví malý panel.

**Hodí sa na:**

- Reléové riadenie - kúrenie, čerpadlá, svetlá - s Ethernetom
- CAN master pre menič alebo I/O uzly CANopen
- Termostat alebo malý panel s voliteľným 2,8" displejom

Stránka dosky v katalógu: [Olimex ESP32-EVB](https://ctrl32.com/hardware/boards/olimex-esp32-evb/)

![Olimex ESP32-EVB - mapa pinov: funkcia každého GPIO v ctrl32](pinout/pinout.png)

## Čo ctrl32 na tejto doske dokáže

<!-- capabilities:start -->
| Vlastnosť | Na tejto doske | Poznámka |
|---|---|---|
| Čip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Pamäť | 4 MB flash |  |
| Veľkosť programu | 128 premenných, 32 alarmov, 128 blokov | editor ho overí pred nahratím |
| Digitálne vstupy / výstupy | 6 voľných GPIO | 2 z nich len vstupy |
| Analógové vstupy | 4 na čipe (ADC1) | GPIO32, GPIO33, GPIO34, GPIO36 |
| Ethernet | áno - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 |  |
| Modbus RTU (RS-485) | áno - na voľných pinoch | treba externý prevodník |
| Modbus TCP | klient aj server |  |
| MQTT | áno | objavenie v Home Assistant |
| WEBview | áno | stránka operátora v každom prehliadači |
| Displej / dotyk (HMI) | - 240x320, - |  |
| USB | Micro-USB (CH340T USB-UART) |  |
| Napájanie | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Čo nie je podporované

- Bluetooth.
- IR prijímač a vysielač - ctrl32 ich na tejto doske nepoužíva.
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

