---
title: LaskaKit ESPlan
slug: laskakit-esplan
sidebar_position: 10
hardware: /hardware/boards/laskakit-esplan/
image: img/board-01.jpg
image_alt: LaskaKit ESPlan board with the Ethernet jack, the RS-485 terminal and the power terminal
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# LaskaKit ESPlan

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![LaskaKit ESPlan board with the Ethernet jack, the RS-485 terminal and the power terminal](img/board-01.jpg)

The LaskaKit ESPlan is an industrial ESP32 board: 10/100 Ethernet, an RS-485 interface with protection and switchable termination, Wi-Fi, and a wide 7-40 V supply on a screw terminal (or PoE with an add-on module). With ctrl32 it is a Modbus RTU master or slave in a cabinet - a ladder program on the chip, RS-485 devices read and written, the values on Modbus TCP, MQTT and its operator page (WEBview).

**Good for:**

- A Modbus RTU master for meters, sensors and drives, on a 24 V supply
- A Modbus RTU / TCP gateway with its own logic
- Building automation in a cabinet

Board page in the catalog: [LaskaKit ESPlan](https://ctrl32.com/hardware/boards/laskakit-esplan/)

![LaskaKit ESPlan pin map: the function of every GPIO in ctrl32](pinout/pinout.png)

## What ctrl32 can do on this board

<!-- capabilities:start -->
| Feature | On this board | Notes |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memory | 4 MB flash |  |
| Program size | 128 variables, 32 alarms, 128 blocks | checked by the editor before a download |
| Digital inputs / outputs | 5 free GPIO | 2 of them inputs only |
| Analog inputs | 2 on the chip (ADC1) | GPIO35, GPIO39 |
| Ethernet | yes - LAN8720A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - on free pins | needs an external transceiver |
| Modbus RTU (RS-485) | yes |  |
| Modbus TCP | client and server |  |
| MQTT | yes | Home Assistant discovery |
| WEBview | yes | the operator page in any browser |
| Display / touch (HMI) | no | the operator page is WEBview |
| USB | USB-C (CH9102 USB-UART) |  |
| Power | 5 V USB, PoE |  |
<!-- capabilities:end -->

### What is not supported

- Bluetooth - the ESP32 has it, ctrl32 does not use it.
- The microSD slot - ctrl32 keeps the program and the screens in the chip's own flash.

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

