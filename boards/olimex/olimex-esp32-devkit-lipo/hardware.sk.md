---
title: 'Olimex ESP32-DevKit-LiPo: hardvér a zapojenie'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-DevKit-LiPo - mapa pinov
tags:
- esp32
- wifi
- battery
- olimex
---

# Hardvér a zapojenie

## Čo treba

- Olimex ESP32-DevKit-LiPo.
- Dátový kábel micro-USB - na nahratie aj napájanie (5 V).
- Meno a heslo tvojej Wi-Fi 2,4 GHz.
- PC s [editorom ctrl32](https://ctrl32.com/download/) (Windows).
- Voliteľne pre príklad all-in-one: tlačidlo z GPIO13 na GND; reléový modul alebo LED s rezistorom na GPIO4; potenciometer (10 k) medzi 3,3 V a GND s bežcom na GPIO32; 3,3 V prevodník CAN na GPIO14 / GPIO34 a prevodník RS-485 na GPIO16 / GPIO36 / GPIO17 (DE); článok Li-Po na zálohu.

## Napájanie

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | konektor micro-USB | napájanie a programovanie |
| Li-Po batéria | konektor batérie | nabíja sa na doske, prevezme napájanie pri výpadku USB |

## Mapa pinov

![Olimex ESP32-DevKit-LiPo - mapa pinov](pinout/pinout.png)

| GPIO | Funkcia v ctrl32 | Poznámka |
|---|---|---|
| 4 | voľný I/O |  |
| 6 | SPI flash modulu | ⚠ používa doska |
| 7 | SPI flash modulu | ⚠ používa doska |
| 8 | SPI flash modulu | ⚠ používa doska |
| 9 | SPI flash modulu | ⚠ používa doska |
| 10 | SPI flash modulu | ⚠ používa doska |
| 11 | SPI flash modulu | ⚠ používa doska |
| 13 | voľný I/O |  |
| 14 | voľný I/O |  |
| 16 | voľný I/O |  |
| 17 | voľný I/O |  |
| 18 | voľný I/O |  |
| 19 | voľný I/O |  |
| 21 | voľný I/O |  |
| 22 | voľný I/O |  |
| 23 | voľný I/O |  |
| 25 | voľný I/O |  |
| 26 | voľný I/O |  |
| 27 | voľný I/O |  |
| 32 | voľný I/O | ADC1 |
| 33 | voľný I/O | ADC1 |
| 34 | voľný vstup | ⚠ len vstup, ADC1 |
| 35 | free (BAT SENSE line) | ⚠ len vstup, ADC1 |
| 36 | voľný vstup | ⚠ len vstup, ADC1 |
| 39 | free (PWR SENSE line) | ⚠ len vstup, ADC1 |

Dve lišty nesú voľné GPIO modulu. GPIO34 až GPIO39 sú len vstupy; GPIO0,
2, 12 a 15 sú strapping piny - nechaj ich na vstupy alebo ich pred použitím
vyskúšaj. Tlačidlo na GND nepotrebuje rezistor: ctrl32 ho číta invertované
s pull-upom čipu.

## Bezpečnosť

- Doska nie je určená na bezpečnostné funkcie. Núdzové zastavenie, dverový
  spínač či svetelná závora sa zapájajú v hardvéri, nikdy cez program.
- Piny GPIO majú 3,3 V. Signál 24 V potrebuje optočlen alebo prevodník
  úrovní; cievka relé potrebuje budič (reléový modul ho má).

---

[← Prehľad](README.sk.md) | [Prehľad](README.sk.md) | [Nahratie runtime →](install.sk.md)
