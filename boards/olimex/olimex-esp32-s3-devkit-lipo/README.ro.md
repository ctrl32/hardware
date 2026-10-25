---
title: Olimex ESP32-S3-DevKit-Lipo
slug: olimex-esp32-s3-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-s3-devkit-lipo/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-S3-DevKit-Lipo cu cei doi conectori USB-C și conectorii de pini
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Olimex ESP32-S3-DevKit-Lipo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Placa Olimex ESP32-S3-DevKit-Lipo cu cei doi conectori USB-C și conectorii de pini](img/board-01.jpg)

Olimex ESP32-S3-DevKit-Lipo este o placă ESP32-S3 open-source cu 8 MB de flash, 8 MB de PSRAM, Wi-Fi, două porturi USB-C și un încărcător Li-Po. S3 cu PSRAM este cipul de referință al ctrl32: un program ladder cu dimensiunea completă de program, pagina de operator în orice browser (WEBview), Modbus TCP și MQTT cu TLS - totul prin Wi-Fi.

**Potrivit pentru:**

- Un PLC Wi-Fi cu loc de creștere - 512 variabile, TLS către un broker în cloud
- Un controler cu acumulator de rezervă care rulează mai departe la o pană de curent
- Dezvoltarea propriei plăci pe ESP32-S3

Pagina plăcii în catalog: [Olimex ESP32-S3-DevKit-Lipo](https://ctrl32.com/hardware/boards/olimex-esp32-s3-devkit-lipo/)

![Olimex ESP32-S3-DevKit-Lipo - harta pinilor: funcția fiecărui GPIO în ctrl32](pinout/pinout.png)

## Ce poate face ctrl32 pe această placă

<!-- capabilities:start -->
| Funcție | Pe această placă | Note |
|---|---|---|
| Cip | ESP32-S3 (ESP32-S3-WROOM-1-N8R8) |  |
| Memorie | 8 MB flash, 8 MB PSRAM |  |
| Mărimea programului | 512 variabile, 128 alarme, 1024 blocuri | verificat de editor înainte de descărcare |
| Intrări / ieșiri digitale | 21 GPIO libere | vezi harta pinilor |
| Intrări analogice | 9 pe cip (ADC1) | GPIO1, GPIO2, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 |
| Ethernet | nu |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - pe pini liberi | necesită un transceiver extern |
| Modbus RTU (RS-485) | da - pe pini liberi | necesită un transceiver extern |
| Modbus TCP | client și server |  |
| MQTT | da (și TLS) | descoperire în Home Assistant |
| WEBview | da | pagina operatorului în orice browser |
| Afișaj / touch (HMI) | nu | pagina operatorului este WEBview |
| USB | USB-C (CH340X USB-UART, Native USB) |  |
| Alimentare | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ce nu este suportat

- Bluetooth - ESP32-S3 îl are, ctrl32 nu îl folosește.
- Intrările de măsurare a bateriei și a alimentării (GPIO5 / GPIO6) sunt pini liberi în ctrl32, nu un indicator de baterie.

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
- [Olimex ESP32-DevKit-LiPo](../olimex-esp32-devkit-lipo/README.ro.md) - varianta cu ESP32 clasic

