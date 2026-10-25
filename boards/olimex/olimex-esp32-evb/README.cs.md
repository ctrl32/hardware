---
title: Olimex ESP32-EVB
slug: olimex-esp32-evb
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-evb/
image: img/board-01.jpg
image_alt: Deska Olimex ESP32-EVB se dvěma relé, konektorem Ethernet a svorkou CAN
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Olimex ESP32-EVB

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 240x320](https://img.shields.io/badge/HMI-240x320-0891b2)

![Deska Olimex ESP32-EVB se dvěma relé, konektorem Ethernet a svorkou CAN](img/board-01.jpg)

Olimex ESP32-EVB je deska s ESP32 stavěná na řízení: dvě relé (10 A / 250 VAC), převodník CAN, Ethernet a Wi-Fi na jedné desce. S ctrl32 je to hotové PLC - relé a tlačítko jsou proměnné ladder programu, CAN mluví s měniči a I/O uzly a operátorská stránka běží v libovolném prohlížeči (WEBview). Volitelný 2,8" dotykový displej na konektoru UEXT z ní udělá malý panel.

**Hodí se na:**

- Reléové řízení - topení, čerpadla, světla - s Ethernetem
- CAN master pro měnič nebo I/O uzly CANopen
- Termostat nebo malý panel s volitelným 2,8" displejem

Stránka desky v katalogu: [Olimex ESP32-EVB](https://ctrl32.com/hardware/boards/olimex-esp32-evb/)

![Olimex ESP32-EVB - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Paměť | 4 MB flash |  |
| Velikost programu | 128 proměnných, 32 alarmů, 128 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | 6 volných GPIO | 2 z nich jen vstupy |
| Analogové vstupy | 4 na čipu (ADC1) | GPIO32, GPIO33, GPIO34, GPIO36 |
| Ethernet | ano - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 |  |
| Modbus RTU (RS-485) | ano - na volných pinech | potřebuje externí převodník |
| Modbus TCP | klient i server |  |
| MQTT | ano | objevení v Home Assistant |
| WEBview | ano | stránka operátora v každém prohlížeči |
| Displej / dotyk (HMI) | - 240x320, - |  |
| USB | Micro-USB (CH340T USB-UART) |  |
| Napájení | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Co není podporováno

- Bluetooth.
- IR přijímač a vysílač - ctrl32 je na této desce nepoužívá.
- Slot microSD - ctrl32 drží program i obrazovky ve vlastní flash paměti čipu.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.cs.md) - Ethernet a napájení přes Ethernet

