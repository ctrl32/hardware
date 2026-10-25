---
title: Olimex ESP32-S3-DevKit-Lipo
slug: olimex-esp32-s3-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-s3-devkit-lipo/
image: img/board-01.jpg
image_alt: Board Olimex ESP32-S3-DevKit-Lipo mit seinen zwei USB-C-Anschlüssen und den Stiftleisten
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Olimex ESP32-S3-DevKit-Lipo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Board Olimex ESP32-S3-DevKit-Lipo mit seinen zwei USB-C-Anschlüssen und den Stiftleisten](img/board-01.jpg)

Das Olimex ESP32-S3-DevKit-Lipo ist ein quelloffenes ESP32-S3-Board mit 8 MB Flash, 8 MB PSRAM, WLAN, zwei USB-C-Anschlüssen und einem Li-Po-Ladegerät. Der S3 mit PSRAM ist der Referenzchip von ctrl32: ein Ladder-Programm in voller Programmgröße, seine Bedienseite in jedem Browser (WEBview), Modbus TCP und MQTT mit TLS - alles über WLAN.

**Geeignet für:**

- Eine WLAN-SPS mit Reserve - 512 Variablen, TLS zu einem Cloud-Broker
- Eine akkugepufferte Steuerung, die bei einem Stromausfall weiterläuft
- Entwicklung eines eigenen Boards auf dem ESP32-S3

Seite des Boards im Katalog: [Olimex ESP32-S3-DevKit-Lipo](https://ctrl32.com/hardware/boards/olimex-esp32-s3-devkit-lipo/)

![Olimex ESP32-S3-DevKit-Lipo - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | ESP32-S3 (ESP32-S3-WROOM-1-N8R8) |  |
| Speicher | 8 MB flash, 8 MB PSRAM |  |
| Programmgröße | 512 Variablen, 128 Alarme, 1024 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | 21 freie GPIO | siehe Pin-Belegung |
| Analogeingänge | 9 auf dem Chip (ADC1) | GPIO1, GPIO2, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 |
| Ethernet | nein |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - an freien Pins | braucht einen externen Transceiver |
| Modbus RTU (RS-485) | ja - an freien Pins | braucht einen externen Transceiver |
| Modbus TCP | Client und Server |  |
| MQTT | ja (auch TLS) | Home-Assistant-Discovery |
| WEBview | ja | die Bedienseite in jedem Browser |
| Display / Touch (HMI) | nein | die Bedienseite ist WEBview |
| USB | USB-C (CH340X USB-UART, Native USB) |  |
| Versorgung | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Was nicht unterstützt wird

- Bluetooth - der ESP32-S3 hat es, ctrl32 nutzt es nicht.
- Die Messeingänge für Akku und Versorgung (GPIO5 / GPIO6) sind in ctrl32 freie Pins, keine Akkuanzeige.

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
- [Olimex ESP32-DevKit-LiPo](../olimex-esp32-devkit-lipo/README.de.md) - die Variante mit dem klassischen ESP32

