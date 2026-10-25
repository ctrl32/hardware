---
title: 'Makerfabs MaTouch ESP32-P4 7": Hardware und Verdrahtung'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch ESP32-P4 7" - Pin-Belegung
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Hardware und Verdrahtung

## Was Sie brauchen

- Das Makerfabs MaTouch ESP32-P4 TFT with Touch 7" MIPI.
- Ein USB-C-Datenkabel - für das erste Übertragen der Runtime und für die Versorgung.
- Für die Versorgung: ein 5-V-USB-C-Netzteil mit mindestens 2 A (die Hintergrundbeleuchtung des Displays zieht das meiste davon).
- Ein Ethernet-Kabel oder das WLAN Ihres Netzwerks.
- Ein PC mit dem [ctrl32-Editor](https://ctrl32.com/download/) (Windows).
- Optional, für das Beispiel all-in-one: zwei Taster und ein Relaismodul an der Stiftleiste J6; ein ADS1115-Modul am I2C-Bus; ein 3,3-V-RS-485-Transceiver (z. B. MAX3485) und ein 3,3-V-CAN-Transceiver (z. B. SN65HVD230).

## Spannungsversorgung

| Quelle | Wo | Hinweis |
|---|---|---|
| USB 5 V | der USB-C-Anschluss | 2 A oder mehr - die Hintergrundbeleuchtung des 7"-Displays zieht das meiste davon |
| Li-Po-Akku | der Akku-Anschluss | 3,7 V, Ladung auf dem Board |

!!! warning "Ein schwaches Netzteil"
    Der USB-Port eines PCs trägt das Board mit eingeschalteter
    Hintergrundbeleuchtung oft nicht. Startet das Board neu, während der
    Bildschirm aufleuchtet, verwenden Sie ein Netzteil mit 5 V / 2 A oder
    einen aktiven USB-Hub.

## Pin-Belegung

![Makerfabs MaTouch ESP32-P4 7" - Pin-Belegung](pinout/pinout.png)

| GPIO | Funktion in ctrl32 | Hinweis |
|---|---|---|
| 0 | RTC XTAL P | ⚠  |
| 1 | RTC XTAL N | ⚠  |
| 2 | frei - E/A |  |
| 3 | frei - E/A |  |
| 4 | frei - E/A |  |
| 5 | frei - E/A |  |
| 6 | C6 IO2 | ⚠  |
| 7 | TOUCH SDA |  |
| 8 | TOUCH SCL |  |
| 20 | frei - E/A |  |
| 21 | frei - E/A |  |
| 22 | TOUCH RST |  |
| 23 | TFT BL |  |
| 26 | USB1 PAIR | ⚠  |
| 27 | DSI RST |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 29 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 30 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 31 | Ethernet MDC (IP101GRI) | ⚠ vom Board belegt |
| 32 | frei - E/A |  |
| 33 | frei - E/A |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 35 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 36 | frei - E/A | ⚠ Strapping-Pin |
| 37 | CONSOLE RX | ⚠ Strapping-Pin |
| 38 | CONSOLE TX | ⚠ Strapping-Pin |
| 45 | MOSFET GATE | ⚠  |
| 46 | frei - E/A |  |
| 47 | frei - E/A |  |
| 48 | frei - E/A |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 50 | Ethernet RMII (IP101GRI) | ⚠ vom Board belegt |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ vom Board belegt |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ vom Board belegt |
| 53 | AMP EN | ⚠  |
| 54 | C6 EN | ⚠  |

Die freien Pins liegen auf den Stiftleisten **J6** und **J10** und auf den
beiden Grove-Steckern (**J1**, **J2**). Der I2C-Bus des Boards (GPIO7 /
GPIO8) trägt den Touch-Controller und den Audio-Codec; weitere I2C-Chips
(ein ADS1115, ein Sensor) hängen am selben Bus. CAN und RS-485 haben auf
dem Board keinen Transceiver: das Beispiel legt sie auf freie Pins -
**CAN** TX GPIO20 / RX GPIO21 (Grove J2), **RS-485** TX GPIO4 / RX GPIO5 /
DE GPIO32 (J10) - jeweils an ein 3,3-V-Transceiver-Modul.

## Sicherheit

- Das Board ist nicht für Sicherheitsfunktionen bestimmt. Ein Not-Halt,
  ein Türschalter oder ein Lichtvorhang wird in Hardware verdrahtet, nie
  über ein Programm oder einen Touchscreen.
- Die GPIO-Pins führen 3,3 V. Ein 24-V-Signal braucht einen Optokoppler;
  eine Relaisspule braucht einen Treiber (ein Relaismodul hat einen).
- Kapazitiver Touch kann neben einer starken Störquelle (einem
  Frequenzumrichter) eine falsche Berührung erkennen. Kritische Befehle auf
  einem Bildschirm verlangen eine Bestätigung.

## Fotos

![Makerfabs MaTouch ESP32-P4 7" - Foto 1](img/board-01.jpg)
![Makerfabs MaTouch ESP32-P4 7" - Foto 2](img/board-02.jpg)
![Makerfabs MaTouch ESP32-P4 7" - Foto 3](img/board-03.jpg)
![Makerfabs MaTouch ESP32-P4 7" - Foto 4](img/board-04.jpg)
![Makerfabs MaTouch ESP32-P4 7" - Foto 5](img/board-05.jpg)
![Makerfabs MaTouch ESP32-P4 7" - Foto 6](img/board-06.jpg)
![Makerfabs MaTouch ESP32-P4 7" - Foto 7](img/board-07.jpg)
![Makerfabs MaTouch ESP32-P4 7" - Foto 8](img/board-08.jpg)

---

[← Übersicht](README.de.md) | [Übersicht](README.de.md) | [Runtime installieren →](install.de.md)
