---
title: Olimex ESP32-PoE-ISO
slug: olimex-esp32-poe-iso
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe-iso/
image: img/board-01.jpg
image_alt: Board Olimex ESP32-PoE-ISO mit Ethernet-Buchse und galvanisch getrennter PoE-Versorgung
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Olimex ESP32-PoE-ISO

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Board Olimex ESP32-PoE-ISO mit Ethernet-Buchse und galvanisch getrennter PoE-Versorgung](img/board-01.jpg)

Das Olimex ESP32-PoE-ISO ist das ESP32-PoE mit galvanisch getrennter Power-over-Ethernet-Versorgung: ein einziges Netzwerkkabel versorgt es mit Spannung und bindet es ins Netz ein, und ein PC kann über USB angeschlossen bleiben, während das Board an PoE läuft. Mit ctrl32 ist es eine kompakte SPS für den Schaltschrank - ein Ladder-Programm im Chip, die Bedienseite in jedem Browser (WEBview), Modbus TCP zu Zählern und I/O-Modulen und MQTT zu Home Assistant.

**Geeignet für:**

- Eine kleine SPS im Schaltschrank, versorgt aus einem PoE-Switch
- Ein Modbus-TCP-Gateway, das Zähler ausliest und per MQTT veröffentlicht
- Hausautomation - ein Raum oder ein Heizungskeller an einem Kabel

Seite des Boards im Katalog: [Olimex ESP32-PoE-ISO](https://ctrl32.com/hardware/boards/olimex-esp32-poe-iso/)

![Olimex ESP32-PoE-ISO - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

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

-

## Weiter

- [ctrl32-Dokumentation](https://ctrl32.com/docs/) - der Editor, die Sprachen, jeder Baustein
- [Editor herunterladen](https://ctrl32.com/download/)
- [Alle getesteten Boards](../../README.de.md)
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.de.md) - dasselbe Board ohne die galvanisch getrennte Versorgung
- [Olimex ESP32-POE2](../olimex-esp32-poe2/README.de.md) - die nächste Generation

