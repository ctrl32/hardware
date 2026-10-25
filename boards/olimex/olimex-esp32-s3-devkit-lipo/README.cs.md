---
title: Olimex ESP32-S3-DevKit-Lipo
slug: olimex-esp32-s3-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-s3-devkit-lipo/
image: img/board-01.jpg
image_alt: Deska Olimex ESP32-S3-DevKit-Lipo se dvěma konektory USB-C a pinovými lištami
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Olimex ESP32-S3-DevKit-Lipo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Deska Olimex ESP32-S3-DevKit-Lipo se dvěma konektory USB-C a pinovými lištami](img/board-01.jpg)

Olimex ESP32-S3-DevKit-Lipo je otevřená deska s ESP32-S3, 8 MB flash, 8 MB PSRAM, Wi-Fi, dvěma porty USB-C a nabíječkou Li-Po. S3 s PSRAM je referenční čip ctrl32: ladder program v plné velikosti, stránka operátora v libovolném prohlížeči (WEBview), Modbus TCP a MQTT s TLS - to všechno přes Wi-Fi.

**Hodí se na:**

- Wi-Fi PLC s rezervou - 512 proměnných, TLS do cloudového brokeru
- Řízení zálohované baterií, které běží i při výpadku napájení
- Vývoj vlastní desky na ESP32-S3

Stránka desky v katalogu: [Olimex ESP32-S3-DevKit-Lipo](https://ctrl32.com/hardware/boards/olimex-esp32-s3-devkit-lipo/)

![Olimex ESP32-S3-DevKit-Lipo - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | ESP32-S3 (ESP32-S3-WROOM-1-N8R8) |  |
| Paměť | 8 MB flash, 8 MB PSRAM |  |
| Velikost programu | 512 proměnných, 128 alarmů, 1024 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | 21 volných GPIO | viz mapa pinů |
| Analogové vstupy | 9 na čipu (ADC1) | GPIO1, GPIO2, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 |
| Ethernet | ne |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na volných pinech | potřebuje externí převodník |
| Modbus RTU (RS-485) | ano - na volných pinech | potřebuje externí převodník |
| Modbus TCP | klient i server |  |
| MQTT | ano (i TLS) | objevení v Home Assistant |
| WEBview | ano | stránka operátora v každém prohlížeči |
| Displej / dotyk (HMI) | ne | stránka operátora je WEBview |
| USB | USB-C (CH340X USB-UART, Native USB) |  |
| Napájení | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Co není podporováno

- Bluetooth - ESP32-S3 ho má, ctrl32 ho nepoužívá.
- Vstupy pro snímání baterie a napájení (GPIO5 / GPIO6) jsou v ctrl32 volné piny, ne měřič baterie.

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
- [Olimex ESP32-DevKit-LiPo](../olimex-esp32-devkit-lipo/README.cs.md) - verze s klasickým ESP32

