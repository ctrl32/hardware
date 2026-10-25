---
title: Olimex ESP32-PoE
slug: olimex-esp32-poe
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/board-01.jpg
image_alt: Deska Olimex ESP32-PoE shora, s konektorem Ethernet a USB
tags:
- esp32
- ethernet
- poe
- olimex
---

# Olimex ESP32-PoE

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Deska Olimex ESP32-PoE shora, s konektorem Ethernet a USB](img/board-01.jpg)

Olimex ESP32-PoE je otevřená deska s ESP32, Ethernetem a napájením přes Ethernet (PoE): jeden síťový kabel ji napájí i připojuje do sítě. S ctrl32 se z ní stane kompaktní PLC do rozvaděče nebo do krabice na zeď - ladder program v čipu, operátorská stránka v libovolném prohlížeči v síti (WEBview), Modbus TCP k elektroměrům a I/O modulům a MQTT do Home Assistant nebo jiného brokeru.

**Hodí se na:**

- Malé PLC v rozvaděči napájené z PoE switche
- Brána Modbus TCP, která čte elektroměry a posílá je přes MQTT
- Domácí automatizace - místnost nebo kotelna na jednom kabelu

Stránka desky v katalogu: [Olimex ESP32-PoE](https://ctrl32.com/hardware/boards/olimex-esp32-poe/)

![Olimex ESP32-PoE - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Paměť | 4 MB flash |  |
| Velikost programu | 128 proměnných, 32 alarmů, 128 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | 6 volných GPIO | 3 z nich jen vstupy |
| Analogové vstupy | 4 na čipu (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | ano - LAN8710A |  |
| Napájení přes Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na volných pinech | potřebuje externí převodník |
| Modbus RTU (RS-485) | ano - na volných pinech | potřebuje externí převodník |
| Modbus TCP | klient i server |  |
| MQTT | ano | objevení v Home Assistant |
| WEBview | ano | stránka operátora v každém prohlížeči |
| Displej / dotyk (HMI) | ne | stránka operátora je WEBview |
| USB | Micro-USB (CH340T USB-UART) |  |
| Napájení | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Co není podporováno

- Bluetooth - ESP32 ho má, ctrl32 ho nepoužívá.
- Slot microSD - ctrl32 drží program i obrazovky ve vlastní flash paměti čipu.
- Vstup pro baterii funguje jako vlastnost desky; ctrl32 stav baterie nečte.

## Návod

| Krok | Stránka |
|---|---|
| 1 | [Hardware a zapojení](hardware.cs.md) - co je potřeba, napájení, mapa pinů |
| 2 | [Nahrání runtime](install.cs.md) - editor, deska, první nahrání |
| 3 | [Nastavení](configure.cs.md) - síť, vstupy a výstupy, komunikace |
| 4 | [Vzorové projekty](examples/README.cs.md) - všechno, co deska umí, připravené k otevření |
| - | [Řešení problémů](troubleshooting.cs.md) |

## Soubory

| Soubor | Co |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | mapa pinů, vektorová (i [PNG](pinout/pinout.png)) |
| [olimex-esp32-poe-schematic.pdf](schematics/olimex-esp32-poe-schematic.pdf) | ESP32-PoE schematic Rev M2 |
| [esp32-poe-revm2.zip](schematics/esp32-poe-revm2.zip) | KiCad project |
| [olimex-esp32-poe-user-manual.pdf](datasheets/olimex-esp32-poe-user-manual.pdf) | ESP32-PoE user manual |
| [olimex-esp32-poe.zip](3d/olimex-esp32-poe.zip) | 3D model (STEP, v zipu) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | odkud jsou fotky, schémata a modely |

## Dále

- [Dokumentace ctrl32](https://ctrl32.com/docs/) - editor, jazyky, každý blok
- [Stáhni editor](https://ctrl32.com/download/)
- Všechny otestované desky
- Olimex ESP32-PoE-ISO - stejná deska s odděleným napájením PoE
- Olimex ESP32-POE2 - další generace

