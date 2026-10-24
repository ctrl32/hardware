---
title: Makerfabs MaTouch ESP32-P4 7"
slug: makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/board-01.jpg
image_alt: Doska Makerfabs MaTouch ESP32-P4 7" s dotykovým displejom 1024x600
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

![Doska Makerfabs MaTouch ESP32-P4 7" s dotykovým displejom 1024x600](img/board-01.jpg)

Makerfabs MaTouch ESP32-P4 7" je kompletný dotykový panel na jednej doske: displej MIPI 1024 x 600 s kapacitným dotykom, dvojjadrový ESP32-P4 s 32 MB PSRAM, Ethernet a Wi-Fi 6 cez ESP32-C6. S ctrl32 je to HMI aj PLC v jednom - obrazovky nakreslené v editore bežia na skle, vedľa nich beží ladder program a tie isté hodnoty sa dostanú do ľubovoľného prehliadača (WEBview), do zariadení Modbus, na CAN a do MQTT.

**Hodí sa na:**

- Operátorský panel na stroji s vlastnou logikou
- Ovládací panel inteligentného domu alebo budovy na stene
- Brána Modbus / CAN s obrazovkou

Stránka dosky v katalógu: [Makerfabs MaTouch ESP32-P4 7"](https://ctrl32.com/hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/)

![Makerfabs MaTouch ESP32-P4 7" - mapa pinov: funkcia každého GPIO v ctrl32](pinout/pinout.png)

## Čo ctrl32 na tejto doske dokáže

<!-- capabilities:start -->
| Vlastnosť | Na tejto doske | Poznámka |
|---|---|---|
| Čip | ESP32-P4 (ESP32-P4NRW32) |  |
| Pamäť | 16 MB flash, 32 MB PSRAM |  |
| Veľkosť programu | 4096 premenných, 512 alarmov, 512 blokov | editor ho overí pred nahratím |
| Digitálne vstupy / výstupy | 12 voľných GPIO | pozri mapu pinov |
| Analógové vstupy | cez I2C prevodník (ADS1115) |  |
| Ethernet | áno - IP101GRI |  |
| Wi-Fi | Wi-Fi 6 (2.4 GHz) |  |
| CAN (TWAI) | 1 | treba externý prevodník |
| Modbus RTU (RS-485) | áno | na voľných pinoch, treba externý prevodník |
| Modbus TCP | klient aj server |  |
| MQTT | áno (aj TLS) | objavenie v Home Assistant |
| WEBview | áno | stránka operátora v každom prehliadači |
| Displej / dotyk (HMI) | 7" 1024x600, GT911 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Napájanie | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Čo nie je podporované

- Kamera (SC2336 na MIPI CSI) - ctrl32 robí strojové videnie len na 64-bitovom Linux runtime.
- Audio kodek, mikrofón a výstup na reproduktor.
- Bluetooth čipu ESP32-C6.
- Slot microSD - ctrl32 drží program aj obrazovky vo flash pamäti dosky.

## Návod

| Krok | Stránka |
|---|---|
| 1 | [Hardvér a zapojenie](hardware.sk.md) - čo treba, napájanie, mapa pinov |
| 2 | [Nahratie runtime](install.sk.md) - editor, doska, prvé nahratie |
| 3 | [Nastavenie](configure.sk.md) - sieť, vstupy a výstupy, komunikácia |
| 4 | [Vzorové projekty](examples/README.sk.md) - všetko, čo doska dokáže, pripravené na otvorenie |
| - | [Riešenie problémov](troubleshooting.sk.md) |

## Súbory

| Súbor | Čo |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | mapa pinov, vektorová (aj [PNG](pinout/pinout.png)) |
| [makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf](schematics/makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf) | MaTouch ESP32-P4 TFT with Touch 7“ V1.2 |
| [makerfabs-matouch-p4-7-display-datasheet.pdf](datasheets/makerfabs-matouch-p4-7-display-datasheet.pdf) | 7" 1024x600 MIPI display AML070JGI50 datasheet |
| [makerfabs-matouch-p4-es8311-datasheet.pdf](datasheets/makerfabs-matouch-p4-es8311-datasheet.pdf) | ES8311 audio codec datasheet |
| [esp32-p4-datasheet.pdf](datasheets/esp32-p4-datasheet.pdf) | ESP32-P4 datasheet (pre-release) |
| [makerfabs-matouch-p4-sc2336-camera-datasheet.pdf](datasheets/makerfabs-matouch-p4-sc2336-camera-datasheet.pdf) | SC2336 2 MP MIPI camera module datasheet |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | odkiaľ sú fotky, schémy a modely |

## Ďalej

- [Dokumentácia ctrl32](https://ctrl32.com/docs/) - editor, jazyky, každý blok
- [Stiahni editor](https://ctrl32.com/download/)
- [Všetky otestované dosky](../../README.sk.md)
- Makerfabs MaTouch Lite ESP32-S3 3.95" - menší súrodenec
- [Ovládací panel inteligentného domu na MaTouch ESP32-P4](https://ctrl32.com/examples/smart-home-control-panel-on-an-esp32-p4-7-touch-display/) - celý príklad na webe

