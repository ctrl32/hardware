---
title: LaskaKit ESPlan
slug: laskakit-esplan
sidebar_position: 10
hardware: /hardware/boards/laskakit-esplan/
image: img/board-01.jpg
image_alt: Deska LaskaKit ESPlan s konektorem Ethernet, svorkou RS-485 a napájecí svorkou
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# LaskaKit ESPlan

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Deska LaskaKit ESPlan s konektorem Ethernet, svorkou RS-485 a napájecí svorkou](img/board-01.jpg)

LaskaKit ESPlan je průmyslová deska s ESP32: 10/100 Ethernet, rozhraní RS-485 s ochranou a přepínatelným zakončením, Wi-Fi a široké napájení 7-40 V na šroubovací svorce (nebo PoE s přídavným modulem). S ctrl32 je to Modbus RTU master nebo slave v rozvaděči - ladder program v čipu, zařízení na RS-485 čtená i zapisovaná, hodnoty na Modbus TCP, MQTT a na stránce operátora (WEBview).

**Hodí se na:**

- Modbus RTU master pro elektroměry, čidla a měniče, na napájení 24 V
- Brána Modbus RTU / TCP s vlastní logikou
- Automatizace budov v rozvaděči

Stránka desky v katalogu: [LaskaKit ESPlan](https://ctrl32.com/hardware/boards/laskakit-esplan/)

![LaskaKit ESPlan - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Paměť | 4 MB flash |  |
| Velikost programu | 128 proměnných, 32 alarmů, 128 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | 5 volných GPIO | 2 z nich jen vstupy |
| Analogové vstupy | 2 na čipu (ADC1) | GPIO35, GPIO39 |
| Ethernet | ano - LAN8720A |  |
| Napájení přes Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - na volných pinech | potřebuje externí převodník |
| Modbus RTU (RS-485) | ano |  |
| Modbus TCP | klient i server |  |
| MQTT | ano | objevení v Home Assistant |
| WEBview | ano | stránka operátora v každém prohlížeči |
| Displej / dotyk (HMI) | ne | stránka operátora je WEBview |
| USB | USB-C (CH9102 USB-UART) |  |
| Napájení | 5 V USB, PoE |  |
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

