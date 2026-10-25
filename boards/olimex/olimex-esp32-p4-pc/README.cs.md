---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Deska Olimex ESP32-P4-PC s konektorem Ethernet, porty USB a konektorem HDMI
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Deska Olimex ESP32-P4-PC s konektorem Ethernet, porty USB a konektorem HDMI](img/board-01.jpg)

Olimex ESP32-P4-PC je malý počítač na ESP32-P4 - dvoujádrovém na 400 MHz s 32 MB PSRAM - se 100 Mb Ethernetem, čtyřmi porty USB host, HDMI, zvukem a baterií Li-Po, která ho udrží v chodu i při výpadku napájení. S ctrl32 je to řízení připojené kabelem s největším programem, jaký ESP32 zvládne - 4096 proměnných - se stránkou operátora v libovolném prohlížeči (WEBview), Modbus TCP, MQTT s TLS a CAN nebo RS-485 na volných pinech lišty.

**Hodí se na:**

- PLC připojené kabelem, které výpadek napájení překlene na vlastní baterii
- Brána s rozsáhlou logikou mezi Modbus TCP, CAN a MQTT
- Řízení v rozvaděči napájené přes PoE (s rozšiřujícím modulem)

Stránka desky v katalogu: [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | ESP32-P4 (ESP32-P4NRW32) |  |
| Paměť | 16 MB flash, 32 MB PSRAM |  |
| Velikost programu | 4096 proměnných, 512 alarmů, 1024 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | 15 volných GPIO | viz mapa pinů |
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
| Napájení | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Co není podporováno

- Výstup HDMI a konektory MIPI DSI / CSI - v ctrl32 tato deska běží bez displeje (stránka operátora je WEBview).
- Porty USB host a zvukový výstup.
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

| Soubor | Co |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | mapa pinů, vektorová (i [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | odkud jsou fotky, schémata a modely |

## Dále

- [Dokumentace ctrl32](https://ctrl32.com/docs/) - editor, jazyky, každý blok
- [Stáhni editor](https://ctrl32.com/download/)
- [Všechny otestované desky](../../README.cs.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.cs.md) - stejný ESP32-P4 na menší desce

