---
title: Olimex ESP32-GATEWAY
slug: olimex-esp32-gateway
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-gateway/
image: img/board-01.jpg
image_alt: Deska Olimex ESP32-GATEWAY s konektorem Ethernet a USB-C
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Olimex ESP32-GATEWAY

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Deska Olimex ESP32-GATEWAY s konektorem Ethernet a USB-C](img/board-01.jpg)

Olimex ESP32-GATEWAY je kompaktní deska s ESP32, 100 Mb Ethernetem a Wi-Fi - dost malá do instalační krabice. S ctrl32 je to brána s vlastní logikou: zařízení Modbus TCP čtená a posílaná přes MQTT, ladder program v čipu a jeho operátorská stránka v libovolném prohlížeči (WEBview).

**Hodí se na:**

- Brána Modbus TCP do MQTT s vlastní logikou
- Malý řídicí systém v instalační krabici, na Ethernetu
- Domácí automatizace - čtení elektroměrů, spínání přes I/O moduly Modbus

Stránka desky v katalogu: [Olimex ESP32-GATEWAY](https://ctrl32.com/hardware/boards/olimex-esp32-gateway/)

![Olimex ESP32-GATEWAY - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Paměť | 4 MB flash |  |
| Velikost programu | 128 proměnných, 32 alarmů, 128 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | 3 volných GPIO | 1 z nich jen vstupy |
| Analogové vstupy | 2 na čipu (ADC1) | GPIO33, GPIO34 |
| Ethernet | ano - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na volných pinech | potřebuje externí převodník |
| Modbus RTU (RS-485) | ano - na volných pinech | potřebuje externí převodník |
| Modbus TCP | klient i server |  |
| MQTT | ano | objevení v Home Assistant |
| WEBview | ano | stránka operátora v každém prohlížeči |
| Displej / dotyk (HMI) | ne | stránka operátora je WEBview |
| USB | USB-C (CH340 USB-UART) |  |
| Napájení | 5 V USB |  |
<!-- capabilities:end -->

### Co není podporováno

- Bluetooth - ESP32 ho má, ctrl32 ho nepoužívá.
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

