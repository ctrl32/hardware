---
title: 'Olimex ESP32-S3-DevKit-Lipo: hardvér a zapojenie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-S3-DevKit-Lipo - mapa pinov
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Hardvér a zapojenie

## Čo treba

- Olimex ESP32-S3-DevKit-Lipo.
- Dátový kábel USB-C - na nahratie do konektora označeného UART (CH340X).
- Meno a heslo tvojej 2,4 GHz Wi-Fi.
- PC s [editorom ctrl32](https://ctrl32.com/download/) (Windows).
- Voliteľne pre príklad all-in-one: tlačidlo Boot/User (GPIO0) a LED (GPIO38) sú na doske; potenciometer (10 k) medzi 3,3 V a GND s bežcom na GPIO1; 3,3 V prevodník CAN na GPIO10 / GPIO17 a prevodník RS-485 na GPIO18 / GPIO2 / GPIO4 (DE).

## Napájanie

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | ktorýkoľvek konektor USB-C | napájanie aj programovanie |
| Li-Po batéria | konektor batérie | nabíja sa na doske, automatické prepnutie |

## Mapa pinov

![Olimex ESP32-S3-DevKit-Lipo - mapa pinov](pinout/pinout.png)

| GPIO | Funkcia v ctrl32 | Poznámka |
|---|---|---|
| 0 | voľný - tlačidlo dosky | ⚠ strapping pin |
| 1 | voľný I/O | ADC1 |
| 2 | voľný I/O | ADC1 |
| 4 | voľný I/O | ADC1 |
| 5 | free (PWR SENSE line) | ADC1 |
| 6 | free (BAT SENSE line) | ADC1 |
| 7 | voľný I/O | ADC1 |
| 8 | voľný I/O | ADC1 |
| 9 | voľný I/O | ADC1 |
| 10 | free (SPI CS line) | ADC1 |
| 11 | SPI MOSI |  |
| 12 | SPI SCLK |  |
| 13 | SPI MISO |  |
| 14 | voľný I/O |  |
| 15 | voľný I/O |  |
| 16 | voľný I/O |  |
| 17 | free (UART TX line) |  |
| 18 | free (UART RX line) |  |
| 21 | voľný I/O |  |
| 38 | free (LED0 line) |  |
| 39 | voľný I/O |  |
| 40 | voľný I/O |  |
| 41 | voľný I/O |  |
| 42 | voľný I/O |  |
| 47 | I2C SCL |  |
| 48 | I2C SDA |  |

Na lištách sú voľné GPIO; ADC1 (analógové vstupy, ktoré ctrl32 používa) je
na GPIO1 až GPIO10. GPIO0 je tlačidlo Boot/User - v programe vstup, a keď
ho pri zapnutí držíš, čip sa spustí v režime nahrávania. Konektor pUEXT
nesie I2C (GPIO48 / GPIO47) a SPI.

## Bezpečnosť

- Doska nie je určená na bezpečnostné funkcie. Núdzové zastavenie, dverový
  spínač či svetelná závora sa zapájajú v hardvéri, nikdy cez program.
- Piny GPIO majú 3,3 V. Signál 24 V potrebuje optočlen alebo prevodník
  úrovní; cievka relé potrebuje budič (reléový modul ho má).

---

[← Prehľad](README.sk.md) | [Prehľad](README.sk.md) | [Nahratie runtime →](install.sk.md)
