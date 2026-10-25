---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Board Olimex ESP32-P4-PC mit der Ethernet-Buchse, den USB-Ports und dem HDMI-Anschluss
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Board Olimex ESP32-P4-PC mit der Ethernet-Buchse, den USB-Ports und dem HDMI-Anschluss](img/board-01.jpg)

Der Olimex ESP32-P4-PC ist ein kleiner Rechner auf dem ESP32-P4 - zwei Kerne mit 400 MHz und 32 MB PSRAM - mit 100-Mbit-Ethernet, vier USB-Host-Ports, HDMI, Audio und einem Li-Po-Akku, der ihn bei einem Stromausfall weiterlaufen lässt. Mit ctrl32 ist er eine kabelgebundene Steuerung mit dem größten Programm, das ein ESP32 ausführt - 4096 Variablen - mit der Bedienseite in jedem Browser (WEBview), Modbus TCP, MQTT mit TLS und CAN oder RS-485 auf den freien Pins seiner Stiftleiste.

**Geeignet für:**

- Eine kabelgebundene SPS, die einen Stromausfall mit eigenem Akku überbrückt
- Ein Gateway mit umfangreicher Logik zwischen Modbus TCP, CAN und MQTT
- Eine Steuerung im Gehäuse, versorgt über PoE (mit der Erweiterung)

Seite des Boards im Katalog: [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | ESP32-P4 (ESP32-P4NRW32) |  |
| Speicher | 16 MB flash, 32 MB PSRAM |  |
| Programmgröße | 4096 Variablen, 512 Alarme, 1024 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | 15 freie GPIO | siehe Pin-Belegung |
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
| Versorgung | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Was nicht unterstützt wird

- Der HDMI-Ausgang und die MIPI-DSI- / CSI-Steckverbinder - dieses Board läuft in ctrl32 ohne Display (die Bedienseite ist WEBview).
- Die USB-Host-Ports und der Audioausgang.
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

| Datei | Was |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | die Pin-Belegung, als Vektorgrafik (auch als [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | woher die Fotos, Schaltpläne und Modelle stammen |

## Weiter

- [ctrl32-Dokumentation](https://ctrl32.com/docs/) - der Editor, die Sprachen, jeder Baustein
- [Editor herunterladen](https://ctrl32.com/download/)
- [Alle getesteten Boards](../../README.de.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.de.md) - derselbe ESP32-P4 auf einem kleineren Board

