---
title: Makerfabs MaTouch ESP32-P4 7"
slug: makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/board-01.jpg
image_alt: Placa Makerfabs MaTouch ESP32-P4 de 7 inch cu display-ul tactil de 1024x600
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Makerfabs MaTouch ESP32-P4 7"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 1024x600](https://img.shields.io/badge/HMI-1024x600-0891b2)

![Placa Makerfabs MaTouch ESP32-P4 de 7 inch cu display-ul tactil de 1024x600](img/board-01.jpg)

Makerfabs MaTouch ESP32-P4 7" este un panou tactil complet pe o singură placă: un display MIPI de 1024 x 600 cu touch capacitiv, ESP32-P4 cu două nuclee și 32 MB de PSRAM, Ethernet și Wi-Fi 6 printr-un ESP32-C6. Cu ctrl32 este HMI și PLC într-unul - ecranele desenate în editor rulează pe sticlă, alături rulează un program ladder, iar aceleași valori ajung în orice browser (WEBview), la dispozitive Modbus, pe CAN și MQTT.

**Potrivit pentru:**

- Un panou de operator pe o mașină, cu logică proprie
- Un panou de comandă pentru casă inteligentă sau clădire, pe perete
- Un gateway Modbus / CAN cu ecran

Pagina plăcii în catalog: [Makerfabs MaTouch ESP32-P4 7"](https://ctrl32.com/hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/)

![Makerfabs MaTouch ESP32-P4 7" - harta pinilor: funcția fiecărui GPIO în ctrl32](pinout/pinout.png)

## Ce poate face ctrl32 pe această placă

<!-- capabilities:start -->
| Funcție | Pe această placă | Note |
|---|---|---|
| Cip | ESP32-P4 (ESP32-P4NRW32) |  |
| Memorie | 16 MB flash, 32 MB PSRAM |  |
| Mărimea programului | 4096 variabile, 512 alarme, 512 blocuri | verificat de editor înainte de descărcare |
| Intrări / ieșiri digitale | 12 GPIO libere | vezi harta pinilor |
| Intrări analogice | printr-un ADC I2C (ADS1115) |  |
| Ethernet | da - IP101GRI |  |
| Wi-Fi | Wi-Fi 6 (2.4 GHz) |  |
| CAN (TWAI) | 1 | necesită un transceiver extern |
| Modbus RTU (RS-485) | da | pe pini liberi, necesită un transceiver extern |
| Modbus TCP | client și server |  |
| MQTT | da (și TLS) | descoperire în Home Assistant |
| WEBview | da | pagina operatorului în orice browser |
| Afișaj / touch (HMI) | 7" 1024x600, GT911 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Alimentare | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ce nu este suportat

- Camera (SC2336 pe MIPI CSI) - ctrl32 rulează vision doar pe runtime-ul Linux pe 64 de biți.
- Codecul audio, microfonul și ieșirea de difuzor.
- Bluetooth-ul lui ESP32-C6.
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
| [makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf](schematics/makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf) | MaTouch ESP32-P4 TFT with Touch 7“ V1.2 |
| [makerfabs-matouch-p4-7-display-datasheet.pdf](datasheets/makerfabs-matouch-p4-7-display-datasheet.pdf) | 7" 1024x600 MIPI display AML070JGI50 datasheet |
| [makerfabs-matouch-p4-es8311-datasheet.pdf](datasheets/makerfabs-matouch-p4-es8311-datasheet.pdf) | ES8311 audio codec datasheet |
| [esp32-p4-datasheet.pdf](datasheets/esp32-p4-datasheet.pdf) | ESP32-P4 datasheet (pre-release) |
| [makerfabs-matouch-p4-sc2336-camera-datasheet.pdf](datasheets/makerfabs-matouch-p4-sc2336-camera-datasheet.pdf) | SC2336 2 MP MIPI camera module datasheet |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | de unde provin fotografiile, schemele și modelele |

## Pașii următori

- [Documentația ctrl32](https://ctrl32.com/docs/) - editorul, limbajele, fiecare bloc
- [Descarcă editorul](https://ctrl32.com/download/)
- Toate plăcile testate
- Makerfabs MaTouch Lite ESP32-S3 3.95" - fratele mai mic
- [Panou de comandă pentru casă inteligentă pe MaTouch ESP32-P4](https://ctrl32.com/examples/smart-home-control-panel-on-an-esp32-p4-7-touch-display/) - un exemplu complet pe web

