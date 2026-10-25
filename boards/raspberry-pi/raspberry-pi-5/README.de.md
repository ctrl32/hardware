---
title: Raspberry Pi 5
slug: raspberry-pi-5
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-5/
image: img/board-01.jpg
image_alt: Board Raspberry Pi 5 von oben
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Raspberry Pi 5

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Board Raspberry Pi 5 von oben](img/board-01.jpg)

Der Raspberry Pi 5 betreibt die ctrl32 Linux-Runtime - das größte Ziel von ctrl32: Zehntausende Variablen, ein HMI am HDMI-Monitor, ein OPC-UA-Server für SCADA, Antriebe an EtherCAT, CAN und RS-485 über HATs oder USB-Adapter und Bildverarbeitung mit einer Kamera. Der Editor installiert die Runtime über das Netzwerk; der Pi startet sie danach bei jedem Hochfahren.

**Geeignet für:**

- Eine Liniensteuerung mit HMI am HDMI-Monitor und OPC UA zum SCADA
- Ein EtherCAT-Master für Servoantriebe
- Ein Gateway zwischen Modbus, CAN, OPC UA und MQTT

Seite des Boards im Katalog: [Raspberry Pi 5](https://ctrl32.com/hardware/boards/raspberry-pi-5/)

![Raspberry Pi 5 - Pin-Belegung: die Funktion jedes GPIO in ctrl32](pinout/pinout.png)

## Was ctrl32 auf diesem Board kann

<!-- capabilities:start -->
| Merkmal | Auf diesem Board | Hinweise |
|---|---|---|
| Chip | Linux |  |
| Programmgröße | 20480 Variablen, 4096 Alarme, 40960 Bausteine | der Editor prüft es vor dem Download |
| Digitale Ein-/Ausgänge | über E/A-Module | Modbus, CANopen, EtherCAT |
| Ethernet | ja |  |
| Wi-Fi | Wi-Fi 5 (2.4 + 5 GHz) |  |
| CAN | über ein CAN-HAT oder einen USB-Adapter | SocketCAN, bis zu 4 Busse |
| Modbus RTU (RS-485) | ja | ein USB-Adapter oder ein HAT |
| Modbus TCP | Client und Server |  |
| MQTT | ja (auch TLS) | Home-Assistant-Discovery |
| WEBview | ja | die Bedienseite in jedem Browser |
| OPC-UA-Server | ja |  |
| EtherCAT master | ja | an einem zweiten Ethernet-Port |
| Display (HMI) | HDMI oder ein DSI-Panel | oder ohne Display mit WEBview |
| USB | USB-C |  |
| Versorgung | USB-C PD 5 V / 5 A |  |
<!-- capabilities:end -->

### Was nicht unterstützt wird

- Die 40-polige GPIO-Stiftleiste als Ein- und Ausgänge des Programms - Ein- und Ausgänge laufen über I/O-Module (Modbus RTU / TCP, CANopen, EtherCAT); die Stiftleiste trägt die Busse der HATs.
- Bluetooth.
- Eine Desktop-Umgebung - die Runtime zeichnet den Bildschirm selbst; das System, das sie erwartet, ist Raspberry Pi OS Lite.

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
| [raspberry-pi-5-mechanical-drawing.pdf](datasheets/raspberry-pi-5-mechanical-drawing.pdf) | Raspberry Pi 5 mechanical drawing |
| [raspberry-pi-5-rp1-peripherals.pdf](datasheets/raspberry-pi-5-rp1-peripherals.pdf) | RP1 peripherals |
| [raspberry-pi-5-3d.zip](3d/raspberry-pi-5-3d.zip) | 3D-Modell (GLB, als Zip) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | woher die Fotos, Schaltpläne und Modelle stammen |

## Weiter

- [ctrl32-Dokumentation](https://ctrl32.com/docs/) - der Editor, die Sprachen, jeder Baustein
- [Editor herunterladen](https://ctrl32.com/download/)
- [Alle getesteten Boards](../../README.de.md)
- Raspberry Pi 4 Model B
- Raspberry Pi 3 Model B+
- [Die Linux-Runtime](https://ctrl32.com/docs/linux-runtime/) - was sie leistet und ihre Grenzen

