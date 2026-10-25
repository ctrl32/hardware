---
title: Olimex ESP32-GATEWAY
slug: olimex-esp32-gateway
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-gateway/
image: img/board-01.jpg
image_alt: Board Olimex ESP32-GATEWAY mit Ethernet-Buchse und USB-C-Anschluss
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Olimex ESP32-GATEWAY

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Board Olimex ESP32-GATEWAY mit Ethernet-Buchse und USB-C-Anschluss](img/board-01.jpg)

Das Olimex ESP32-GATEWAY ist ein kompaktes ESP32-Board mit 100-Mbit-Ethernet und WLAN - klein genug für eine Abzweigdose. Mit ctrl32 ist es ein Gateway mit eigener Logik: Modbus-TCP-Geräte werden ausgelesen und per MQTT veröffentlicht, ein Ladder-Programm läuft im Chip und seine Bedienseite in jedem Browser (WEBview).

**Geeignet für:**

- Ein Gateway von Modbus TCP zu MQTT mit eigener Logik
- Eine kleine Steuerung in einer Abzweigdose, am Ethernet
- Hausautomation - Zähler auslesen, schalten über Modbus-I/O-Module

Seite des Boards im Katalog: [Olimex ESP32-GATEWAY](https://ctrl32.com/hardware/boards/olimex-esp32-gateway/)

![Olimex ESP32-GATEWAY - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Speicher | 4 MB flash |  |
| Programmgröße | 128 Variablen, 32 Alarme, 128 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | 3 freie GPIO | 1 davon nur Eingänge |
| Analogeingänge | 2 auf dem Chip (ADC1) | GPIO33, GPIO34 |
| Ethernet | ja - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - an freien Pins | braucht einen externen Transceiver |
| Modbus RTU (RS-485) | ja - an freien Pins | braucht einen externen Transceiver |
| Modbus TCP | Client und Server |  |
| MQTT | ja | Home-Assistant-Discovery |
| WEBview | ja | die Bedienseite in jedem Browser |
| Display / Touch (HMI) | nein | die Bedienseite ist WEBview |
| USB | USB-C (CH340 USB-UART) |  |
| Versorgung | 5 V USB |  |
<!-- capabilities:end -->

### Was nicht unterstützt wird

- Bluetooth - der ESP32 hat es, ctrl32 nutzt es nicht.
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

