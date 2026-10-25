---
title: 'Olimex ESP32-DevKit-LiPo: hardware a zapojení'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-DevKit-LiPo - mapa pinů
tags:
- esp32
- wifi
- battery
- olimex
---

# Hardware a zapojení

## Co je potřeba

- Olimex ESP32-DevKit-LiPo.
- Datový kabel micro-USB - na nahrání i napájení (5 V).
- Jméno a heslo tvé Wi-Fi 2,4 GHz.
- PC s [editorem ctrl32](https://ctrl32.com/download/) (Windows).
- Volitelně pro příklad all-in-one: tlačítko z GPIO13 na GND; reléový modul nebo LED s rezistorem na GPIO4; potenciometr (10 k) mezi 3,3 V a GND s jezdcem na GPIO32; 3,3 V převodník CAN na GPIO14 / GPIO34 a převodník RS-485 na GPIO16 / GPIO36 / GPIO17 (DE); článek Li-Po jako záloha.

## Napájení

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | konektor micro-USB | napájení a programování |
| Li-Po baterie | konektor baterie | nabíjí se na desce, převezme napájení při výpadku USB |

## Mapa pinů

![Olimex ESP32-DevKit-LiPo - mapa pinů](pinout/pinout.png)

| GPIO | Funkce v ctrl32 | Poznámka |
|---|---|---|
| 4 | volný I/O |  |
| 6 | SPI flash modulu | ⚠ používá deska |
| 7 | SPI flash modulu | ⚠ používá deska |
| 8 | SPI flash modulu | ⚠ používá deska |
| 9 | SPI flash modulu | ⚠ používá deska |
| 10 | SPI flash modulu | ⚠ používá deska |
| 11 | SPI flash modulu | ⚠ používá deska |
| 13 | volný I/O |  |
| 14 | volný I/O |  |
| 16 | volný I/O |  |
| 17 | volný I/O |  |
| 18 | volný I/O |  |
| 19 | volný I/O |  |
| 21 | volný I/O |  |
| 22 | volný I/O |  |
| 23 | volný I/O |  |
| 25 | volný I/O |  |
| 26 | volný I/O |  |
| 27 | volný I/O |  |
| 32 | volný I/O | ADC1 |
| 33 | volný I/O | ADC1 |
| 34 | volný vstup | ⚠ jen vstup, ADC1 |
| 35 | free (BAT SENSE line) | ⚠ jen vstup, ADC1 |
| 36 | volný vstup | ⚠ jen vstup, ADC1 |
| 39 | free (PWR SENSE line) | ⚠ jen vstup, ADC1 |

Obě lišty nesou volné GPIO modulu. GPIO34 až GPIO39 jsou pouze vstupy;
GPIO0, 2, 12 a 15 jsou strapping piny - nech je na vstupy nebo je před
použitím vyzkoušej. Tlačítko proti GND nepotřebuje rezistor: ctrl32 ho čte
invertovaně s pull-upem čipu.

## Bezpečnost

- Deska není určena pro bezpečnostní funkce. Nouzové zastavení, dveřní
  spínač nebo světelná závora se zapojují v hardwaru, nikdy přes program.
- Piny GPIO mají 3,3 V. Signál 24 V potřebuje optočlen nebo převodník
  úrovní; cívka relé potřebuje budič (reléový modul ho má).

---

[← Přehled](README.cs.md) | [Přehled](README.cs.md) | [Nahrání runtime →](install.cs.md)
