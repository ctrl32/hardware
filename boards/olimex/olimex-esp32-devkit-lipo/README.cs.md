---
title: Olimex ESP32-DevKit-LiPo
slug: olimex-esp32-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-devkit-lipo/
image: img/board-01.jpg
image_alt: Deska Olimex ESP32-DevKit-LiPo se dvěma pinovými lištami a konektorem micro-USB
tags:
- esp32
- wifi
- battery
- olimex
---

# Olimex ESP32-DevKit-LiPo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Deska Olimex ESP32-DevKit-LiPo se dvěma pinovými lištami a konektorem micro-USB](img/board-01.jpg)

Olimex ESP32-DevKit-LiPo je otevřená vývojová deska s ESP32, Wi-Fi, všemi GPIO modulu na dvou pinových lištách a nabíječkou Li-Po, která ji udrží v chodu při výpadku napájení. S ctrl32 je to malé PLC na Wi-Fi: ladder program v čipu, vstupy a výstupy na jejích pinech, operátorská stránka v libovolném prohlížeči (WEBview), Modbus TCP a MQTT.

**Hodí se na:**

- Řízení přes Wi-Fi pro místnost, skleník nebo čerpadlo
- Záznamník dat zálohovaný baterií, který posílá přes MQTT
- Seznámení s ctrl32 na nepájivém poli

Stránka desky v katalogu: [Olimex ESP32-DevKit-LiPo](https://ctrl32.com/hardware/boards/olimex-esp32-devkit-lipo/)

![Olimex ESP32-DevKit-LiPo - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Paměť | 4 MB flash |  |
| Velikost programu | 128 proměnných, 32 alarmů, 128 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | 19 volných GPIO | 4 z nich jen vstupy |
| Analogové vstupy | 6 na čipu (ADC1) | GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO39 |
| Ethernet | ne |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na volných pinech | potřebuje externí převodník |
| Modbus RTU (RS-485) | ano - na volných pinech | potřebuje externí převodník |
| Modbus TCP | klient i server |  |
| MQTT | ano | objevení v Home Assistant |
| WEBview | ano | stránka operátora v každém prohlížeči |
| Displej / dotyk (HMI) | ne | stránka operátora je WEBview |
| USB | Micro-USB (CH340 USB-UART) |  |
| Napájení | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Co není podporováno

- Bluetooth - ESP32 ho má, ctrl32 ho nepoužívá.
- Vstupy pro snímání baterie a napájení (GPIO35 / GPIO39) jsou v ctrl32 volné piny, ne měřič baterie.

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
- Olimex ESP32-S3-DevKit-Lipo - stejná myšlenka s ESP32-S3 a PSRAM

