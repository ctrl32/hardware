---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Olimex ESP32-P4-PC board with the Ethernet jack, the USB ports and the HDMI connector
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Olimex ESP32-P4-PC board with the Ethernet jack, the USB ports and the HDMI connector](img/board-01.jpg)

The Olimex ESP32-P4-PC is a small computer on the ESP32-P4 - dual-core 400 MHz with 32 MB of PSRAM - with 100 Mb Ethernet, four USB hosts, HDMI, audio and a Li-Po battery that keeps it running through a power cut. With ctrl32 it is a wired controller with the largest program an ESP32 runs - 4096 variables - its operator page in any browser (WEBview), Modbus TCP, MQTT with TLS, and CAN or RS-485 on the free pins of its header.

**Good for:**

- A wired PLC that rides through a power cut on its own battery
- A gateway with heavy logic between Modbus TCP, CAN and MQTT
- A controller in an enclosure, powered from PoE (with the extension)

Board page in the catalog: [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC pin map: the function of every GPIO in ctrl32](pinout/pinout.png)

## What ctrl32 can do on this board

<!-- capabilities:start -->
| Feature | On this board | Notes |
|---|---|---|
| Chip | ESP32-P4 (ESP32-P4NRW32) |  |
| Memory | 16 MB flash, 32 MB PSRAM |  |
| Program size | 4096 variables, 512 alarms, 1024 blocks | checked by the editor before a download |
| Digital inputs / outputs | 15 free GPIO | see the pin map |
| Analog inputs | through an I2C ADC (ADS1115) |  |
| Ethernet | yes - IP101GRI |  |
| Wi-Fi | no |  |
| CAN (TWAI) | 1 - on free pins | needs an external transceiver |
| Modbus RTU (RS-485) | yes - on free pins | needs an external transceiver |
| Modbus TCP | client and server |  |
| MQTT | yes (TLS too) | Home Assistant discovery |
| WEBview | yes | the operator page in any browser |
| Display / touch (HMI) | no | the operator page is WEBview |
| USB | USB-C (Native USB) |  |
| Power | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### What is not supported

- The HDMI output and the MIPI DSI / CSI connectors - this board runs headless in ctrl32 (the operator page is WEBview).
- The USB host ports and the audio output.
- The microSD slot - ctrl32 keeps the program and the screens in the board's flash.

## The guide

| Step | Page |
|---|---|
| 1 | [Hardware and wiring](hardware.md) - what you need, power, the pin map |
| 2 | [Install the runtime](install.md) - the editor, the board, the first upload |
| 3 | [Configure](configure.md) - network, I/O, communication |
| 4 | [Example projects](examples/README.md) - everything the board does, ready to open |
| - | [Troubleshooting](troubleshooting.md) |

## Files

| File | What |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | the pin map, vector (also [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | where the photos, schematics and models come from |

## Next steps

- [ctrl32 documentation](https://ctrl32.com/docs/) - the editor, the languages, every block
- [Download the editor](https://ctrl32.com/download/)
- [All tested boards](../../README.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.md) - the same ESP32-P4 on a smaller board

