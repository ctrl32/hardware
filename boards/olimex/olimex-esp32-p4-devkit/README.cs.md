---
title: Olimex ESP32-P4-DevKit
slug: olimex-esp32-p4-devkit
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-devkit/
image: img/board-01.jpg
image_alt: Deska Olimex ESP32-P4-DevKit s konektorem Ethernet a pinovými lištami
tags:
- esp32-p4
- ethernet
- olimex
---

# Olimex ESP32-P4-DevKit

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Deska Olimex ESP32-P4-DevKit s konektorem Ethernet a pinovými lištami](img/board-01.jpg)

Olimex ESP32-P4-DevKit je malá otevřená deska s ESP32-P4 - nejrychlejším ESP32, dvoujádrovým na 400 MHz s 32 MB PSRAM - a 100 Mb Ethernetem. Nemá Wi-Fi: je to řízení připojené kabelem. S ctrl32 na ní běží největší programy, jaké ESP32 zvládne - 4096 proměnných - se stránkou operátora v libovolném prohlížeči (WEBview), Modbus TCP a MQTT s TLS.

**Hodí se na:**

- PLC připojené kabelem, s velkým programem a mnoha zařízeními Modbus
- Brána s rozsáhlou logikou mezi Modbus TCP a MQTT
- Vývoj vlastní desky s P4

Stránka desky v katalogu: [Olimex ESP32-P4-DevKit](https://ctrl32.com/hardware/boards/olimex-esp32-p4-devkit/)

![Olimex ESP32-P4-DevKit - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | ESP32-P4 (ESP32-P4NRW32) |  |
| Paměť | 16 MB flash, 32 MB PSRAM |  |
| Velikost programu | 4096 proměnných, 512 alarmů, 1024 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | 11 volných GPIO | viz mapa pinů |
| Analogové vstupy | přes I2C převodník (ADS1115) |  |
| Ethernet | ano - IP101GRI |  |
| Wi-Fi | ne |  |
| CAN (TWAI) | 1 - na volných pinech | potřebuje externí převodník |
| Modbus RTU (RS-485) | ano - na volných pinech | potřebuje externí převodník |
| Modbus TCP | klient i server |  |
| MQTT | ano (i TLS) | objevení v Home Assistant |
| WEBview | ano | stránka operátora v každém prohlížeči |
| Displej / dotyk (HMI) | ne | stránka operátora je WEBview |
| USB | USB-C (Native USB) |  |
| Napájení | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Co není podporováno

- Konektory displeje MIPI DSI a kamery CSI - v ctrl32 tato deska běží bez displeje (stránka operátora je WEBview).
- Slot microSD - ctrl32 drží program i obrazovky ve flash paměti desky.

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
- [Makerfabs MaTouch ESP32-P4 7"](../../makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.cs.md) - ESP32-P4 se 7" dotykovou obrazovkou

