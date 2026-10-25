---
title: 'Olimex ESP32-GATEWAY: Hardware und Verdrahtung'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY - Pin-Belegung
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Hardware und Verdrahtung

## Was Sie brauchen

- Das Olimex ESP32-GATEWAY.
- Ein USB-C-Datenkabel - für das Aufspielen und für die Spannungsversorgung (5 V).
- Ein Ethernet-Kabel und ein freier Port in Ihrem Netzwerk.
- Ein PC mit dem [ctrl32-Editor](https://ctrl32.com/download/) (Windows).
- Das Beispiel all-in-one nutzt den eigenen Taster (GPIO34) und die LED (GPIO33) des Boards - sonst ist nichts zu verdrahten.

## Spannungsversorgung

| Quelle | Wo | Hinweis |
|---|---|---|
| USB 5 V | der USB-C-Anschluss | Spannungsversorgung und Programmierung |

## Pin-Belegung

![Olimex ESP32-GATEWAY - Pin-Belegung](pinout/pinout.png)

| GPIO | Funktion in ctrl32 | Hinweis |
|---|---|---|
| 2 | SPI MOSI | ⚠ Strapping-Pin |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ vom Board belegt |
| 6 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 7 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 8 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 9 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 10 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 11 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 13 | free (SPI CS line) |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ Strapping-Pin |
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ vom Board belegt |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ vom Board belegt |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ vom Board belegt |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ vom Board belegt |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ vom Board belegt |
| 23 | Ethernet MDC (LAN8710A) | ⚠ vom Board belegt |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ vom Board belegt |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ vom Board belegt |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ vom Board belegt |
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | frei - der Taster des Boards | ⚠ nur Eingang, ADC1 |

Die 20-polige **EXT**-Stiftleiste führt die freien Pins und die I2C- /
SPI-Leitungen. Die LED des Boards liegt an GPIO33, sein Taster an GPIO34
(ein reiner Eingang). Nur wenige Pins bleiben frei: weitere I/O laufen über
Modbus TCP oder I2C-Chips.

## Sicherheit

- Das Board ist nicht für Sicherheitsfunktionen bestimmt. Ein Not-Halt,
  ein Türschalter oder ein Lichtvorhang wird in Hardware verdrahtet, nie
  über ein Programm.
- Die GPIO-Pins führen 3,3 V. Ein 24-V-Signal braucht einen Optokoppler
  oder einen Pegelwandler; eine Relaisspule braucht einen Treiber (ein
  Relaismodul hat ihn).

---

[← Übersicht](README.de.md) | [Übersicht](README.de.md) | [Runtime installieren →](install.de.md)
