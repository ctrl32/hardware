---
title: 'Olimex ESP32-P4-DevKit: Hardware und Verdrahtung'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-DevKit - Pin-Belegung
tags:
- esp32-p4
- ethernet
- olimex
---

# Hardware und Verdrahtung

## Was Sie brauchen

- Das Olimex ESP32-P4-DevKit.
- Ein USB-C-Datenkabel - für das Aufspielen und für die Spannungsversorgung (5 V).
- Ein Ethernet-Kabel und ein freier Port in Ihrem Netzwerk.
- Ein PC mit dem [ctrl32-Editor](https://ctrl32.com/download/) (Windows).
- Optional, für das Beispiel all-in-one: die LED (GPIO2) ist auf dem Board; ein Taster von GPIO20 nach GND; ein 3,3-V-CAN-Transceiver an GPIO5 / GPIO21 und ein RS-485-Transceiver an GPIO22 / GPIO23 / GPIO32 (DE).

## Spannungsversorgung

| Quelle | Wo | Hinweis |
|---|---|---|
| USB 5 V | der USB-C-Anschluss | Spannungsversorgung, Programmierung und Debugging |
| PoE | über die PoE-Erweiterung | optional |

## Pin-Belegung

![Olimex ESP32-P4-DevKit - Pin-Belegung](pinout/pinout.png)

| GPIO | Funktion in ctrl32 | Hinweis |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 7 | I2C SDA |  |
| 8 | I2C SCL |  |
| 20 | frei - E/A |  |
| 21 | frei - E/A |  |
| 22 | frei - E/A |  |
| 23 | frei - E/A |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 29 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 30 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 31 | Ethernet MDC (IP101GRI) | ⚠ vom Board belegt |
| 32 | frei - E/A |  |
| 33 | frei - E/A |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 35 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 46 | frei - E/A |  |
| 47 | frei - E/A |  |
| 48 | frei - E/A |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 50 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ vom Board belegt |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ vom Board belegt |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Alle GPIO liegen auf den zwei 20-poligen Stiftleisten. Der ESP32-P4 hat
keinen Analogeingang, den ctrl32 nutzt: Analogsignale gehen über einen
I2C-ADC (ein ADS1115 am pUEXT-Steckverbinder, I2C GPIO7 / GPIO8) oder über
ein Modbus-Modul.

## Sicherheit

- Das Board ist nicht für Sicherheitsfunktionen bestimmt. Ein Not-Halt,
  ein Türschalter oder ein Lichtvorhang wird in Hardware verdrahtet, nie
  über ein Programm.
- Die GPIO-Pins führen 3,3 V. Ein 24-V-Signal braucht einen Optokoppler
  oder einen Pegelwandler; eine Relaisspule braucht einen Treiber (ein
  Relaismodul hat ihn).

---

[← Übersicht](README.de.md) | [Übersicht](README.de.md) | [Runtime installieren →](install.de.md)
