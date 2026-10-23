---
title: Olimex ESP32-S3-DevKit-Lipo
slug: olimex-esp32-s3-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-s3-devkit-lipo/
image: img/board-01.jpg
image_alt: Olimex ESP32-S3-DevKit-Lipo board with its two USB-C connectors and pin headers
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Olimex ESP32-S3-DevKit-Lipo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Olimex ESP32-S3-DevKit-Lipo board with its two USB-C connectors and pin headers](img/board-01.jpg)

The Olimex ESP32-S3-DevKit-Lipo is an open-source ESP32-S3 board with 8 MB of flash, 8 MB of PSRAM, Wi-Fi, two USB-C ports and a Li-Po charger. The S3 with PSRAM is the reference chip of ctrl32: a ladder program with the full program size, its operator page in any browser (WEBview), Modbus TCP and MQTT with TLS - all over Wi-Fi.

**Good for:**

- A Wi-Fi PLC with room to grow - 512 variables, TLS to a cloud broker
- A battery-backed controller that keeps running through a power cut
- Development of a board of your own on the ESP32-S3

Board page in the catalog: [Olimex ESP32-S3-DevKit-Lipo](https://ctrl32.com/hardware/boards/olimex-esp32-s3-devkit-lipo/)

![Olimex ESP32-S3-DevKit-Lipo pin map: the function of every GPIO in ctrl32](pinout/pinout.png)

## What ctrl32 can do on this board

<!-- capabilities:start -->
| Feature | On this board | Notes |
|---|---|---|
| Chip | ESP32-S3 (ESP32-S3-WROOM-1-N8R8) |  |
| Memory | 8 MB flash, 8 MB PSRAM |  |
| Program size | 512 variables, 128 alarms, 1024 blocks | checked by the editor before a download |
| Digital inputs / outputs | 21 free GPIO | see the pin map |
| Analog inputs | 9 on the chip (ADC1) | GPIO1, GPIO2, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 |
| Ethernet | no |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - on free pins | needs an external transceiver |
| Modbus RTU (RS-485) | yes - on free pins | needs an external transceiver |
| Modbus TCP | client and server |  |
| MQTT | yes (TLS too) | Home Assistant discovery |
| WEBview | yes | the operator page in any browser |
| Display / touch (HMI) | no | the operator page is WEBview |
| USB | USB-C (CH340X USB-UART, Native USB) |  |
| Power | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### What is not supported

- Bluetooth - the ESP32-S3 has it, ctrl32 does not use it.
- The battery and power sense inputs (GPIO5 / GPIO6) are free pins in ctrl32, not a battery gauge.

## The guide

| Step | Page |
|---|---|
| 1 | [Hardware and wiring](hardware.md) - what you need, power, the pin map |
| 2 | [Install the runtime](install.md) - the editor, the board, the first upload |
| 3 | [Configure](configure.md) - network, I/O, communication |
| 4 | [Example projects](examples/README.md) - everything the board does, ready to open |
| - | [Troubleshooting](troubleshooting.md) |

## Files

-

## Next steps

- [ctrl32 documentation](https://ctrl32.com/docs/) - the editor, the languages, every block
- [Download the editor](https://ctrl32.com/download/)
- [All tested boards](../../README.md)
- [Olimex ESP32-DevKit-LiPo](../olimex-esp32-devkit-lipo/README.md) - the classic ESP32 version

