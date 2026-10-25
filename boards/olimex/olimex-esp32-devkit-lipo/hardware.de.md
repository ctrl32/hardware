---
title: 'Olimex ESP32-DevKit-LiPo: Hardware und Verdrahtung'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-DevKit-LiPo - Pin-Belegung
tags:
- esp32
- wifi
- battery
- olimex
---

# Hardware und Verdrahtung

## Was Sie brauchen

- Das Olimex ESP32-DevKit-LiPo.
- Ein Micro-USB-Datenkabel - für das Aufspielen und für die Spannungsversorgung (5 V).
- Name und Passwort Ihres 2,4-GHz-WLANs.
- Ein PC mit dem [ctrl32-Editor](https://ctrl32.com/download/) (Windows).
- Optional, für das Beispiel all-in-one: ein Taster von GPIO13 nach GND; ein Relaismodul oder eine LED mit Vorwiderstand an GPIO4; ein Potentiometer (10 k) zwischen 3,3 V und GND mit dem Schleifer an GPIO32; ein 3,3-V-CAN-Transceiver an GPIO14 / GPIO34 und ein RS-485-Transceiver an GPIO16 / GPIO36 / GPIO17 (DE); eine Li-Po-Zelle als Pufferung.

## Spannungsversorgung

| Quelle | Wo | Hinweis |
|---|---|---|
| USB 5 V | der Micro-USB-Anschluss | Spannungsversorgung und Programmierung |
| Li-Po-Akku | der Akkuanschluss | wird auf dem Board geladen, übernimmt beim Ausfall von USB |

## Pin-Belegung

![Olimex ESP32-DevKit-LiPo - Pin-Belegung](pinout/pinout.png)

| GPIO | Funktion in ctrl32 | Hinweis |
|---|---|---|
| 4 | frei - E/A |  |
| 6 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 7 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 8 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 9 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 10 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 11 | SPI-Flash des Moduls | ⚠ vom Board belegt |
| 13 | frei - E/A |  |
| 14 | frei - E/A |  |
| 16 | frei - E/A |  |
| 17 | frei - E/A |  |
| 18 | frei - E/A |  |
| 19 | frei - E/A |  |
| 21 | frei - E/A |  |
| 22 | frei - E/A |  |
| 23 | frei - E/A |  |
| 25 | frei - E/A |  |
| 26 | frei - E/A |  |
| 27 | frei - E/A |  |
| 32 | frei - E/A | ADC1 |
| 33 | frei - E/A | ADC1 |
| 34 | frei - Eingang | ⚠ nur Eingang, ADC1 |
| 35 | free (BAT SENSE line) | ⚠ nur Eingang, ADC1 |
| 36 | frei - Eingang | ⚠ nur Eingang, ADC1 |
| 39 | free (PWR SENSE line) | ⚠ nur Eingang, ADC1 |

Die zwei Stiftleisten führen die freien GPIO des Moduls. GPIO34 bis GPIO39
sind reine Eingänge; GPIO0, 2, 12 und 15 sind Strapping-Pins - lassen Sie
sie für Eingänge oder prüfen Sie sie vor dem Einsatz. Ein Taster nach GND
braucht keinen Widerstand: ctrl32 liest ihn invertiert mit dem Pull-up des
Chips.

## Sicherheit

- Das Board ist nicht für Sicherheitsfunktionen bestimmt. Ein Not-Halt,
  ein Türschalter oder ein Lichtvorhang wird in Hardware verdrahtet, nie
  über ein Programm.
- Die GPIO-Pins führen 3,3 V. Ein 24-V-Signal braucht einen Optokoppler
  oder einen Pegelwandler; eine Relaisspule braucht einen Treiber (ein
  Relaismodul hat ihn).

---

[← Übersicht](README.de.md) | [Übersicht](README.de.md) | [Runtime installieren →](install.de.md)
