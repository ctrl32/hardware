---
title: 'Olimex ESP32-P4-PC: Hardware und Verdrahtung'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-PC - Pin-Belegung
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Hardware und Verdrahtung

## Was Sie brauchen

- Der Olimex ESP32-P4-PC.
- Ein USB-C-Datenkabel - für das Aufspielen und für die Spannungsversorgung (5 V).
- Ein Ethernet-Kabel und ein freier Port in Ihrem Netzwerk.
- Ein PC mit dem [ctrl32-Editor](https://ctrl32.com/download/) (Windows).
- Optional: eine Li-Po-Zelle als Akkupufferung; für das Beispiel all-in-one ist die Benutzer-LED (GPIO2) auf dem Board, und ein Taster geht von GPIO14 nach GND (EXT1); ein 3,3-V-CAN-Transceiver an GPIO5 / GPIO15 und ein RS-485-Transceiver an GPIO16 / GPIO17 / GPIO18 (DE).

## Spannungsversorgung

| Quelle | Wo | Hinweis |
|---|---|---|
| USB 5 V | der USB-C-Anschluss | Spannungsversorgung, Programmierung und Debugging |
| Li-Po-Akku | der Akkuanschluss | wird auf dem Board geladen; übernimmt beim Ausfall der Versorgung (USV) |
| PoE | über die PoE-Erweiterung | optional |

## Pin-Belegung

![Olimex ESP32-P4-PC - Pin-Belegung](pinout/pinout.png)

| GPIO | Funktion in ctrl32 | Hinweis |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 14 | frei - E/A |  |
| 15 | frei - E/A |  |
| 16 | frei - E/A |  |
| 17 | frei - E/A |  |
| 18 | frei - E/A |  |
| 19 | frei - E/A |  |
| 20 | frei - E/A |  |
| 21 | USB HUB RST | ⚠  |
| 22 | I2C SDA |  |
| 23 | I2C SCL |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 29 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 30 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 31 | Ethernet MDC (IP101GRI) | ⚠ vom Board belegt |
| 32 | frei - E/A |  |
| 33 | frei - E/A |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 35 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 36 | frei - E/A | ⚠ Strapping-Pin |
| 46 | frei - E/A |  |
| 47 | frei - E/A |  |
| 48 | frei - E/A |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 50 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ vom Board belegt |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ vom Board belegt |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Die freien Pins liegen auf der 20-poligen Stiftleiste **EXT1**: GPIO14 bis
GPIO20, 32, 33, 36, 46, 47, 48 und die Benutzer-LED an GPIO2. Der
**UEXT**-Steckverbinder führt I2C (GPIO22 / GPIO23 - geteilt mit der
HDMI-Bridge), SPI (GPIO4 / 53 / 54, CS GPIO5) und die Konsolen-UART. Der
ESP32-P4 hat keinen Analogeingang, den ctrl32 nutzt: Analogsignale gehen
über einen I2C-ADC (ein ADS1115 an UEXT) oder über ein Modbus-Modul. CAN
und RS-485 kommen auf freie EXT1-Pins mit einem 3,3-V-Transceiver-Modul.

## Sicherheit

- Das Board ist nicht für Sicherheitsfunktionen bestimmt. Ein Not-Halt,
  ein Türschalter oder ein Lichtvorhang wird in Hardware verdrahtet, nie
  über ein Programm.
- Die GPIO-Pins führen 3,3 V. Ein 24-V-Signal braucht einen Optokoppler
  oder einen Pegelwandler; eine Relaisspule braucht einen Treiber (ein
  Relaismodul hat ihn).

## Fotos

![Olimex ESP32-P4-PC - Foto 1](img/board-01.jpg)
![Olimex ESP32-P4-PC - Foto 2](img/board-02.jpg)
![Olimex ESP32-P4-PC - Foto 3](img/board-03.jpg)
![Olimex ESP32-P4-PC - Foto 4](img/board-04.jpg)

---

[← Übersicht](README.de.md) | [Übersicht](README.de.md) | [Runtime installieren →](install.de.md)
