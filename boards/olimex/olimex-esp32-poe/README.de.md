---
title: Olimex ESP32-PoE
slug: olimex-esp32-poe
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/board-01.jpg
image_alt: Board Olimex ESP32-PoE von oben, mit Ethernet-Buchse und USB-Anschluss
tags:
- esp32
- ethernet
- poe
- olimex
---

# Olimex ESP32-PoE

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Board Olimex ESP32-PoE von oben, mit Ethernet-Buchse und USB-Anschluss](img/board-01.jpg)

Das Olimex ESP32-PoE ist ein quelloffenes ESP32-Board mit Ethernet und Power over Ethernet: ein einziges Netzwerkkabel versorgt es mit Spannung und bindet es ins Netz ein. Mit ctrl32 wird daraus eine kompakte SPS für den Schaltschrank oder ein Wandgehäuse - ein Ladder-Programm im Chip, die Bedienseite in jedem Browser im Netzwerk (WEBview), Modbus TCP zu Zählern und I/O-Modulen und MQTT zu Home Assistant oder einem beliebigen Broker.

**Geeignet für:**

- Eine kleine SPS im Schaltschrank, versorgt aus einem PoE-Switch
- Ein Modbus-TCP-Gateway, das Zähler ausliest und per MQTT veröffentlicht
- Hausautomation - ein Raum oder ein Heizungskeller an einem Kabel

Seite des Boards im Katalog: [Olimex ESP32-PoE](https://ctrl32.com/hardware/boards/olimex-esp32-poe/)

![Olimex ESP32-PoE - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Speicher | 4 MB flash |  |
| Programmgröße | 128 Variablen, 32 Alarme, 128 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | 6 freie GPIO | 3 davon nur Eingänge |
| Analogeingänge | 4 auf dem Chip (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | ja - LAN8710A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - an freien Pins | braucht einen externen Transceiver |
| Modbus RTU (RS-485) | ja - an freien Pins | braucht einen externen Transceiver |
| Modbus TCP | Client und Server |  |
| MQTT | ja | Home-Assistant-Discovery |
| WEBview | ja | die Bedienseite in jedem Browser |
| Display / Touch (HMI) | nein | die Bedienseite ist WEBview |
| USB | Micro-USB (CH340T USB-UART) |  |
| Versorgung | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Was nicht unterstützt wird

- Bluetooth - der ESP32 hat es, ctrl32 nutzt es nicht.
- Der microSD-Steckplatz - ctrl32 hält Programm und Bildschirme im eigenen Flash des Chips.
- Der Akkueingang funktioniert als Eigenschaft des Boards; ctrl32 liest den Ladezustand nicht aus.

## Die Anleitung

| Schritt | Seite |
|---|---|
| 1 | [Hardware und Verdrahtung](hardware.de.md) - was Sie brauchen, Spannungsversorgung, die Pin-Belegung |
| 2 | [Runtime installieren](install.de.md) - der Editor, das Board, der erste Upload |
| 3 | [Einrichten](configure.de.md) - Netzwerk, E/A, Kommunikation |
| 4 | [Beispielprojekte](examples/README.de.md) - alles, was das Board kann, fertig zum Öffnen |
| - | [Fehlersuche](troubleshooting.de.md) |

## Dateien

| Datei | Was |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | die Pin-Belegung, als Vektorgrafik (auch als [PNG](pinout/pinout.png)) |
| [olimex-esp32-poe-schematic.pdf](schematics/olimex-esp32-poe-schematic.pdf) | ESP32-PoE schematic Rev M2 |
| [esp32-poe-revm2.zip](schematics/esp32-poe-revm2.zip) | KiCad project |
| [olimex-esp32-poe-user-manual.pdf](datasheets/olimex-esp32-poe-user-manual.pdf) | ESP32-PoE user manual |
| [olimex-esp32-poe.zip](3d/olimex-esp32-poe.zip) | 3D-Modell (STEP, als Zip) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | woher die Fotos, Schaltpläne und Modelle stammen |

## Weiter

- [ctrl32-Dokumentation](https://ctrl32.com/docs/) - der Editor, die Sprachen, jeder Baustein
- [Editor herunterladen](https://ctrl32.com/download/)
- [Alle getesteten Boards](../../README.de.md)
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.de.md) - dasselbe Board mit galvanisch getrennter PoE-Versorgung
- [Olimex ESP32-POE2](../olimex-esp32-poe2/README.de.md) - die nächste Generation

