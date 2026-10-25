---
title: Makerfabs MaTouch ESP32-P4 7"
slug: makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/board-01.jpg
image_alt: Deska Makerfabs MaTouch ESP32-P4 7" s dotykovým displejem 1024x600
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

![Deska Makerfabs MaTouch ESP32-P4 7" s dotykovým displejem 1024x600](img/board-01.jpg)

Makerfabs MaTouch ESP32-P4 7" je kompletní dotykový panel na jedné desce: displej MIPI 1024 x 600 s kapacitním dotykem, dvoujádrový ESP32-P4 s 32 MB PSRAM, Ethernet a Wi-Fi 6 přes ESP32-C6. S ctrl32 je to HMI a PLC v jednom - obrazovky nakreslené v editoru běží na skle, vedle nich běží ladder program a stejné hodnoty se dostanou do libovolného prohlížeče (WEBview), do zařízení Modbus, na CAN a do MQTT.

**Hodí se na:**

- Operátorský panel na stroji s vlastní logikou
- Ovládací panel chytré domácnosti nebo budovy na zdi
- Brána Modbus / CAN s obrazovkou

Stránka desky v katalogu: [Makerfabs MaTouch ESP32-P4 7"](https://ctrl32.com/hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/)

![Makerfabs MaTouch ESP32-P4 7" - mapa pinů: funkce každého GPIO v ctrl32](pinout/pinout.png)

## Co ctrl32 na této desce umí

<!-- capabilities:start -->
| Vlastnost | Na této desce | Poznámka |
|---|---|---|
| Čip | ESP32-P4 (ESP32-P4NRW32) |  |
| Paměť | 16 MB flash, 32 MB PSRAM |  |
| Velikost programu | 4096 proměnných, 512 alarmů, 512 bloků | editor ji ověří před nahráním |
| Digitální vstupy / výstupy | 12 volných GPIO | viz mapa pinů |
| Analogové vstupy | přes I2C převodník (ADS1115) |  |
| Ethernet | ano - IP101GRI |  |
| Wi-Fi | Wi-Fi 6 (2.4 GHz) |  |
| CAN (TWAI) | 1 | potřebuje externí převodník |
| Modbus RTU (RS-485) | ano | na volných pinech, potřebuje externí převodník |
| Modbus TCP | klient i server |  |
| MQTT | ano (i TLS) | objevení v Home Assistant |
| WEBview | ano | stránka operátora v každém prohlížeči |
| Displej / dotyk (HMI) | 7" 1024x600, GT911 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Napájení | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Co není podporováno

- Kamera (SC2336 na MIPI CSI) - ctrl32 dělá strojové vidění jen na 64bitovém Linux runtime.
- Audiokodek, mikrofon a výstup na reproduktor.
- Bluetooth čipu ESP32-C6.
- Slot microSD - ctrl32 drží program i obrazovky ve flash paměti desky.

## Návod

| Krok | Stránka |
|---|---|
| 1 | [Hardware a zapojení](hardware.cs.md) - co je potřeba, napájení, mapa pinů |
| 2 | [Nahrání runtime](install.cs.md) - editor, deska, první nahrání |
| 3 | [Nastavení](configure.cs.md) - síť, vstupy a výstupy, komunikace |
| 4 | [Vzorové projekty](examples/README.cs.md) - všechno, co deska umí, připravené k otevření |
| - | [Řešení problémů](troubleshooting.cs.md) |

## Soubory

| Soubor | Co |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | mapa pinů, vektorová (i [PNG](pinout/pinout.png)) |
| [makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf](schematics/makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf) | MaTouch ESP32-P4 TFT with Touch 7“ V1.2 |
| [makerfabs-matouch-p4-7-display-datasheet.pdf](datasheets/makerfabs-matouch-p4-7-display-datasheet.pdf) | 7" 1024x600 MIPI display AML070JGI50 datasheet |
| [makerfabs-matouch-p4-es8311-datasheet.pdf](datasheets/makerfabs-matouch-p4-es8311-datasheet.pdf) | ES8311 audio codec datasheet |
| [esp32-p4-datasheet.pdf](datasheets/esp32-p4-datasheet.pdf) | ESP32-P4 datasheet (pre-release) |
| [makerfabs-matouch-p4-sc2336-camera-datasheet.pdf](datasheets/makerfabs-matouch-p4-sc2336-camera-datasheet.pdf) | SC2336 2 MP MIPI camera module datasheet |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | odkud jsou fotky, schémata a modely |

## Dále

- [Dokumentace ctrl32](https://ctrl32.com/docs/) - editor, jazyky, každý blok
- [Stáhni editor](https://ctrl32.com/download/)
- Všechny otestované desky
- Makerfabs MaTouch Lite ESP32-S3 3.95" - menší sourozenec
- [Ovládací panel chytré domácnosti na MaTouch ESP32-P4](https://ctrl32.com/examples/smart-home-control-panel-on-an-esp32-p4-7-touch-display/) - celý příklad na webu

