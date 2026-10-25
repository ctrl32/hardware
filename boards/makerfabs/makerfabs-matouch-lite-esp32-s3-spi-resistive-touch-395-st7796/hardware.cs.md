---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": hardware a zapojení'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa pinů
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Hardware a zapojení

## Co je potřeba

- Makerfabs MaTouch Lite ESP32-S3 3,95" (ST7796).
- Datový kabel USB-C - pro nahrání i napájení.
- Jméno a heslo tvé 2,4 GHz Wi-Fi.
- PC s [editorem ctrl32](https://ctrl32.com/download/) (Windows).
- Volitelně pro příklad all-in-one: reléový modul nebo LED na GPIO4, potenciometr (10 k) mezi 3,3 V a GND s jezdcem na GPIO5 (konektory JST) a 3,3 V převodník CAN (např. SN65HVD230) na GPIO6 / GPIO7.

## Napájení

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | konektor USB-C | napájení i programování |
| Li-Po baterie | konektor baterie | 3,7 V |

## Mapa pinů

![Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa pinů](pinout/pinout.png)

| GPIO | Funkce v ctrl32 | Poznámka |
|---|---|---|
| 0 | BOOT BTN | ⚠ strapping pin |
| 1 | TFT RST |  |
| 2 | SD CMD | ⚠  |
| 4 | volný I/O | ADC1 |
| 5 | volný I/O | ADC1 |
| 6 | volný I/O | ADC1 |
| 7 | volný I/O | ADC1 |
| 13 | TFT MOSI |  |
| 14 | TFT SCLK |  |
| 15 | TFT CS |  |
| 21 | TFT DC |  |
| 38 | TOUCH SDA |  |
| 39 | TOUCH SCL |  |
| 40 | TOUCH INT |  |
| 41 | SD DO | ⚠  |
| 42 | SD SCLK | ⚠  |
| 48 | TFT BL |  |

Dva konektory **JST** nesou čtyři volné piny (GPIO4 až GPIO7) - je jich málo,
proto na ně příklad dává výstup, analogový vstup a CAN; další I/O jdou přes
Modbus TCP nebo čipy na I2C. Displej, řadič dotyku a slot microSD zabírají
zbytek pinů.

## Bezpečnost

- Deska není určena pro bezpečnostní funkce. Nouzové zastavení, dveřní
  spínač nebo světelná závora se zapojují v hardwaru, nikdy přes program
  ani přes dotykovou obrazovku.
- Piny GPIO mají 3,3 V. Cívka relé potřebuje budič (reléový modul ho má).

---

[← Přehled](README.cs.md) | [Přehled](README.cs.md) | [Nahrání runtime →](install.cs.md)
