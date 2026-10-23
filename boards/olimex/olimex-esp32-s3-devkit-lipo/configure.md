---
title: Configure the Olimex ESP32-S3-DevKit-Lipo in the ctrl32 editor
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: The board page of the Olimex ESP32-S3-DevKit-Lipo in the editor
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Configure the board

## The board page

Double-click the board in the device tree. The page shows what the board carries and every pin: a free pin gets a variable in one click - an input, an output, or on an analog-capable pin an analog input.

![The board page: the free pins and what each can do](img/configure-01-board.png)

## Network

The board joins your Wi-Fi: open the **WiFi** page of the device tree and
type the network's name and password (the example carries placeholders).
It takes its address from the router (DHCP); a fixed address is set on the
board page, in its **Network** section.


## Inputs, outputs and variables

Every signal of the program is a **variable**. A variable on a pin reads or drives the pin; an analog variable says what is wired to it (a voltage, 4-20 mA, a thermistor) and its range in units.

![The variables of the all-in-one example](img/configure-03-variables.png)

## Communication

**Modbus TCP.** A device on the network is added under **Ethernet → Modbus TCP master**; its registers become variables.

**Modbus RTU / RS-485.** There is no RS-485 transceiver on the board. Modbus devices are reached over Modbus TCP on the Wi-Fi.

**CAN.** The ESP32-S3 has one CAN controller (TWAI), but this board does not bring it out to a transceiver, so ctrl32 does not offer CAN here.

**MQTT.** The board publishes chosen variables to a broker; in the Home Assistant mode the broker finds them by itself, and a variable marked *write* can be set from there.

![The MQTT page: the broker and the published variables](img/configure-05-mqtt.png)

## WEBview

The board serves its operator page to any browser on the network - open the board's address. The page is drawn in the editor like a screen.

![The WEBview page settings](img/configure-06-webview.png)

---

[← Install the runtime](install.md) | [Overview](README.md) | [Example projects →](examples/README.md)
