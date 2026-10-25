---
title: Olimex ESP32-EVB
slug: olimex-esp32-evb
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-evb/
image: img/board-01.jpg
image_alt: Board Olimex ESP32-EVB mit seinen zwei Relais, der Ethernet-Buchse und der CAN-Klemme
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Olimex ESP32-EVB

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 240x320](https://img.shields.io/badge/HMI-240x320-0891b2)

![Board Olimex ESP32-EVB mit seinen zwei Relais, der Ethernet-Buchse und der CAN-Klemme](img/board-01.jpg)

Das Olimex ESP32-EVB ist ein ESP32-Board, gebaut zum Steuern: zwei Relais (10 A / 250 VAC), ein CAN-Transceiver, Ethernet und WLAN auf einem Board. Mit ctrl32 ist es eine fertige SPS - die Relais und der Taster sind Variablen eines Ladder-Programms, CAN spricht mit Antrieben und I/O-Knoten, und die Bedienseite läuft in jedem Browser (WEBview). Ein optionales 2,8"-Touchdisplay am UEXT-Steckverbinder macht daraus ein kleines Bedienpanel.

**Geeignet für:**

- Eine Relaissteuerung - Heizung, Pumpen, Licht - mit Ethernet
- Ein CAN-Master für einen Antrieb oder CANopen-I/O-Knoten
- Ein Thermostat oder ein kleines Panel mit dem optionalen 2,8"-Display

Seite des Boards im Katalog: [Olimex ESP32-EVB](https://ctrl32.com/hardware/boards/olimex-esp32-evb/)

![Olimex ESP32-EVB - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Speicher | 4 MB flash |  |
| Programmgröße | 128 Variablen, 32 Alarme, 128 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | 6 freie GPIO | 2 davon nur Eingänge |
| Analogeingänge | 4 auf dem Chip (ADC1) | GPIO32, GPIO33, GPIO34, GPIO36 |
| Ethernet | ja - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 |  |
| Modbus RTU (RS-485) | ja - an freien Pins | braucht einen externen Transceiver |
| Modbus TCP | Client und Server |  |
| MQTT | ja | Home-Assistant-Discovery |
| WEBview | ja | die Bedienseite in jedem Browser |
| Display / Touch (HMI) | - 240x320, - |  |
| USB | Micro-USB (CH340T USB-UART) |  |
| Versorgung | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Was nicht unterstützt wird

- Bluetooth.
- Der IR-Empfänger und -Sender - ctrl32 nutzt sie auf diesem Board nicht.
- Der microSD-Steckplatz - ctrl32 hält Programm und Bildschirme im eigenen Flash des Chips.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.de.md) - Ethernet und Power over Ethernet

