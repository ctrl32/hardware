---
title: Olimex ESP32-POE2
slug: olimex-esp32-poe2
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe2/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-POE2 cu mufa Ethernet și ieșirile de alimentare
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Olimex ESP32-POE2

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Placa Olimex ESP32-POE2 cu mufa Ethernet și ieșirile de alimentare](img/board-01.jpg)

Olimex ESP32-POE2 este generația următoare a lui ESP32-PoE: un ESP32 cu 8 MB de PSRAM, Ethernet și Power over Ethernet IEEE 802.3at care alimentează și dispozitivele tale din teren - ieșiri de 24 V sau 12 V, 5 V și 3,3 V, până la 25 W din cablul de rețea. Cu ctrl32 este un PLC într-un dulap alimentat printr-un singur cablu: logică ladder, WEBview, Modbus TCP și MQTT, cu dimensiunea completă de program a unui ESP32 clasic cu PSRAM.

**Potrivit pentru:**

- Un PLC de dulap care își alimentează senzorii și un mic modul de relee din PoE
- Un gateway Modbus TCP cu MQTT către Home Assistant
- Automatizarea clădirilor cu un singur cablu pe cameră

Pagina plăcii în catalog: [Olimex ESP32-POE2](https://ctrl32.com/hardware/boards/olimex-esp32-poe2/)

![Olimex ESP32-POE2 - harta pinilor: funcția fiecărui GPIO în ctrl32](pinout/pinout.png)

## Ce poate face ctrl32 pe această placă

<!-- capabilities:start -->
| Funcție | Pe această placă | Note |
|---|---|---|
| Cip | ESP32 (ESP32-WROVER-E-N4R8) |  |
| Memorie | 4 MB flash, 8 MB PSRAM |  |
| Mărimea programului | 512 variabile, 128 alarme, 1024 blocuri | verificat de editor înainte de descărcare |
| Intrări / ieșiri digitale | 5 GPIO libere | 3 dintre ele doar intrări |
| Intrări analogice | 3 pe cip (ADC1) | GPIO34, GPIO36, GPIO39 |
| Ethernet | da - LAN8710A |  |
| Power over Ethernet | IEEE 802.3at |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - pe pini liberi | necesită un transceiver extern |
| Modbus RTU (RS-485) | da - pe pini liberi | necesită un transceiver extern |
| Modbus TCP | client și server |  |
| MQTT | da | descoperire în Home Assistant |
| WEBview | da | pagina operatorului în orice browser |
| Afișaj / touch (HMI) | nu | pagina operatorului este WEBview |
| USB | USB-C |  |
| Alimentare | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Ce nu este suportat

- Bluetooth - ESP32 îl are, ctrl32 nu îl folosește.
- Slotul microSD - ctrl32 ține programul și ecranele în flash-ul propriu al cipului.
- Intrarea de acumulator funcționează ca funcție proprie a plăcii; ctrl32 nu citește nivelul acumulatorului.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.ro.md) - prima generație
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.ro.md) - cu alimentare PoE izolată

