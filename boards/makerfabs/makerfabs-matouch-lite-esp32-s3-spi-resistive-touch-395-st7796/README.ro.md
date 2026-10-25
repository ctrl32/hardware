---
title: Makerfabs MaTouch Lite ESP32-S3 3.95"
slug: makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/
image: img/board-01.jpg
image_alt: Placa Makerfabs MaTouch Lite ESP32-S3 cu display-ul tactil de 3,95 inch
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Makerfabs MaTouch Lite ESP32-S3 3.95"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 320x480](https://img.shields.io/badge/HMI-320x480-0891b2)

![Placa Makerfabs MaTouch Lite ESP32-S3 cu display-ul tactil de 3,95 inch](img/board-01.jpg)

Makerfabs MaTouch Lite este un panou tactil ieftin: un display de 3,95" cu 320 x 480 și touch rezistiv pe un ESP32-S3 cu PSRAM și Wi-Fi. Cu ctrl32 este HMI și PLC într-unul - ecrane desenate în editor pe sticlă, alături un program ladder, aceleași valori în orice browser (WEBview), Modbus TCP, CAN și MQTT. Touch-ul rezistiv funcționează și cu mănuși.

**Potrivit pentru:**

- Un mic panou de operator pe o mașină, folosit cu mănuși
- Un termostat de perete sau un regulator de cameră
- Un display CAN pentru un vehicul sau o acționare

Pagina plăcii în catalog: [Makerfabs MaTouch Lite ESP32-S3 3.95"](https://ctrl32.com/hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/)

![Makerfabs MaTouch Lite ESP32-S3 3.95" - harta pinilor: funcția fiecărui GPIO în ctrl32](pinout/pinout.png)

## Ce poate face ctrl32 pe această placă

<!-- capabilities:start -->
| Funcție | Pe această placă | Note |
|---|---|---|
| Cip | ESP32-S3 (esp32s3_wroom_1_n16r8) |  |
| Memorie | 16 MB flash, 8 MB PSRAM |  |
| Mărimea programului | 512 variabile, 128 alarme, 512 blocuri | verificat de editor înainte de descărcare |
| Intrări / ieșiri digitale | 4 GPIO libere | vezi harta pinilor |
| Intrări analogice | 4 pe cip (ADC1) | GPIO4, GPIO5, GPIO6, GPIO7 |
| Ethernet | nu |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 | necesită un transceiver extern |
| Modbus RTU (RS-485) | da | pe pini liberi, necesită un transceiver extern |
| Modbus TCP | client și server |  |
| MQTT | da (și TLS) | descoperire în Home Assistant |
| WEBview | da | pagina operatorului în orice browser |
| Afișaj / touch (HMI) | 3.95" 320x480, NS2009 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Alimentare | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ce nu este suportat

- Bluetooth.
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
- [Makerfabs MaTouch ESP32-P4 7"](../makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.ro.md) - fratele mare

