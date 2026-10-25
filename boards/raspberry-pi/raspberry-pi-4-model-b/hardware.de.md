---
title: 'Raspberry Pi 4 Model B: Hardware und Verdrahtung'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Raspberry Pi 4 Model B - Pin-Belegung
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Hardware und Verdrahtung

## Was Sie brauchen

- Ein Raspberry Pi 4 Model B (2 GB oder mehr empfohlen).
- Eine microSD-Karte (16 GB oder mehr) und der [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
- Das offizielle USB-C-Netzteil (5 V / 3 A).
- Ein Ethernet-Kabel im selben Netzwerk wie der PC.
- Für das HMI: ein HDMI-Monitor (Micro-HDMI-Kabel) oder ein DSI-Display; bei einem Touch-Monitor auch dessen USB.
- Ein PC mit dem [ctrl32-Editor](https://ctrl32.com/download/) (Windows).
- Optional, für das Beispiel all-in-one: ein USB-RS485-Adapter mit einem Modbus-RTU-I/O-Modul und einem Temperatursensor; ein CAN-HAT (MCP2515 oder MCP251xFD).

## Spannungsversorgung

| Quelle | Wo | Hinweis |
|---|---|---|
| USB-C | der Stromanschluss | 5 V / 3 A - das offizielle Netzteil |
| PoE | über einen PoE-HAT | optional |

!!! warning "Unterspannung"
    Mit einem schwächeren Netzteil drosselt der Pi und begrenzt den
    USB-Strom - ein USB-RS485-Adapter oder ein Touch-Monitor kann dann
    ausfallen. Verwenden Sie das offizielle Netzteil.

## Pin-Belegung

![Raspberry Pi 4 Model B - Pin-Belegung](pinout/pinout.png)

| GPIO | Funktion in ctrl32 | Hinweis |
|---|---|---|
| 2 | I2C1 SDA - I2C-Chips, RTC |  |
| 3 | I2C1 SCL |  |
| 4 | frei - von ctrl32 nicht genutzt | ⚠  |
| 8 | SPI0 CE0 - CAN-HAT |  |
| 9 | SPI0 MISO - CAN-HAT |  |
| 10 | SPI0 MOSI - CAN-HAT |  |
| 11 | SPI0 SCLK - CAN-HAT |  |
| 14 | UART TX - RS-485-HAT |  |
| 15 | UART RX - RS-485-HAT |  |
| 17 | frei - von ctrl32 nicht genutzt | ⚠  |
| 22 | frei - von ctrl32 nicht genutzt | ⚠  |
| 25 | Interrupt des CAN-HAT (MCP2515) |  |
| 27 | frei - von ctrl32 nicht genutzt | ⚠  |

Auf einem Linux-Board sind die Busse **Gerätenamen**, keine Pins: die
Runtime öffnet, was die Einstellungen des Geräts benennen - `can0` für
einen CAN-HAT oder einen USB-Adapter, `/dev/ttyUSB0` für einen
USB-RS485-Adapter (oder die eigene UART des Pi mit einem RS-485-HAT).
**Prepare a Linux device** richtet sie ein (Schritt 3 der Installation).
Der zweite Ethernet-Port für EtherCAT ist ein USB-Ethernet-Adapter.

## Sicherheit

- Das Board ist nicht für Sicherheitsfunktionen bestimmt. Ein Not-Halt,
  ein Türschalter oder ein Lichtvorhang wird in Hardware verdrahtet, nie
  über ein Programm.
- Fahren Sie den Pi herunter, bevor Sie die Versorgung trennen, wo immer
  das möglich ist - die Runtime hält die remanenten Werte sicher, das
  Betriebssystem bevorzugt ein sauberes Herunterfahren.

---

[← Übersicht](README.de.md) | [Übersicht](README.de.md) | [Runtime installieren →](install.de.md)
