---
title: Configure the Olimex ESP32-EVB in the ctrl32 editor
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: The board page of the Olimex ESP32-EVB in the editor
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Configure the board

## The board page

Double-click the board in the device tree. The page shows what the board carries and every pin: a free pin gets a variable in one click - an input, an output, or on an analog-capable pin an analog input.

![The board page: the free pins and what each can do](img/configure-01-board.png)

## Network

The Ethernet port starts by itself and takes its address from your router
(DHCP). A fixed address is set on the board page, in its **Network**
section; Wi-Fi on the **WiFi** page of the device tree.


## Inputs, outputs and variables

Every signal of the program is a **variable**. A variable on a pin reads or drives the pin; an analog variable says what is wired to it (a voltage, 4-20 mA, a thermistor) and its range in units.

![The variables of the all-in-one example](img/configure-03-variables.png)

## Communication

**Modbus TCP.** A device on the network is added under **Ethernet → Modbus TCP master**; its registers become variables.

**Modbus RTU / RS-485.** The board has no RS-485 transceiver: put a 3.3 V transceiver module on free pins (TX, RX and the direction pin DE) and name them on the board page (Bus pins) - ctrl32 is then a Modbus RTU master or slave on that line. Modbus TCP devices on the network need nothing.

**CAN.** The ESP32 has one CAN controller (TWAI) and this board carries its transceiver: CAN_H / CAN_L on the terminal, GPIO5 / GPIO35. CANopen devices (a drive, I/O nodes), raw CAN frames and the vehicle buses (J1939) all run on it.

**MQTT.** The board publishes chosen variables to a broker; in the Home Assistant mode the broker finds them by itself, and a variable marked *write* can be set from there.

![The MQTT page: the broker and the published variables](img/configure-05-mqtt.png)

## Display and touch

With the MOD-LCD2.8RTP on the UEXT connector the project can carry screens
(240 x 320, portrait or turned). The board has no PSRAM: with the display
lit the runtime keeps its memory for the screen and runs the network on
Ethernet only (no Wi-Fi, no MQTT). The all-in-one example has no screen for
that reason; WEBview runs either way.

![The HMIview settings: the screen the project draws on](img/configure-04-display.png)

## WEBview

The board serves its operator page to any browser on the network - open the board's address. The page is drawn in the editor like a screen.

![The WEBview page settings](img/configure-06-webview.png)

---

[← Install the runtime](install.md) | [Overview](README.md) | [Example projects →](examples/README.md)
