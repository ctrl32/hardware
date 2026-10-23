---
title: Olimex ESP32-DevKit-LiPo
slug: olimex-esp32-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-devkit-lipo/
image: img/board-01.jpg
image_alt: Olimex ESP32-DevKit-LiPo board with its two pin headers and the micro-USB connector
tags:
- esp32
- wifi
- battery
- olimex
---

# Olimex ESP32-DevKit-LiPo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Olimex ESP32-DevKit-LiPo board with its two pin headers and the micro-USB connector](img/board-01.jpg)

The Olimex ESP32-DevKit-LiPo is an open-source ESP32 development board with Wi-Fi, all the module's GPIO on two headers and a Li-Po charger that keeps it running when the power fails. With ctrl32 it is a small Wi-Fi PLC: a ladder program on the chip, inputs and outputs on its pins, its operator page in any browser (WEBview), Modbus TCP and MQTT.

**Good for:**

- A Wi-Fi controller for a room, a greenhouse or a pump
- A battery-backed data logger that publishes over MQTT
- Learning ctrl32 on a breadboard

Board page in the catalog: [Olimex ESP32-DevKit-LiPo](https://ctrl32.com/hardware/boards/olimex-esp32-devkit-lipo/)

![Olimex ESP32-DevKit-LiPo pin map: the function of every GPIO in ctrl32](pinout/pinout.png)

## What ctrl32 can do on this board

<!-- capabilities:start -->
| Feature | On this board | Notes |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memory | 4 MB flash |  |
| Program size | 128 variables, 32 alarms, 128 blocks | checked by the editor before a download |
| Digital inputs / outputs | 19 free GPIO | 4 of them inputs only |
| Analog inputs | 6 on the chip (ADC1) | GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO39 |
| Ethernet | no |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 on the chip - not brought out on this board |  |
| Modbus RTU (RS-485) | no transceiver on the board |  |
| Modbus TCP | client and server |  |
| MQTT | yes | Home Assistant discovery |
| WEBview | yes | the operator page in any browser |
| Display / touch (HMI) | no | the operator page is WEBview |
| USB | Micro-USB (CH340 USB-UART) |  |
| Power | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### What is not supported

- Bluetooth - the ESP32 has it, ctrl32 does not use it.
- The battery and power sense inputs (GPIO35 / GPIO39) are free pins in ctrl32, not a battery gauge.

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
- [Olimex ESP32-S3-DevKit-Lipo](../olimex-esp32-s3-devkit-lipo/README.md) - the same idea with the ESP32-S3 and PSRAM

