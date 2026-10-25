---
title: 'Olimex ESP32-EVB: Hardware und Verdrahtung'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-EVB - Pin-Belegung
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Hardware und Verdrahtung

## Was Sie brauchen

- Das Olimex ESP32-EVB.
- Ein Micro-USB-Datenkabel - für das erste Aufspielen der Runtime.
- Spannungsversorgung: ein 5-V-USB-Netzteil oder 5 V an der Schraubklemme.
- Ein Ethernet-Kabel und ein freier Port in Ihrem Netzwerk.
- Ein PC mit dem [ctrl32-Editor](https://ctrl32.com/download/) (Windows).
- Optional, für das Beispiel all-in-one: ein Potentiometer (10 k) zwischen 3,3 V und GND mit dem Schleifer an GPIO36 (UEXT); ein CAN-Knoten oder ein CAN-Adapter und zwei Abschlusswiderstände mit 120 Ohm.
- Optional: das Display Olimex MOD-LCD2.8RTP (2,8 Zoll, 240 x 320, resistiver Touch) am UEXT-Steckverbinder.

## Spannungsversorgung

| Quelle | Wo | Hinweis |
|---|---|---|
| USB 5 V | der Micro-USB-Anschluss | der Weg für das erste Aufspielen |
| 5 V DC | die Schraubklemme | für den Schaltschrank |
| Li-Po-Akku | der Akkuanschluss | wird auf dem Board geladen |

!!! warning "Die Relais schalten Netzspannung"
    Verdrahten Sie die Relaiskontakte nur bei spannungslosem Board, in
    einem Gehäuse und nur als Person, die an Netzinstallationen arbeiten
    darf. Die Kontakte vertragen 10 A / 250 VAC; ein Motor oder ein
    Heizgerät darüber braucht ein Schütz, das vom Relais angesteuert wird.

## Pin-Belegung

![Olimex ESP32-EVB - Pin-Belegung](pinout/pinout.png)

| GPIO | Funktion in ctrl32 | Hinweis |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ vom Board belegt |
| 2 | TFT MOSI | ⚠ Strapping-Pin |
| 2 | SPI MOSI | ⚠ Strapping-Pin |
| 4 | free (UART TX line) |  |
| 5 | CAN TX |  |
| 6 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 7 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 8 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 9 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 10 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 11 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 13 | I2C SDA |  |
| 14 | TFT SCLK |  |
| 14 | SPI SCLK |  |
| 15 | TFT DC | ⚠ Strapping-Pin |
| 15 | SPI MISO | ⚠ Strapping-Pin |
| 16 | I2C SCL |  |
| 17 | TFT CS |  |
| 17 | free (SPI CS line) |  |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ vom Board belegt |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ vom Board belegt |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ vom Board belegt |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ vom Board belegt |
| 23 | Ethernet MDC (LAN8710A) | ⚠ vom Board belegt |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ vom Board belegt |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ vom Board belegt |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ vom Board belegt |
| 32 | free (REL1 line) | ADC1 |
| 33 | free (REL2 line) | ADC1 |
| 34 | frei - der Taster des Boards | ⚠ nur Eingang, ADC1 |
| 35 | CAN RX |  |
| 36 | free (UART RX line) | ⚠ nur Eingang, ADC1 |

**Relais:** REL1 an GPIO32, REL2 an GPIO33. **Taster:** BUT1 an GPIO34
(reiner Eingang). **CAN:** der Transceiver auf dem Board an GPIO5 (TX) /
GPIO35 (RX), CAN_H / CAN_L an der Klemme - schließen Sie den Bus an beiden
Enden mit 120 Ohm ab. Der **UEXT**-Steckverbinder führt I2C
(GPIO13 / GPIO16), SPI und einen freien UART (GPIO4 / GPIO36); das
optionale Display nutzt seine SPI-Leitungen.

## Sicherheit

- Das Board ist nicht für Sicherheitsfunktionen bestimmt. Ein Not-Halt,
  ein Türschalter oder ein Lichtvorhang wird in Hardware verdrahtet, nie
  über ein Programm.
- Die GPIO-Pins führen 3,3 V. Ein 24-V-Signal braucht einen Optokoppler
  oder einen Pegelwandler; eine Relaisspule braucht einen Treiber (ein
  Relaismodul hat ihn).

---

[← Übersicht](README.de.md) | [Übersicht](README.de.md) | [Runtime installieren →](install.de.md)
