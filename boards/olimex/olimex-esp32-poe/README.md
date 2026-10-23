---
title: Olimex ESP32-PoE
slug: olimex-esp32-poe
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/board-01.jpg
image_alt: Olimex ESP32-PoE board, top view, with the Ethernet jack and the USB connector
tags:
- esp32
- ethernet
- poe
- olimex
---

# Olimex ESP32-PoE

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Olimex ESP32-PoE board, top view, with the Ethernet jack and the USB connector](img/board-01.jpg)

The Olimex ESP32-PoE is an open-source ESP32 board with Ethernet and Power over Ethernet: one network cable powers it and carries its link. With ctrl32 it becomes a compact PLC for a cabinet or a wall box - a ladder program on the chip, its operator page served to any browser on the network (WEBview), Modbus TCP to meters and I/O modules, and MQTT to Home Assistant or any broker.

**Good for:**

- A small PLC in a cabinet, powered from a PoE switch
- A Modbus TCP gateway that reads meters and publishes them over MQTT
- Home automation - a room or a boiler room on one cable

Board page in the catalog: [Olimex ESP32-PoE](https://ctrl32.com/hardware/boards/olimex-esp32-poe/)

![Olimex ESP32-PoE pin map: the function of every GPIO in ctrl32](pinout/pinout.png)

## What ctrl32 can do on this board

<!-- capabilities:start -->
| Feature | On this board | Notes |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memory | 4 MB flash |  |
| Program size | 128 variables, 32 alarms, 128 blocks | checked by the editor before a download |
| Digital inputs / outputs | 6 free GPIO | 3 of them inputs only |
| Analog inputs | 4 on the chip (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | yes - LAN8710A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - on free pins | needs an external transceiver |
| Modbus RTU (RS-485) | yes - on free pins | needs an external transceiver |
| Modbus TCP | client and server |  |
| MQTT | yes | Home Assistant discovery |
| WEBview | yes | the operator page in any browser |
| Display / touch (HMI) | no | the operator page is WEBview |
| USB | Micro-USB (CH340T USB-UART) |  |
| Power | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### What is not supported

- Bluetooth - the ESP32 has it, ctrl32 does not use it.
- The microSD slot - ctrl32 keeps the program and the screens in the chip's own flash.
- The battery input works as the board's own feature; ctrl32 does not read the battery level.

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
| [olimex-esp32-poe-schematic.pdf](schematics/olimex-esp32-poe-schematic.pdf) | ESP32-PoE schematic Rev M2 |
| [esp32-poe-revm2.zip](schematics/esp32-poe-revm2.zip) | KiCad project |
| [olimex-esp32-poe-user-manual.pdf](datasheets/olimex-esp32-poe-user-manual.pdf) | ESP32-PoE user manual |
| [olimex-esp32-poe.zip](3d/olimex-esp32-poe.zip) | 3D model (STEP, zipped) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | where the photos, schematics and models come from |

## Next steps

- [ctrl32 documentation](https://ctrl32.com/docs/) - the editor, the languages, every block
- [Download the editor](https://ctrl32.com/download/)
- [All tested boards](../../README.md)
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.md) - the same board with an isolated PoE supply
- [Olimex ESP32-POE2](../olimex-esp32-poe2/README.md) - the next generation

