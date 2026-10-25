---
title: 'Olimex ESP32-S3-DevKit-Lipo: hardver és bekötés'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-S3-DevKit-Lipo - lábkiosztás
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Hardver és bekötés

## Amire szükséged van

- Az Olimex ESP32-S3-DevKit-Lipo.
- Egy USB-C adatkábel - a feltöltéshez az UART feliratú csatlakozón (a CH340X).
- A 2,4 GHz-es Wi-Fi-hálózatod neve és jelszava.
- Egy PC a [ctrl32 szerkesztővel](https://ctrl32.com/download/) (Windows).
- Opcionálisan, az all-in-one példához: a Boot/User gomb (GPIO0) és a LED (GPIO38) a panelen van; egy potenciométer (10 k) a 3,3 V és a GND között, a csúszkája a GPIO1-en; egy 3,3 V-os CAN adó-vevő a GPIO10 / GPIO17 lábon és egy RS-485 adó-vevő a GPIO18 / GPIO2 / GPIO4 (DE) lábon.

## Tápellátás

| Forrás | Hol | Megjegyzés |
|---|---|---|
| USB 5 V | bármelyik USB-C csatlakozó | tápellátás és programozás |
| Li-Po akkumulátor | az akkumulátor-csatlakozó | a panelen töltődik, automatikus átkapcsolás |

## Lábkiosztás

![Olimex ESP32-S3-DevKit-Lipo - lábkiosztás](pinout/pinout.png)

| GPIO | Funkció a ctrl32-ben | Megjegyzés |
|---|---|---|
| 0 | szabad - a panel gombja | ⚠ strapping láb |
| 1 | szabad - I/O | ADC1 |
| 2 | szabad - I/O | ADC1 |
| 4 | szabad - I/O | ADC1 |
| 5 | free (PWR SENSE line) | ADC1 |
| 6 | free (BAT SENSE line) | ADC1 |
| 7 | szabad - I/O | ADC1 |
| 8 | szabad - I/O | ADC1 |
| 9 | szabad - I/O | ADC1 |
| 10 | free (SPI CS line) | ADC1 |
| 11 | SPI MOSI |  |
| 12 | SPI SCLK |  |
| 13 | SPI MISO |  |
| 14 | szabad - I/O |  |
| 15 | szabad - I/O |  |
| 16 | szabad - I/O |  |
| 17 | free (UART TX line) |  |
| 18 | free (UART RX line) |  |
| 21 | szabad - I/O |  |
| 38 | free (LED0 line) |  |
| 39 | szabad - I/O |  |
| 40 | szabad - I/O |  |
| 41 | szabad - I/O |  |
| 42 | szabad - I/O |  |
| 47 | I2C SCL |  |
| 48 | I2C SDA |  |

A tüskesorok viszik a szabad GPIO-kat; az ADC1 (a ctrl32 által használt
analóg bemenetek) a GPIO1-GPIO10 lábakon van. A GPIO0 a Boot/User gomb - a
programban bemenet, bekapcsoláskor nyomva tartva pedig a chip letöltési
módját indítja. A pUEXT csatlakozó I2C-t (GPIO48 / GPIO47) és SPI-t visz.

## Biztonság

- A panel nem biztonsági funkciókra készült. A vészleállítót, az
  ajtókapcsolót vagy a fényfüggönyt hardveresen kell bekötni, soha nem
  programon keresztül.
- A GPIO lábak 3,3 V-osak. Egy 24 V-os jelhez optocsatoló vagy
  szintillesztő kell; egy relétekercshez meghajtó kell (egy relémodulon
  van ilyen).

---

[← Áttekintés](README.hu.md) | [Áttekintés](README.hu.md) | [A runtime telepítése →](install.hu.md)
