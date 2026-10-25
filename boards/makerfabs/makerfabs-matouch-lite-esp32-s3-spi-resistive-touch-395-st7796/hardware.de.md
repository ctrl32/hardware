---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": Hardware und Verdrahtung'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95" - Pin-Belegung
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Hardware und Verdrahtung

## Was Sie brauchen

- Das Makerfabs MaTouch Lite ESP32-S3 3,95" (ST7796).
- Ein USB-C-Datenkabel - für das Aufspielen und für die Spannungsversorgung.
- Name und Passwort Ihres 2,4-GHz-WLANs.
- Ein PC mit dem [ctrl32-Editor](https://ctrl32.com/download/) (Windows).
- Optional, für das Beispiel all-in-one: ein Relaismodul oder eine LED an GPIO4, ein Potentiometer (10 k) zwischen 3,3 V und GND mit dem Schleifer an GPIO5 (die JST-Steckverbinder) und ein 3,3-V-CAN-Transceiver (z. B. SN65HVD230) an GPIO6 / GPIO7.

## Spannungsversorgung

| Quelle | Wo | Hinweis |
|---|---|---|
| USB 5 V | der USB-C-Anschluss | Spannungsversorgung und Programmierung |
| Li-Po-Akku | der Akkuanschluss | 3,7 V |

## Pin-Belegung

![Makerfabs MaTouch Lite ESP32-S3 3.95" - Pin-Belegung](pinout/pinout.png)

| GPIO | Funktion in ctrl32 | Hinweis |
|---|---|---|
| 0 | BOOT BTN | ⚠ Strapping-Pin |
| 1 | TFT RST |  |
| 2 | SD CMD | ⚠  |
| 4 | frei - E/A | ADC1 |
| 5 | frei - E/A | ADC1 |
| 6 | frei - E/A | ADC1 |
| 7 | frei - E/A | ADC1 |
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

Die zwei **JST**-Steckverbinder führen die vier freien Pins (GPIO4 bis
GPIO7) - wenige, deshalb legt das Beispiel den Ausgang, den Analogeingang
und CAN darauf; weitere I/O gehen über Modbus TCP oder I2C-Chips. Das
Display, der Touch-Controller und der microSD-Steckplatz belegen die
übrigen Pins.

## Sicherheit

- Das Board ist nicht für Sicherheitsfunktionen bestimmt. Ein Not-Halt,
  ein Türschalter oder ein Lichtvorhang wird in Hardware verdrahtet, nie
  über ein Programm oder einen Touchscreen.
- Die GPIO-Pins führen 3,3 V. Eine Relaisspule braucht einen Treiber (ein Relaismodul hat einen).

---

[← Übersicht](README.de.md) | [Übersicht](README.de.md) | [Runtime installieren →](install.de.md)
