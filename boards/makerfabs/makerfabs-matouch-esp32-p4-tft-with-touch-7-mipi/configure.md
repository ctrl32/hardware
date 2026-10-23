---
title: Configure the Makerfabs MaTouch ESP32-P4 7" in the ctrl32 editor
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: The board page of the Makerfabs MaTouch ESP32-P4 7" in the editor
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Configure the board

## The board page

Double-click the board in the device tree. The page shows what the board carries and every pin: a free pin gets a variable in one click - an input, an output, or on an analog-capable pin an analog input.

![The board page: the free pins and what each can do](img/configure-01-board.png)

## Network

The Ethernet port starts by itself and takes its address from your router
(DHCP). The Wi-Fi of the ESP32-C6 is set on the **WiFi** page of the device
tree - the network name and the password. A fixed address is set on the
board page, in its **Network** section.


## Inputs, outputs and variables

Every signal of the program is a **variable**. A variable on a pin reads or drives the pin; an analog variable says what is wired to it (a voltage, 4-20 mA, a thermistor) and its range in units.

![The variables of the all-in-one example](img/configure-03-variables.png)

## Communication

**Modbus TCP.** A device on the network is added under **Ethernet → Modbus TCP master**; its registers become variables.

**Modbus RTU / RS-485.** The board has no RS-485 transceiver: put a 3.3 V transceiver module on free pins (TX, RX and the direction pin DE) and name them on the board page - the example uses GPIO4 / GPIO5 / GPIO32. ctrl32 is then a Modbus RTU master or slave on that line.

**CAN.** The ESP32-P4 has one CAN controller (TWAI). The board has no CAN transceiver: put a 3.3 V transceiver module on two free pins and name them on the board page (Bus pins) - the example uses GPIO20 / GPIO21. CANopen devices, raw CAN frames and the vehicle buses (J1939) all run on it.

**MQTT.** The board publishes chosen variables to a broker; in the Home Assistant mode the broker finds them by itself, and a variable marked *write* can be set from there.

![The MQTT page: the broker and the published variables](img/configure-05-mqtt.png)

## Display and touch

The project is drawn at the glass's own 1024 x 600. The HMIview page sets
the orientation (as mounted, or turned - the touch follows), the size of
the WEBview canvas and the boot splash. Touch needs no setup: the GT911
controller is part of the board.

![The HMIview settings: the screen the project draws on](img/configure-04-display.png)

## WEBview

The board serves its operator page to any browser on the network - open the board's address. The page is drawn in the editor like a screen.

![The WEBview page settings](img/configure-06-webview.png)

---

[← Install the runtime](install.md) | [Overview](README.md) | [Example projects →](examples/README.md)
