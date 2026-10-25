---
title: Olimex ESP32-POE2
slug: olimex-esp32-poe2
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe2/
image: img/board-01.jpg
image_alt: Deska Olimex ESP32-POE2 s konektorem Ethernet a napájecími výstupy
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Olimex ESP32-POE2

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Deska Olimex ESP32-POE2 s konektorem Ethernet a napájecími výstupy](img/board-01.jpg)

Olimex ESP32-POE2 je další generace ESP32-PoE: ESP32 s 8 MB PSRAM, Ethernetem a napájením přes Ethernet IEEE 802.3at, které napájí i tvoje zařízení v poli - výstupy 24 V nebo 12 V, 5 V a 3,3 V, celkem až 25 W ze síťového kabelu. S ctrl32 je to PLC v rozvaděči na jednom kabelu: ladder logika, WEBview, Modbus TCP a MQTT, s plnou velikostí programu klasického ESP32 s PSRAM.

**Hodí se na:**

- PLC v rozvaděči, které z PoE napájí své snímače a malý reléový modul
- Brána Modbus TCP s MQTT do Home Assistant
- Automatizace budovy na jednom kabelu na místnost

Stránka desky v katalogu: [Olimex ESP32-POE2](https://ctrl32.com/hardware/boards/olimex-esp32-poe2/)

![Olimex ESP32-POE2 - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | ESP32 (ESP32-WROVER-E-N4R8) |  |
| Paměť | 4 MB flash, 8 MB PSRAM |  |
| Velikost programu | 512 proměnných, 128 alarmů, 1024 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | 5 volných GPIO | 3 z nich jen vstupy |
| Analogové vstupy | 3 na čipu (ADC1) | GPIO34, GPIO36, GPIO39 |
| Ethernet | ano - LAN8710A |  |
| Napájení přes Ethernet | IEEE 802.3at |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na volných pinech | potřebuje externí převodník |
| Modbus RTU (RS-485) | ano - na volných pinech | potřebuje externí převodník |
| Modbus TCP | klient i server |  |
| MQTT | ano | objevení v Home Assistant |
| WEBview | ano | stránka operátora v každém prohlížeči |
| Displej / dotyk (HMI) | ne | stránka operátora je WEBview |
| USB | USB-C |  |
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

-

## Dále

- [Dokumentace ctrl32](https://ctrl32.com/docs/) - editor, jazyky, každý blok
- [Stáhni editor](https://ctrl32.com/download/)
- [Všechny otestované desky](../../README.cs.md)
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.cs.md) - první generace
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.cs.md) - s odděleným napájením PoE

