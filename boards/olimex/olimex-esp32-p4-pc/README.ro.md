---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-P4-PC cu mufa Ethernet, porturile USB și conectorul HDMI
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Placa Olimex ESP32-P4-PC cu mufa Ethernet, porturile USB și conectorul HDMI](img/board-01.jpg)

Olimex ESP32-P4-PC este un mic calculator pe ESP32-P4 - două nuclee la 400 MHz cu 32 MB de PSRAM - cu Ethernet de 100 Mb, patru porturi USB host, HDMI, audio și un acumulator Li-Po care îl ține în funcțiune la o pană de curent. Cu ctrl32 este un controler cu fir cu cel mai mare program pe care îl rulează un ESP32 - 4096 de variabile - cu pagina de operator în orice browser (WEBview), Modbus TCP, MQTT cu TLS și CAN sau RS-485 pe pinii liberi ai conectorului său.

**Potrivit pentru:**

- Un PLC cu fir care trece peste o pană de curent cu propriul acumulator
- Un gateway cu logică bogată între Modbus TCP, CAN și MQTT
- Un controler într-o carcasă, alimentat prin PoE (cu extensia)

Pagina plăcii în catalog: [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC - harta pinilor: funcția fiecărui GPIO în ctrl32](pinout/pinout.png)

## Ce poate face ctrl32 pe această placă

<!-- capabilities:start -->
| Funcție | Pe această placă | Note |
|---|---|---|
| Cip | ESP32-P4 (ESP32-P4NRW32) |  |
| Memorie | 16 MB flash, 32 MB PSRAM |  |
| Mărimea programului | 4096 variabile, 512 alarme, 1024 blocuri | verificat de editor înainte de descărcare |
| Intrări / ieșiri digitale | 15 GPIO libere | vezi harta pinilor |
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
| Alimentare | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Ce nu este suportat

- Ieșirea HDMI și conectorii MIPI DSI / CSI - această placă rulează fără display în ctrl32 (pagina de operator este WEBview).
- Porturile USB host și ieșirea audio.
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

| Fișier | Ce |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | harta pinilor, vectorial (și ca [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | de unde provin fotografiile, schemele și modelele |

## Pașii următori

- [Documentația ctrl32](https://ctrl32.com/docs/) - editorul, limbajele, fiecare bloc
- [Descarcă editorul](https://ctrl32.com/download/)
- [Toate plăcile testate](../../README.ro.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.ro.md) - același ESP32-P4 pe o placă mai mică

