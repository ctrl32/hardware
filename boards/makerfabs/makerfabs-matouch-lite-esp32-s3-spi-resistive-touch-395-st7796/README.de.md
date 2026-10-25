---
title: Makerfabs MaTouch Lite ESP32-S3 3.95"
slug: makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/
image: img/board-01.jpg
image_alt: Board Makerfabs MaTouch Lite ESP32-S3 mit seinem 3,95-Zoll-Touch-Display
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Makerfabs MaTouch Lite ESP32-S3 3.95"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 320x480](https://img.shields.io/badge/HMI-320x480-0891b2)

![Board Makerfabs MaTouch Lite ESP32-S3 mit seinem 3,95-Zoll-Touch-Display](img/board-01.jpg)

Das Makerfabs MaTouch Lite ist ein günstiges Touch-Panel: ein 3,95"-Display mit 320 x 480 und resistivem Touch auf einem ESP32-S3 mit PSRAM und WLAN. Mit ctrl32 ist es HMI und SPS in einem - im Editor gezeichnete Bildschirme auf dem Glas, daneben ein Ladder-Programm, dieselben Werte in jedem Browser (WEBview), Modbus TCP, CAN und MQTT. Der resistive Touch funktioniert auch mit Handschuhen.

**Geeignet für:**

- Ein kleines Bedienpanel an einer Maschine, mit Handschuhen bedient
- Ein Wandthermostat oder ein Raumregler
- Ein CAN-Display für ein Fahrzeug oder einen Frequenzumrichter

Seite des Boards im Katalog: [Makerfabs MaTouch Lite ESP32-S3 3.95"](https://ctrl32.com/hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/)

![Makerfabs MaTouch Lite ESP32-S3 3.95" - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | ESP32-S3 (esp32s3_wroom_1_n16r8) |  |
| Speicher | 16 MB flash, 8 MB PSRAM |  |
| Programmgröße | 512 Variablen, 128 Alarme, 512 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | 4 freie GPIO | siehe Pin-Belegung |
| Analogeingänge | 4 auf dem Chip (ADC1) | GPIO4, GPIO5, GPIO6, GPIO7 |
| Ethernet | nein |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 | braucht einen externen Transceiver |
| Modbus RTU (RS-485) | ja | an freien Pins, braucht einen externen Transceiver |
| Modbus TCP | Client und Server |  |
| MQTT | ja (auch TLS) | Home-Assistant-Discovery |
| WEBview | ja | die Bedienseite in jedem Browser |
| Display / Touch (HMI) | 3.95" 320x480, NS2009 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Versorgung | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Was nicht unterstützt wird

- Bluetooth.
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
- [Makerfabs MaTouch ESP32-P4 7"](../makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.de.md) - das große Geschwister

