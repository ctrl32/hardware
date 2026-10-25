---
title: Olimex ESP32-P4-DevKit
slug: olimex-esp32-p4-devkit
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-devkit/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-P4-DevKit cu mufa Ethernet și conectorii de pini
tags:
- esp32-p4
- ethernet
- olimex
---

# Olimex ESP32-P4-DevKit

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Placa Olimex ESP32-P4-DevKit cu mufa Ethernet și conectorii de pini](img/board-01.jpg)

Olimex ESP32-P4-DevKit este o mică placă open-source cu ESP32-P4 - cel mai rapid ESP32, două nuclee la 400 MHz cu 32 MB de PSRAM - și Ethernet de 100 Mb. Nu are Wi-Fi: este un controler cu fir. Cu ctrl32 rulează cele mai mari programe pe care le poate rula un ESP32 - 4096 de variabile - cu pagina de operator în orice browser (WEBview), Modbus TCP și MQTT cu TLS.

**Potrivit pentru:**

- Un PLC cu fir, cu un program mare și multe dispozitive Modbus
- Un gateway cu logică bogată între Modbus TCP și MQTT
- Dezvoltarea propriei plăci P4

Pagina plăcii în catalog: [Olimex ESP32-P4-DevKit](https://ctrl32.com/hardware/boards/olimex-esp32-p4-devkit/)

![Olimex ESP32-P4-DevKit - harta pinilor: funcția fiecărui GPIO în ctrl32](pinout/pinout.png)

## Ce poate face ctrl32 pe această placă

<!-- capabilities:start -->
| Funcție | Pe această placă | Note |
|---|---|---|
| Cip | ESP32-P4 (ESP32-P4NRW32) |  |
| Memorie | 16 MB flash, 32 MB PSRAM |  |
| Mărimea programului | 4096 variabile, 512 alarme, 1024 blocuri | verificat de editor înainte de descărcare |
| Intrări / ieșiri digitale | 11 GPIO libere | vezi harta pinilor |
| Intrări analogice | printr-un ADC I2C (ADS1115) |  |
| Ethernet | da - IP101GRI |  |
| Wi-Fi | nu |  |
| CAN (TWAI) | 1 - pe pini liberi | necesită un transceiver extern |
| Modbus RTU (RS-485) | da - pe pini liberi | necesită un transceiver extern |
| Modbus TCP | client și server |  |
| MQTT | da (și TLS) | descoperire în Home Assistant |
| WEBview | da | pagina operatorului în orice browser |
| Afișaj / touch (HMI) | nu | pagina operatorului este WEBview |
| USB | USB-C (Native USB) |  |
| Alimentare | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Ce nu este suportat

- Conectorii pentru display-ul MIPI DSI și camera CSI - această placă rulează fără display în ctrl32 (pagina de operator este WEBview).
- Slotul microSD - ctrl32 ține programul și ecranele în flash-ul plăcii.

## Ghidul

| Pas | Pagină |
|---|---|
| 1 | [Hardware și cablare](hardware.ro.md) - de ce ai nevoie, alimentarea, harta pinilor |
| 2 | [Instalarea runtime-ului](install.ro.md) - editorul, placa, prima încărcare |
| 3 | [Configurare](configure.ro.md) - rețea, I/O, comunicație |
| 4 | [Proiecte exemplu](examples/README.ro.md) - tot ce face placa, gata de deschis |
| - | [Depanare](troubleshooting.ro.md) |

## Fișiere

-

## Pașii următori

- [Documentația ctrl32](https://ctrl32.com/docs/) - editorul, limbajele, fiecare bloc
- [Descarcă editorul](https://ctrl32.com/download/)
- [Toate plăcile testate](../../README.ro.md)
- [Makerfabs MaTouch ESP32-P4 7"](../../makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.ro.md) - ESP32-P4 cu un ecran tactil de 7"

