---
title: A(z) Raspberry Pi 3 Model B+ beállítása a ctrl32 szerkesztőben
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: A(z) Raspberry Pi 3 Model B+ panel oldala a szerkesztőben
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# A panel beállítása

## A panel oldala

Kattints duplán a panelre az eszközfában. Az oldal megmutatja, mi van a panelen, és minden lábat: egy szabad láb egy kattintással kap változót - bemenetet, kimenetet, vagy analógképes lábon analóg bemenetet.

![A panel oldala: a szabad lábak, és mire képes mindegyik](img/configure-01-board.png)

## Hálózat

A Pi megtartja az operációs rendszere hálózati beállításait: DHCP a
routertől, hacsak a **Prepare a Linux device** nem állított be fix címet.
A hosztnevéről vagy a szerkesztő **Find devices** funkciójával találod meg.


## Bemenetek, kimenetek és változók

A program minden jele egy **változó**. Egy lábhoz rendelt változó olvassa vagy vezérli a lábat; egy analóg változó megmondja, mi van rákötve (feszültség, 4-20 mA, termisztor), és mi a tartománya mértékegységben.

![Az all-in-one példa változói](img/configure-03-variables.png)

## Kommunikáció

**Modbus TCP.** A hálózat egy eszközét az **Ethernet → Modbus TCP master** alatt adod hozzá; a regiszterei változókká válnak.

**Modbus RTU / RS-485.** Egy USB-RS485 adapter (`/dev/ttyUSB0`, az irányt magától váltja) vagy egy RS-485 HAT a Pi UART-ján. A ctrl32 rajta Modbus RTU master vagy slave, akár négy vonalon.

**CAN.** A CAN egy SPI-re kötött CAN HAT-ról (MCP2515, MCP251xFD) vagy egy USB CAN adapterről jön; a runtime SocketCAN interfészként használja (`can0`, akár négy busz). A Prepare a Linux device hozzáadja a HAT illesztőprogramját; a bitsebesség a projekté.

**MQTT.** A panel a kiválasztott változókat egy brókernek teszi közzé; Home Assistant módban a bróker magától megtalálja őket, és egy *write* jelölésű változó onnan is beállítható.

![Az MQTT oldal: a bróker és a közzétett változók](img/configure-05-mqtt.png)

## Kijelző

A runtime a csatlakoztatott HDMI monitorra (vagy egy DSI kijelzőre) rajzol,
és a projektet hozzá méretezi; a példa 1280 x 720-ra van rajzolva. Egy
érintőmonitor USB-s érintése illesztőprogram nélkül működik. Monitor
nélkül a Pi a képernyőit csak böngészőknek szolgálja ki (WEBview).

![A HMIview beállításai: a képernyő, amelyre a projekt rajzol](img/configure-04-display.png)

## OPC UA és EtherCAT

- **OPC UA** - a projekt minden változója a Pi saját szerverének egy
  csomópontja (`opc.tcp://<cím>:4840`, `ns=1;s=<név>`); egy változót egy
  pipával a változólistában távol tarthatsz tőle. Mást nem kell beállítani.
- **EtherCAT** - master egy USB Ethernet adapteren I/O terminálokhoz;
  rövid buszciklusú szervohajtásokhoz a Raspberry Pi 4 vagy 5 a jobb
  választás.

## WEBview

A panel a kezelőoldalát a hálózat bármely böngészőjének kiszolgálja - nyisd meg a panel címét. Az oldalt a szerkesztőben úgy rajzolod meg, mint egy képernyőt.

![A WEBview oldal beállításai](img/configure-06-webview.png)

---

[← A runtime telepítése](install.hu.md) | [Áttekintés](README.hu.md) | [Példaprojektek →](examples/README.hu.md)
