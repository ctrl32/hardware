---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": hardvér a zapojenie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa pinov
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Hardvér a zapojenie

## Čo treba

- Makerfabs MaTouch Lite ESP32-S3 3,95" (ST7796).
- Dátový kábel USB-C - na nahratie aj napájanie.
- Meno a heslo tvojej 2,4 GHz Wi-Fi.
- PC s [editorom ctrl32](https://ctrl32.com/download/) (Windows).
- Voliteľne pre príklad all-in-one: reléový modul alebo LED na GPIO4, potenciometer (10 k) medzi 3,3 V a GND s bežcom na GPIO5 (konektory JST) a 3,3 V prevodník CAN (napr. SN65HVD230) na GPIO6 / GPIO7.

## Napájanie

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | konektor USB-C | napájanie aj programovanie |
| Li-Po batéria | konektor batérie | 3,7 V |

## Mapa pinov

![Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa pinov](pinout/pinout.png)

| GPIO | Funkcia v ctrl32 | Poznámka |
|---|---|---|
| 0 | BOOT BTN | ⚠ strapping pin |
| 1 | TFT RST |  |
| 2 | SD CMD | ⚠  |
| 4 | voľný I/O | ADC1 |
| 5 | voľný I/O | ADC1 |
| 6 | voľný I/O | ADC1 |
| 7 | voľný I/O | ADC1 |
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

Dva konektory **JST** nesú štyri voľné piny (GPIO4 až GPIO7) - je ich málo,
preto na ne príklad dáva výstup, analógový vstup a CAN; ďalšie I/O idú cez
Modbus TCP alebo čipy na I2C. Displej, radič dotyku a slot microSD zaberajú
zvyšok pinov.

## Bezpečnosť

- Doska nie je určená na bezpečnostné funkcie. Núdzové zastavenie, dverový
  spínač či svetelná závora sa zapájajú v hardvéri, nikdy cez program ani
  cez dotykovú obrazovku.
- Piny GPIO majú 3,3 V. Cievka relé potrebuje budič (reléový modul ho má).

---

[← Prehľad](README.sk.md) | [Prehľad](README.sk.md) | [Nahratie runtime →](install.sk.md)
