---
title: 'Olimex ESP32-P4-DevKit: hardware and wiring'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-DevKit pin map
tags:
- esp32-p4
- ethernet
- olimex
---

# Hardware and wiring

## What you need

- The Olimex ESP32-P4-DevKit.
- A USB-C data cable - for the upload and for power (5 V).
- An Ethernet cable and a free port on your network.
- A PC with the [ctrl32 editor](https://ctrl32.com/download/) (Windows).
- Optional, for the all-in-one example: the LED (GPIO2) is on the board; a push-button from GPIO20 to GND; a 3.3 V CAN transceiver on GPIO5 / GPIO21 and an RS-485 transceiver on GPIO22 / GPIO23 / GPIO32 (DE).

## Power

| Source | Where | Note |
|---|---|---|
| USB 5 V | the USB-C connector | power, programming and debugging |
| PoE | through the PoE extension | optional |

## Pin map

![Olimex ESP32-P4-DevKit pin map](pinout/pinout.png)

| GPIO | Function in ctrl32 | Note |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 7 | I2C SDA |  |
| 8 | I2C SCL |  |
| 20 | free I/O |  |
| 21 | free I/O |  |
| 22 | free I/O |  |
| 23 | free I/O |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ used by the board |
| 29 | Ethernet RMII (IP101GRI) | ⚠ used by the board |
| 30 | Ethernet RMII (IP101GRI) | ⚠ used by the board |
| 31 | Ethernet MDC (IP101GRI) | ⚠ used by the board |
| 32 | free I/O |  |
| 33 | free I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ used by the board |
| 35 | Ethernet RMII (IP101GRI) | ⚠ used by the board |
| 46 | free I/O |  |
| 47 | free I/O |  |
| 48 | free I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ used by the board |
| 50 | Ethernet RMII (IP101GRI) | ⚠ used by the board |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ used by the board |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ used by the board |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

All GPIO are on the two 20-pin headers. The ESP32-P4 has no analog input
that ctrl32 uses: analog signals go through an I2C ADC (an ADS1115 on the
pUEXT connector, I2C GPIO7 / GPIO8) or a Modbus module.

## Safety

- The board is not intended for safety functions. An emergency stop, a
  door switch or a light curtain is wired in hardware, never through a
  program.
- The GPIO pins are 3.3 V. A 24 V signal needs an opto-coupler or a level
  shifter; a relay coil needs a driver (a relay module has one).

---

[← Overview](README.md) | [Overview](README.md) | [Install the runtime →](install.md)
