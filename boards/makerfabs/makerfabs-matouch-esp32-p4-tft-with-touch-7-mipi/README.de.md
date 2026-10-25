---
title: Makerfabs MaTouch ESP32-P4 7"
slug: makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/board-01.jpg
image_alt: Board Makerfabs MaTouch ESP32-P4 7" mit seinem Touch-Display 1024x600
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Makerfabs MaTouch ESP32-P4 7"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 1024x600](https://img.shields.io/badge/HMI-1024x600-0891b2)

![Board Makerfabs MaTouch ESP32-P4 7" mit seinem Touch-Display 1024x600](img/board-01.jpg)

Das Makerfabs MaTouch ESP32-P4 7" ist ein komplettes Touch-Panel auf einem Board: ein MIPI-Display mit 1024 x 600 und kapazitivem Touch, der Zweikern-ESP32-P4 mit 32 MB PSRAM, Ethernet und Wi-Fi 6 über einen ESP32-C6. Mit ctrl32 ist es HMI und SPS in einem - im Editor gezeichnete Bildschirme laufen auf dem Glas, daneben läuft ein Ladder-Programm, und dieselben Werte erreichen jeden Browser (WEBview), Modbus-Geräte, CAN und MQTT.

**Geeignet für:**

- Ein Bedienpanel an einer Maschine, mit eigener Logik
- Ein Smart-Home- oder Gebäudesteuerungspanel an der Wand
- Ein Modbus-/CAN-Gateway mit Bildschirm

Seite des Boards im Katalog: [Makerfabs MaTouch ESP32-P4 7"](https://ctrl32.com/hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/)

![Makerfabs MaTouch ESP32-P4 7" - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | ESP32-P4 (ESP32-P4NRW32) |  |
| Speicher | 16 MB flash, 32 MB PSRAM |  |
| Programmgröße | 4096 Variablen, 512 Alarme, 512 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | 12 freie GPIO | siehe Pin-Belegung |
| Analogeingänge | über einen I2C-ADC (ADS1115) |  |
| Ethernet | ja - IP101GRI |  |
| Wi-Fi | Wi-Fi 6 (2.4 GHz) |  |
| CAN (TWAI) | 1 | braucht einen externen Transceiver |
| Modbus RTU (RS-485) | ja | an freien Pins, braucht einen externen Transceiver |
| Modbus TCP | Client und Server |  |
| MQTT | ja (auch TLS) | Home-Assistant-Discovery |
| WEBview | ja | die Bedienseite in jedem Browser |
| Display / Touch (HMI) | 7" 1024x600, GT911 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Versorgung | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Was nicht unterstützt wird

- Die Kamera (SC2336 an MIPI CSI) - ctrl32 führt Bildverarbeitung nur auf der 64-Bit-Linux-Runtime aus.
- Der Audio-Codec, das Mikrofon und der Lautsprecherausgang.
- Bluetooth des ESP32-C6.
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
| [makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf](schematics/makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf) | MaTouch ESP32-P4 TFT with Touch 7“ V1.2 |
| [makerfabs-matouch-p4-7-display-datasheet.pdf](datasheets/makerfabs-matouch-p4-7-display-datasheet.pdf) | 7" 1024x600 MIPI display AML070JGI50 datasheet |
| [makerfabs-matouch-p4-es8311-datasheet.pdf](datasheets/makerfabs-matouch-p4-es8311-datasheet.pdf) | ES8311 audio codec datasheet |
| [esp32-p4-datasheet.pdf](datasheets/esp32-p4-datasheet.pdf) | ESP32-P4 datasheet (pre-release) |
| [makerfabs-matouch-p4-sc2336-camera-datasheet.pdf](datasheets/makerfabs-matouch-p4-sc2336-camera-datasheet.pdf) | SC2336 2 MP MIPI camera module datasheet |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | woher die Fotos, Schaltpläne und Modelle stammen |

## Weiter

- [ctrl32-Dokumentation](https://ctrl32.com/docs/) - der Editor, die Sprachen, jeder Baustein
- [Editor herunterladen](https://ctrl32.com/download/)
- [Alle getesteten Boards](../../README.de.md)
- Makerfabs MaTouch Lite ESP32-S3 3.95" - das kleine Geschwister
- [Smart-Home-Steuerpanel auf dem MaTouch ESP32-P4](https://ctrl32.com/examples/smart-home-control-panel-on-an-esp32-p4-7-touch-display/) - ein vollständiges Beispiel im Web

