---
title: 'LaskaKit ESPlan: Hardware und Verdrahtung'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: LaskaKit ESPlan - Pin-Belegung
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Hardware und Verdrahtung

## Was Sie brauchen

- Das LaskaKit ESPlan.
- Ein USB-C-Datenkabel - für das erste Aufspielen der Runtime.
- Spannungsversorgung: 12 oder 24 V DC an der Schraubklemme (7-40 V), oder 5 V über USB-C.
- Ein Ethernet-Kabel und ein freier Port in Ihrem Netzwerk.
- Ein PC mit dem [ctrl32-Editor](https://ctrl32.com/download/) (Windows).
- Optional, für das Beispiel all-in-one: ein Modbus-RTU-Temperatursensor (Unit 1) an der RS-485-Klemme; ein Taster von GPIO16 nach GND; ein Potentiometer (10 k) zwischen 3,3 V und GND mit dem Schleifer an GPIO35; ein 3,3-V-CAN-Transceiver an GPIO14 (TX) / GPIO39 (RX).

## Spannungsversorgung

| Quelle | Wo | Hinweis |
|---|---|---|
| 7-40 V DC | die Schraubklemme | 12 oder 24 V empfohlen |
| USB 5 V | der USB-C-Anschluss | der Weg für das erste Aufspielen |
| PoE | über das optionale PoE-Modul (802.3af) | Zusatzmodul |

## Pin-Belegung

![LaskaKit ESPlan - Pin-Belegung](pinout/pinout.png)

| GPIO | Funktion in ctrl32 | Hinweis |
|---|---|---|
| 0 | free (LED0 line) | ⚠ Strapping-Pin |
| 4 | RS485 TX |  |
| 5 | Ethernet PHY power (LAN8720A) | ⚠ vom Board belegt |
| 6 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 7 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 8 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 9 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 10 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 11 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 12 | SPI MISO | ⚠ Strapping-Pin |
| 13 | SPI MOSI |  |
| 14 | free (SPI SCLK line) |  |
| 15 | SPI CS | ⚠ Strapping-Pin |
| 16 | frei - E/A |  |
| 17 | Ethernet 50 MHz clock (LAN8720A) | ⚠ vom Board belegt |
| 18 | Ethernet MDIO (LAN8720A) | ⚠ vom Board belegt |
| 19 | Ethernet RMII TXD0 (LAN8720A) | ⚠ vom Board belegt |
| 21 | Ethernet RMII TX_EN (LAN8720A) | ⚠ vom Board belegt |
| 22 | Ethernet RMII TXD1 (LAN8720A) | ⚠ vom Board belegt |
| 23 | Ethernet MDC (LAN8720A) | ⚠ vom Board belegt |
| 25 | Ethernet RMII RXD0 (LAN8720A) | ⚠ vom Board belegt |
| 26 | Ethernet RMII RXD1 (LAN8720A) | ⚠ vom Board belegt |
| 27 | Ethernet RMII CRS_DV (LAN8720A) | ⚠ vom Board belegt |
| 32 | TOUCH SCL |  |
| 33 | TOUCH SDA |  |
| 35 | frei - Eingang | ⚠ nur Eingang, ADC1 |
| 36 | RS485 RX |  |
| 39 | frei - Eingang | ⚠ nur Eingang, ADC1 |

**RS-485:** A und B an der Klemme, der WS3081-Transceiver an GPIO4 (TX) /
GPIO36 (RX); eine Steckbrücke schaltet den 120-Ohm-Abschluss zu - setzen
Sie ihn nur an den beiden Enden der Leitung. Die **uSup**-Steckverbinder
führen I2C (GPIO33 / GPIO32) und SPI. Die LED des Boards liegt an GPIO0
(ein Strapping-Pin - belassen Sie ihn als Ausgang, den das Programm
ansteuert).

## Sicherheit

- Das Board ist nicht für Sicherheitsfunktionen bestimmt. Ein Not-Halt,
  ein Türschalter oder ein Lichtvorhang wird in Hardware verdrahtet, nie
  über ein Programm.
- Die GPIO-Pins führen 3,3 V. Ein 24-V-Signal braucht einen Optokoppler
  oder einen Pegelwandler; eine Relaisspule braucht einen Treiber (ein
  Relaismodul hat ihn).

---

[← Übersicht](README.de.md) | [Übersicht](README.de.md) | [Runtime installieren →](install.de.md)
