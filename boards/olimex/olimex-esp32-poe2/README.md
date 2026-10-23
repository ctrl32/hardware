---
title: Olimex ESP32-POE2
slug: olimex-esp32-poe2
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe2/
image: img/board-01.jpg
image_alt: Olimex ESP32-POE2 board with the Ethernet jack and the power outputs
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Olimex ESP32-POE2

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Olimex ESP32-POE2 board with the Ethernet jack and the power outputs](img/board-01.jpg)

The Olimex ESP32-POE2 is the next generation of the ESP32-PoE: an ESP32 with 8 MB of PSRAM, Ethernet and IEEE 802.3at Power over Ethernet that also powers your field devices - 24 V or 12 V, 5 V and 3.3 V outputs, up to 25 W from the network cable. With ctrl32 it is a PLC in a cabinet fed by one cable: ladder logic, WEBview, Modbus TCP and MQTT, with the full program size of a classic ESP32 with PSRAM.

**Good for:**

- A cabinet PLC that powers its sensors and a small relay module from PoE
- A Modbus TCP gateway with MQTT to Home Assistant
- Building automation on one cable per room

Board page in the catalog: [Olimex ESP32-POE2](https://ctrl32.com/hardware/boards/olimex-esp32-poe2/)

![Olimex ESP32-POE2 pin map: the function of every GPIO in ctrl32](pinout/pinout.png)

## What ctrl32 can do on this board

<!-- capabilities:start -->
| Feature | On this board | Notes |
|---|---|---|
| Chip | ESP32 (ESP32-WROVER-E-N4R8) |  |
| Memory | 4 MB flash, 8 MB PSRAM |  |
| Program size | 512 variables, 128 alarms, 1024 blocks | checked by the editor before a download |
| Digital inputs / outputs | 5 free GPIO | 3 of them inputs only |
| Analog inputs | 3 on the chip (ADC1) | GPIO34, GPIO36, GPIO39 |
| Ethernet | yes - LAN8710A |  |
| Power over Ethernet | IEEE 802.3at |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 on the chip - not brought out on this board |  |
| Modbus RTU (RS-485) | no transceiver on the board |  |
| Modbus TCP | client and server |  |
| MQTT | yes | Home Assistant discovery |
| WEBview | yes | the operator page in any browser |
| Display / touch (HMI) | no | the operator page is WEBview |
| USB | USB-C |  |
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

-

## Next steps

- [ctrl32 documentation](https://ctrl32.com/docs/) - the editor, the languages, every block
- [Download the editor](https://ctrl32.com/download/)
- [All tested boards](../../README.md)
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.md) - the first generation
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.md) - with an isolated PoE supply

