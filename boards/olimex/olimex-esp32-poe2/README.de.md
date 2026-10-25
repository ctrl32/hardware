---
title: Olimex ESP32-POE2
slug: olimex-esp32-poe2
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe2/
image: img/board-01.jpg
image_alt: Board Olimex ESP32-POE2 mit Ethernet-Buchse und den Spannungsausgängen
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Olimex ESP32-POE2

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Board Olimex ESP32-POE2 mit Ethernet-Buchse und den Spannungsausgängen](img/board-01.jpg)

Das Olimex ESP32-POE2 ist die nächste Generation des ESP32-PoE: ein ESP32 mit 8 MB PSRAM, Ethernet und Power over Ethernet nach IEEE 802.3at, das auch Ihre Feldgeräte versorgt - Ausgänge mit 24 V oder 12 V, 5 V und 3,3 V, bis zu 25 W aus dem Netzwerkkabel. Mit ctrl32 ist es eine SPS im Schaltschrank an einem einzigen Kabel: Ladder-Logik, WEBview, Modbus TCP und MQTT, mit der vollen Programmgröße eines klassischen ESP32 mit PSRAM.

**Geeignet für:**

- Eine Schaltschrank-SPS, die ihre Sensoren und ein kleines Relaismodul aus PoE versorgt
- Ein Modbus-TCP-Gateway mit MQTT zu Home Assistant
- Gebäudeautomation an einem Kabel pro Raum

Seite des Boards im Katalog: [Olimex ESP32-POE2](https://ctrl32.com/hardware/boards/olimex-esp32-poe2/)

![Olimex ESP32-POE2 - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | ESP32 (ESP32-WROVER-E-N4R8) |  |
| Speicher | 4 MB flash, 8 MB PSRAM |  |
| Programmgröße | 512 Variablen, 128 Alarme, 1024 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | 5 freie GPIO | 3 davon nur Eingänge |
| Analogeingänge | 3 auf dem Chip (ADC1) | GPIO34, GPIO36, GPIO39 |
| Ethernet | ja - LAN8710A |  |
| Power over Ethernet | IEEE 802.3at |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - an freien Pins | braucht einen externen Transceiver |
| Modbus RTU (RS-485) | ja - an freien Pins | braucht einen externen Transceiver |
| Modbus TCP | Client und Server |  |
| MQTT | ja | Home-Assistant-Discovery |
| WEBview | ja | die Bedienseite in jedem Browser |
| Display / Touch (HMI) | nein | die Bedienseite ist WEBview |
| USB | USB-C |  |
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

-

## Weiter

- [ctrl32-Dokumentation](https://ctrl32.com/docs/) - der Editor, die Sprachen, jeder Baustein
- [Editor herunterladen](https://ctrl32.com/download/)
- [Alle getesteten Boards](../../README.de.md)
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.de.md) - die erste Generation
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.de.md) - mit galvanisch getrennter PoE-Versorgung

