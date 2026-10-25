---
title: LaskaKit ESPlan
slug: laskakit-esplan
sidebar_position: 10
hardware: /hardware/boards/laskakit-esplan/
image: img/board-01.jpg
image_alt: Board LaskaKit ESPlan mit der Ethernet-Buchse, der RS-485-Klemme und der Versorgungsklemme
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# LaskaKit ESPlan

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Board LaskaKit ESPlan mit der Ethernet-Buchse, der RS-485-Klemme und der Versorgungsklemme](img/board-01.jpg)

Das LaskaKit ESPlan ist ein Industrie-Board mit dem ESP32: 10/100-Ethernet, eine RS-485-Schnittstelle mit Schutzbeschaltung und zuschaltbarem Abschluss, WLAN und eine weite Spannungsversorgung von 7-40 V an einer Schraubklemme (oder PoE mit einem Zusatzmodul). Mit ctrl32 ist es ein Modbus-RTU-Master oder -Slave im Schaltschrank - ein Ladder-Programm im Chip, RS-485-Geräte gelesen und geschrieben, die Werte auf Modbus TCP, MQTT und seiner Bedienseite (WEBview).

**Geeignet für:**

- Ein Modbus-RTU-Master für Zähler, Sensoren und Frequenzumrichter, an 24 V versorgt
- Ein Modbus-RTU/TCP-Gateway mit eigener Logik
- Gebäudeautomation im Schaltschrank

Seite des Boards im Katalog: [LaskaKit ESPlan](https://ctrl32.com/hardware/boards/laskakit-esplan/)

![LaskaKit ESPlan - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Speicher | 4 MB flash |  |
| Programmgröße | 128 Variablen, 32 Alarme, 128 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | 5 freie GPIO | 2 davon nur Eingänge |
| Analogeingänge | 2 auf dem Chip (ADC1) | GPIO35, GPIO39 |
| Ethernet | ja - LAN8720A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - an freien Pins | braucht einen externen Transceiver |
| Modbus RTU (RS-485) | ja |  |
| Modbus TCP | Client und Server |  |
| MQTT | ja | Home-Assistant-Discovery |
| WEBview | ja | die Bedienseite in jedem Browser |
| Display / Touch (HMI) | nein | die Bedienseite ist WEBview |
| USB | USB-C (CH9102 USB-UART) |  |
| Versorgung | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Was nicht unterstützt wird

- Bluetooth - der ESP32 hat es, ctrl32 nutzt es nicht.
- Der microSD-Steckplatz - ctrl32 hält das Programm und die Bildschirme im eigenen Flash des Chips.

## Die Anleitung

| Schritt | Seite |
|---|---|
| 1 | [Hardware und Verdrahtung](hardware.de.md) - was Sie brauchen, Spannungsversorgung, die Pin-Belegung |
| 2 | [Runtime installieren](install.de.md) - der Editor, das Board, der erste Upload |
| 3 | [Einrichten](configure.de.md) - Netzwerk, E/A, Kommunikation |
| 4 | [Beispielprojekte](examples/README.de.md) - alles, was das Board kann, fertig zum Öffnen |
| - | [Fehlersuche](troubleshooting.de.md) |

## Dateien

-

## Weiter

- [ctrl32-Dokumentation](https://ctrl32.com/docs/) - der Editor, die Sprachen, jeder Baustein
- [Editor herunterladen](https://ctrl32.com/download/)
- [Alle getesteten Boards](../../README.de.md)

