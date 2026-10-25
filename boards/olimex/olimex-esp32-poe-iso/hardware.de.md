---
title: 'Olimex ESP32-PoE-ISO: Hardware und Verdrahtung'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-PoE-ISO - Pin-Belegung
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Hardware und Verdrahtung

## Was Sie brauchen

- Das Olimex ESP32-PoE-ISO (Variante WROOM-32E, ohne PSRAM).
- Ein Micro-USB-Datenkabel - für das erste Aufspielen der Runtime.
- Spannungsversorgung: ein PoE-Switch / Injektor (IEEE 802.3af) oder ein 5-V-USB-Netzteil.
- Ein Ethernet-Kabel und ein freier Port in Ihrem Netzwerk.
- Ein PC mit dem [ctrl32-Editor](https://ctrl32.com/download/) (Windows).
- Optional, für das Beispiel all-in-one: der Taster BUT1 ist auf dem Board; ein Relaismodul oder eine LED mit Vorwiderstand an GPIO4 (UEXT); ein Potentiometer (10 k) zwischen 3,3 V und GND mit dem Schleifer an GPIO33 (EXT2); ein 3,3-V-CAN-Transceiver an GPIO5 (TX) / GPIO36 (RX).

## Spannungsversorgung

| Quelle | Wo | Hinweis |
|---|---|---|
| PoE | die Ethernet-Buchse, aus einem PoE-Switch oder Injektor | IEEE 802.3af, galvanisch getrennt |
| USB 5 V | der Micro-USB-Anschluss | der Weg für das erste Aufspielen |
| Li-Po-Akku | der Akkuanschluss | wird auf dem Board geladen |

Die PoE-Versorgung ist vom Board **galvanisch getrennt**: Anders als
beim einfachen ESP32-PoE dürfen USB zum PC und PoE gleichzeitig
angeschlossen sein - die Runtime lässt sich aufspielen und online
beobachten, während das Board an seinem PoE-Switch bleibt.

## Pin-Belegung

![Olimex ESP32-PoE-ISO - Pin-Belegung](pinout/pinout.png)

| GPIO | Funktion in ctrl32 | Hinweis |
|---|---|---|
| 2 | SPI MOSI | ⚠ Strapping-Pin |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 7 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 8 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 9 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 10 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 11 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ vom Board belegt |
| 13 | I2C SDA |  |
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
| 33 | frei - E/A | ADC1 |
| 34 | frei - der Taster des Boards | ⚠ nur Eingang, ADC1 |
| 35 | frei - Eingang | ⚠ nur Eingang, ADC1 |
| 36 | free (UART RX line) | ⚠ nur Eingang, ADC1 |

Die freien Pins liegen auf den Stiftleisten **EXT1 / EXT2** (2,54 mm) und
auf dem **UEXT**-Steckverbinder. GPIO34 bis GPIO39 sind reine Eingänge -
einen Ausgang dort lehnt der Editor ab. Der UEXT-Steckverbinder führt I2C
(GPIO13 / GPIO16) und SPI (GPIO14 / GPIO2 / GPIO15, gemeinsam mit dem
microSD-Steckplatz).

## Sicherheit

- Das Board ist nicht für Sicherheitsfunktionen vorgesehen. Ein Not-Halt,
  ein Türschalter oder ein Lichtvorhang wird in Hardware verdrahtet, niemals
  über ein Programm.
- Die GPIO-Pins arbeiten mit 3,3 V. Ein 24-V-Eingang braucht einen
  Optokoppler oder einen Pegelwandler; eine Relaisspule braucht einen
  Treiber (ein Relaismodul hat einen).

---

[← Übersicht](README.de.md) | [Übersicht](README.de.md) | [Runtime installieren →](install.de.md)
