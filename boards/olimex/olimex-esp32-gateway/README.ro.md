---
title: Olimex ESP32-GATEWAY
slug: olimex-esp32-gateway
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-gateway/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-GATEWAY cu mufa Ethernet și conectorul USB-C
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Olimex ESP32-GATEWAY

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Placa Olimex ESP32-GATEWAY cu mufa Ethernet și conectorul USB-C](img/board-01.jpg)

Olimex ESP32-GATEWAY este o placă ESP32 compactă cu Ethernet de 100 Mb și Wi-Fi - destul de mică pentru o doză de joncțiune. Cu ctrl32 este un gateway cu logică proprie: dispozitive Modbus TCP citite și publicate prin MQTT, un program ladder pe cip și pagina sa de operator în orice browser (WEBview).

**Potrivit pentru:**

- Un gateway de la Modbus TCP la MQTT cu logică proprie
- Un mic controler într-o doză de joncțiune, pe Ethernet
- Automatizarea casei - citirea contoarelor, comutare prin module I/O Modbus

Pagina plăcii în catalog: [Olimex ESP32-GATEWAY](https://ctrl32.com/hardware/boards/olimex-esp32-gateway/)

![Olimex ESP32-GATEWAY - harta pinilor: funcția fiecărui GPIO în ctrl32](pinout/pinout.png)

## Ce poate face ctrl32 pe această placă

<!-- capabilities:start -->
| Funcție | Pe această placă | Note |
|---|---|---|
| Cip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memorie | 4 MB flash |  |
| Mărimea programului | 128 variabile, 32 alarme, 128 blocuri | verificat de editor înainte de descărcare |
| Intrări / ieșiri digitale | 3 GPIO libere | 1 dintre ele doar intrări |
| Intrări analogice | 2 pe cip (ADC1) | GPIO33, GPIO34 |
| Ethernet | da - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - pe pini liberi | necesită un transceiver extern |
| Modbus RTU (RS-485) | da - pe pini liberi | necesită un transceiver extern |
| Modbus TCP | client și server |  |
| MQTT | da | descoperire în Home Assistant |
| WEBview | da | pagina operatorului în orice browser |
| Afișaj / touch (HMI) | nu | pagina operatorului este WEBview |
| USB | USB-C (CH340 USB-UART) |  |
| Alimentare | 5 V USB |  |
<!-- capabilities:end -->

### Ce nu este suportat

- Bluetooth - ESP32 îl are, ctrl32 nu îl folosește.
- Slotul microSD - ctrl32 ține programul și ecranele în flash-ul propriu al cipului.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.ro.md) - Ethernet și Power over Ethernet

