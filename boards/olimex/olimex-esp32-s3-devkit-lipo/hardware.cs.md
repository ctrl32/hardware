---
title: 'Olimex ESP32-S3-DevKit-Lipo: hardware a zapojení'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-S3-DevKit-Lipo - mapa pinů
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Hardware a zapojení

## Co je potřeba

- Olimex ESP32-S3-DevKit-Lipo.
- Datový kabel USB-C - pro nahrání do konektoru označeného UART (CH340X).
- Jméno a heslo tvé 2,4 GHz Wi-Fi.
- PC s [editorem ctrl32](https://ctrl32.com/download/) (Windows).
- Volitelně pro příklad all-in-one: tlačítko Boot/User (GPIO0) a LED (GPIO38) jsou na desce; potenciometr (10 k) mezi 3,3 V a GND s jezdcem na GPIO1; 3,3 V převodník CAN na GPIO10 / GPIO17 a převodník RS-485 na GPIO18 / GPIO2 / GPIO4 (DE).

## Napájení

| Zdroj | Kde | Poznámka |
|---|---|---|
| USB 5 V | kterýkoli konektor USB-C | napájení i programování |
| Li-Po baterie | konektor baterie | nabíjí se na desce, automatické přepnutí |

## Mapa pinů

![Olimex ESP32-S3-DevKit-Lipo - mapa pinů](pinout/pinout.png)

| GPIO | Funkce v ctrl32 | Poznámka |
|---|---|---|
| 0 | volný - tlačítko desky | ⚠ strapping pin |
| 1 | volný I/O | ADC1 |
| 2 | volný I/O | ADC1 |
| 4 | volný I/O | ADC1 |
| 5 | free (PWR SENSE line) | ADC1 |
| 6 | free (BAT SENSE line) | ADC1 |
| 7 | volný I/O | ADC1 |
| 8 | volný I/O | ADC1 |
| 9 | volný I/O | ADC1 |
| 10 | free (SPI CS line) | ADC1 |
| 11 | SPI MOSI |  |
| 12 | SPI SCLK |  |
| 13 | SPI MISO |  |
| 14 | volný I/O |  |
| 15 | volný I/O |  |
| 16 | volný I/O |  |
| 17 | free (UART TX line) |  |
| 18 | free (UART RX line) |  |
| 21 | volný I/O |  |
| 38 | free (LED0 line) |  |
| 39 | volný I/O |  |
| 40 | volný I/O |  |
| 41 | volný I/O |  |
| 42 | volný I/O |  |
| 47 | I2C SCL |  |
| 48 | I2C SDA |  |

Na lištách jsou volné GPIO; ADC1 (analogové vstupy, které ctrl32 používá) je
na GPIO1 až GPIO10. GPIO0 je tlačítko Boot/User - v programu vstup, a když
ho držíš při zapnutí, čip naběhne v režimu nahrávání. Konektor pUEXT nese
I2C (GPIO48 / GPIO47) a SPI.

## Bezpečnost

- Deska není určena pro bezpečnostní funkce. Nouzové zastavení, dveřní
  spínač nebo světelná závora se zapojují v hardwaru, nikdy přes program.
- Piny GPIO mají 3,3 V. Signál 24 V potřebuje optočlen nebo převodník
  úrovní; cívka relé potřebuje budič (reléový modul ho má).

---

[← Přehled](README.cs.md) | [Přehled](README.cs.md) | [Nahrání runtime →](install.cs.md)
