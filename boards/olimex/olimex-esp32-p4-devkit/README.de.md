---
title: Olimex ESP32-P4-DevKit
slug: olimex-esp32-p4-devkit
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-devkit/
image: img/board-01.jpg
image_alt: Board Olimex ESP32-P4-DevKit mit der Ethernet-Buchse und den Stiftleisten
tags:
- esp32-p4
- ethernet
- olimex
---

# Olimex ESP32-P4-DevKit

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Board Olimex ESP32-P4-DevKit mit der Ethernet-Buchse und den Stiftleisten](img/board-01.jpg)

Das Olimex ESP32-P4-DevKit ist ein kleines quelloffenes Board mit dem ESP32-P4 - dem schnellsten ESP32, zwei Kerne mit 400 MHz und 32 MB PSRAM - und 100-Mbit-Ethernet. Es hat kein WLAN: Es ist eine kabelgebundene Steuerung. Mit ctrl32 laufen darauf die größten Programme, die ein ESP32 ausführen kann - 4096 Variablen - mit der Bedienseite in jedem Browser (WEBview), Modbus TCP und MQTT mit TLS.

**Geeignet für:**

- Eine kabelgebundene SPS mit großem Programm und vielen Modbus-Geräten
- Ein Gateway mit umfangreicher Logik zwischen Modbus TCP und MQTT
- Entwicklung eines eigenen P4-Boards

Seite des Boards im Katalog: [Olimex ESP32-P4-DevKit](https://ctrl32.com/hardware/boards/olimex-esp32-p4-devkit/)

![Olimex ESP32-P4-DevKit - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | ESP32-P4 (ESP32-P4NRW32) |  |
| Speicher | 16 MB flash, 32 MB PSRAM |  |
| Programmgröße | 4096 Variablen, 512 Alarme, 1024 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | 11 freie GPIO | siehe Pin-Belegung |
| Analogeingänge | über einen I2C-ADC (ADS1115) |  |
| Ethernet | ja - IP101GRI |  |
| Wi-Fi | nein |  |
| CAN (TWAI) | 1 - an freien Pins | braucht einen externen Transceiver |
| Modbus RTU (RS-485) | ja - an freien Pins | braucht einen externen Transceiver |
| Modbus TCP | Client und Server |  |
| MQTT | ja (auch TLS) | Home-Assistant-Discovery |
| WEBview | ja | die Bedienseite in jedem Browser |
| Display / Touch (HMI) | nein | die Bedienseite ist WEBview |
| USB | USB-C (Native USB) |  |
| Versorgung | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Was nicht unterstützt wird

- Die Steckverbinder für das MIPI-DSI-Display und die CSI-Kamera - dieses Board läuft in ctrl32 ohne Display (die Bedienseite ist WEBview).
- Der microSD-Steckplatz - ctrl32 hält das Programm und die Bildschirme im Flash des Boards.

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
- [Makerfabs MaTouch ESP32-P4 7"](../../makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.de.md) - der ESP32-P4 mit einem 7"-Touchscreen

