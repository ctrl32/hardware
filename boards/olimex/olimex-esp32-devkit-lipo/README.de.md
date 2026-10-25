---
title: Olimex ESP32-DevKit-LiPo
slug: olimex-esp32-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-devkit-lipo/
image: img/board-01.jpg
image_alt: Board Olimex ESP32-DevKit-LiPo mit seinen zwei Stiftleisten und dem Micro-USB-Anschluss
tags:
- esp32
- wifi
- battery
- olimex
---

# Olimex ESP32-DevKit-LiPo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Board Olimex ESP32-DevKit-LiPo mit seinen zwei Stiftleisten und dem Micro-USB-Anschluss](img/board-01.jpg)

Das Olimex ESP32-DevKit-LiPo ist ein quelloffenes ESP32-Entwicklungsboard mit WLAN, allen GPIO des Moduls auf zwei Stiftleisten und einem Li-Po-Ladegerät, das es bei einem Stromausfall weiterlaufen lässt. Mit ctrl32 ist es eine kleine WLAN-SPS: ein Ladder-Programm im Chip, Ein- und Ausgänge an den Pins, die Bedienseite in jedem Browser (WEBview), Modbus TCP und MQTT.

**Geeignet für:**

- Eine WLAN-Steuerung für einen Raum, ein Gewächshaus oder eine Pumpe
- Ein akkugepufferter Datenlogger, der per MQTT veröffentlicht
- ctrl32 auf dem Steckbrett kennenlernen

Seite des Boards im Katalog: [Olimex ESP32-DevKit-LiPo](https://ctrl32.com/hardware/boards/olimex-esp32-devkit-lipo/)

![Olimex ESP32-DevKit-LiPo - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Speicher | 4 MB flash |  |
| Programmgröße | 128 Variablen, 32 Alarme, 128 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | 19 freie GPIO | 4 davon nur Eingänge |
| Analogeingänge | 6 auf dem Chip (ADC1) | GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO39 |
| Ethernet | nein |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - an freien Pins | braucht einen externen Transceiver |
| Modbus RTU (RS-485) | ja - an freien Pins | braucht einen externen Transceiver |
| Modbus TCP | Client und Server |  |
| MQTT | ja | Home-Assistant-Discovery |
| WEBview | ja | die Bedienseite in jedem Browser |
| Display / Touch (HMI) | nein | die Bedienseite ist WEBview |
| USB | Micro-USB (CH340 USB-UART) |  |
| Versorgung | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Was nicht unterstützt wird

- Bluetooth - der ESP32 hat es, ctrl32 nutzt es nicht.
- Die Messeingänge für Akku und Versorgung (GPIO35 / GPIO39) sind in ctrl32 freie Pins, keine Akkuanzeige.

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
- Olimex ESP32-S3-DevKit-Lipo - dieselbe Idee mit dem ESP32-S3 und PSRAM

