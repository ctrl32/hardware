---
title: 'Olimex ESP32-S3-DevKit-Lipo: Hardware und Verdrahtung'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-S3-DevKit-Lipo - Pin-Belegung
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Hardware und Verdrahtung

## Was Sie brauchen

- Das Olimex ESP32-S3-DevKit-Lipo.
- Ein USB-C-Datenkabel - am Anschluss mit der Beschriftung UART (der CH340X) für das Aufspielen.
- Name und Passwort Ihres 2,4-GHz-WLANs.
- Ein PC mit dem [ctrl32-Editor](https://ctrl32.com/download/) (Windows).
- Optional, für das Beispiel all-in-one: der Taster Boot/User (GPIO0) und die LED (GPIO38) sind auf dem Board; ein Potentiometer (10 k) zwischen 3,3 V und GND mit dem Schleifer an GPIO1; ein 3,3-V-CAN-Transceiver an GPIO10 / GPIO17 und ein RS-485-Transceiver an GPIO18 / GPIO2 / GPIO4 (DE).

## Spannungsversorgung

| Quelle | Wo | Hinweis |
|---|---|---|
| USB 5 V | einer der beiden USB-C-Anschlüsse | Spannungsversorgung und Programmierung |
| Li-Po-Akku | der Akkuanschluss | wird auf dem Board geladen, automatische Umschaltung |

## Pin-Belegung

![Olimex ESP32-S3-DevKit-Lipo - Pin-Belegung](pinout/pinout.png)

| GPIO | Funktion in ctrl32 | Hinweis |
|---|---|---|
| 0 | frei - der Taster des Boards | ⚠ Strapping-Pin |
| 1 | frei - E/A | ADC1 |
| 2 | frei - E/A | ADC1 |
| 4 | frei - E/A | ADC1 |
| 5 | free (PWR SENSE line) | ADC1 |
| 6 | free (BAT SENSE line) | ADC1 |
| 7 | frei - E/A | ADC1 |
| 8 | frei - E/A | ADC1 |
| 9 | frei - E/A | ADC1 |
| 10 | free (SPI CS line) | ADC1 |
| 11 | SPI MOSI |  |
| 12 | SPI SCLK |  |
| 13 | SPI MISO |  |
| 14 | frei - E/A |  |
| 15 | frei - E/A |  |
| 16 | frei - E/A |  |
| 17 | free (UART TX line) |  |
| 18 | free (UART RX line) |  |
| 21 | frei - E/A |  |
| 38 | free (LED0 line) |  |
| 39 | frei - E/A |  |
| 40 | frei - E/A |  |
| 41 | frei - E/A |  |
| 42 | frei - E/A |  |
| 47 | I2C SCL |  |
| 48 | I2C SDA |  |

Die Stiftleisten führen die freien GPIO; ADC1 (die Analogeingänge, die
ctrl32 nutzt) liegt auf GPIO1 bis GPIO10. GPIO0 ist der Taster Boot/User -
im Programm ein Eingang, und beim Einschalten gehalten startet er den
Download-Modus des Chips. Der pUEXT-Steckverbinder führt I2C (GPIO48 /
GPIO47) und SPI.

## Sicherheit

- Das Board ist nicht für Sicherheitsfunktionen bestimmt. Ein Not-Halt,
  ein Türschalter oder ein Lichtvorhang wird in Hardware verdrahtet, nie
  über ein Programm.
- Die GPIO-Pins führen 3,3 V. Ein 24-V-Signal braucht einen Optokoppler
  oder einen Pegelwandler; eine Relaisspule braucht einen Treiber (ein
  Relaismodul hat ihn).

---

[← Übersicht](README.de.md) | [Übersicht](README.de.md) | [Runtime installieren →](install.de.md)
