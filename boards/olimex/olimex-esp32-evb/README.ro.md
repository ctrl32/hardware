---
title: Olimex ESP32-EVB
slug: olimex-esp32-evb
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-evb/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-EVB cu cele două relee, mufa Ethernet și clema CAN
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Olimex ESP32-EVB

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 240x320](https://img.shields.io/badge/HMI-240x320-0891b2)

![Placa Olimex ESP32-EVB cu cele două relee, mufa Ethernet și clema CAN](img/board-01.jpg)

Olimex ESP32-EVB este o placă ESP32 construită pentru comandă: două relee (10 A / 250 VAC), un transceiver CAN, Ethernet și Wi-Fi pe o singură placă. Cu ctrl32 este un PLC gata făcut - releele și butonul sunt variabile ale unui program ladder, CAN comunică cu acționări și noduri I/O, iar pagina de operator rulează în orice browser (WEBview). Un display tactil opțional de 2,8" pe conectorul UEXT o transformă într-un mic panou.

**Potrivit pentru:**

- Un controler cu relee - încălzire, pompe, lumini - cu Ethernet
- Un master CAN pentru o acționare sau noduri I/O CANopen
- Un termostat sau un mic panou cu display-ul opțional de 2,8"

Pagina plăcii în catalog: [Olimex ESP32-EVB](https://ctrl32.com/hardware/boards/olimex-esp32-evb/)

![Olimex ESP32-EVB - harta pinilor: funcția fiecărui GPIO în ctrl32](pinout/pinout.png)

## Ce poate face ctrl32 pe această placă

<!-- capabilities:start -->
| Funcție | Pe această placă | Note |
|---|---|---|
| Cip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memorie | 4 MB flash |  |
| Mărimea programului | 128 variabile, 32 alarme, 128 blocuri | verificat de editor înainte de descărcare |
| Intrări / ieșiri digitale | 6 GPIO libere | 2 dintre ele doar intrări |
| Intrări analogice | 4 pe cip (ADC1) | GPIO32, GPIO33, GPIO34, GPIO36 |
| Ethernet | da - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 |  |
| Modbus RTU (RS-485) | da - pe pini liberi | necesită un transceiver extern |
| Modbus TCP | client și server |  |
| MQTT | da | descoperire în Home Assistant |
| WEBview | da | pagina operatorului în orice browser |
| Afișaj / touch (HMI) | - 240x320, - |  |
| USB | Micro-USB (CH340T USB-UART) |  |
| Alimentare | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ce nu este suportat

- Bluetooth.
- Receptorul și emițătorul IR - ctrl32 nu le folosește pe această placă.
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

