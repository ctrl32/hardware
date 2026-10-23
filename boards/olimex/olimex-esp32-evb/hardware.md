---
title: 'Olimex ESP32-EVB: hardware and wiring'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-EVB pin map
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Hardware and wiring

## What you need

- The Olimex ESP32-EVB.
- A micro-USB data cable - for the first upload of the runtime.
- For power: a 5 V USB supply, or 5 V on the screw terminal.
- An Ethernet cable and a free port on your network.
- A PC with the [ctrl32 editor](https://ctrl32.com/download/) (Windows).
- Optional, for the all-in-one example: a potentiometer (10 k) between 3.3 V and GND with its wiper on GPIO36 (UEXT); a CAN node or a CAN adapter and two 120 ohm terminators.
- Optional: the Olimex MOD-LCD2.8RTP display (2.8 inch, 240 x 320, resistive touch) on the UEXT connector.

## Power

| Source | Where | Note |
|---|---|---|
| USB 5 V | the micro-USB connector | the road for the first upload |
| 5 V DC | the screw terminal | for a cabinet |
| Li-Po battery | the battery connector | charged on board |

!!! warning "The relays switch mains voltage"
    Wire the relay contacts only with the board unpowered, in an
    enclosure, by a person allowed to work on mains installations. The
    contacts take 10 A / 250 VAC; a motor or a heater above that needs a
    contactor driven by the relay.

## Pin map

![Olimex ESP32-EVB pin map](pinout/pinout.png)

| GPIO | Function in ctrl32 | Note |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ used by the board |
| 2 | TFT MOSI | ⚠ strapping pin |
| 2 | SPI MOSI | ⚠ strapping pin |
| 4 | free (UART TX line) |  |
| 5 | CAN TX |  |
| 6 | SPI flash of the module | ⚠ used by the board |
| 7 | SPI flash of the module | ⚠ used by the board |
| 8 | SPI flash of the module | ⚠ used by the board |
| 9 | SPI flash of the module | ⚠ used by the board |
| 10 | SPI flash of the module | ⚠ used by the board |
| 11 | SPI flash of the module | ⚠ used by the board |
| 13 | I2C SDA |  |
| 14 | TFT SCLK |  |
| 14 | SPI SCLK |  |
| 15 | TFT DC | ⚠ strapping pin |
| 15 | SPI MISO | ⚠ strapping pin |
| 16 | I2C SCL |  |
| 17 | TFT CS |  |
| 17 | free (SPI CS line) |  |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ used by the board |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ used by the board |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ used by the board |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ used by the board |
| 23 | Ethernet MDC (LAN8710A) | ⚠ used by the board |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ used by the board |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ used by the board |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ used by the board |
| 32 | free (REL1 line) | ADC1 |
| 33 | free (REL2 line) | ADC1 |
| 34 | free - the board's button | ⚠ input only, ADC1 |
| 35 | CAN RX |  |
| 36 | free (UART RX line) | ⚠ input only, ADC1 |

**Relays:** REL1 on GPIO32, REL2 on GPIO33. **Button:** BUT1 on GPIO34
(input only). **CAN:** the on-board transceiver on GPIO5 (TX) / GPIO35 (RX),
CAN_H / CAN_L on the terminal - terminate the bus with 120 ohm at both
ends. The **UEXT** connector carries I2C (GPIO13 / GPIO16), SPI and a free
UART (GPIO4 / GPIO36); the optional display uses its SPI lines.

## Safety

- The board is not intended for safety functions. An emergency stop, a
  door switch or a light curtain is wired in hardware, never through a
  program.
- The GPIO pins are 3.3 V. A 24 V signal needs an opto-coupler or a level
  shifter; a relay coil needs a driver (a relay module has one).

---

[← Overview](README.md) | [Overview](README.md) | [Install the runtime →](install.md)
