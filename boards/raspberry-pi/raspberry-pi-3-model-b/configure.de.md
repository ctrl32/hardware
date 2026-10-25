---
title: Raspberry Pi 3 Model B+ im ctrl32-Editor einrichten
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Die Board-Seite des Raspberry Pi 3 Model B+ im Editor
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Das Board einrichten

## Die Board-Seite

Doppelklicken Sie auf das Board im Gerätebaum. Die Seite zeigt, was das Board trägt, und jeden Pin: ein freier Pin bekommt mit einem Klick eine Variable - einen Eingang, einen Ausgang oder an einem analogfähigen Pin einen Analogeingang.

![Die Board-Seite: die freien Pins und was jeder kann](img/configure-01-board.png)

## Netzwerk

Der Pi behält die Netzwerkeinstellungen seines Betriebssystems: DHCP vom
Router, sofern **Prepare a Linux device** keine feste Adresse gesetzt hat.
Sie finden ihn über seinen Hostnamen oder mit **Find devices** im Editor.


## Eingänge, Ausgänge und Variablen

Jedes Signal des Programms ist eine **Variable**. Eine Variable an einem Pin liest oder treibt den Pin; eine Analogvariable sagt, was daran angeschlossen ist (eine Spannung, 4-20 mA, ein Thermistor), und ihren Bereich in Einheiten.

![Die Variablen des All-in-one-Beispiels](img/configure-03-variables.png)

## Kommunikation

**Modbus TCP.** Ein Gerät im Netzwerk wird unter **Ethernet → Modbus TCP master** hinzugefügt; seine Register werden zu Variablen.

**Modbus RTU / RS-485.** Ein USB-RS485-Adapter (`/dev/ttyUSB0`, die Richtung schaltet von selbst um) oder ein RS-485-HAT an der UART des Pi. ctrl32 ist darauf Modbus-RTU-Master oder -Slave, auf bis zu vier Leitungen.

**CAN.** CAN kommt von einem CAN-HAT an SPI (MCP2515, MCP251xFD) oder von einem USB-CAN-Adapter; die Runtime nutzt ihn als SocketCAN-Schnittstelle (`can0`, bis zu vier Busse). Prepare a Linux device fügt den Treiber des HAT hinzu; die Bitrate ist die des Projekts.

**MQTT.** Das Board veröffentlicht gewählte Variablen an einen Broker; im Home-Assistant-Modus findet der Broker sie von selbst, und eine mit *write* markierte Variable lässt sich von dort setzen.

![Die Seite MQTT: der Broker und die veröffentlichten Variablen](img/configure-05-mqtt.png)

## Display

Die Runtime zeichnet auf den angeschlossenen HDMI-Monitor (oder ein
DSI-Display) und skaliert das Projekt darauf; das Beispiel ist in
1280 x 720 gezeichnet. Der USB-Touch eines Touch-Monitors funktioniert ohne
Treiber. Ohne Monitor liefert der Pi seine Bildschirme nur an Browser
(WEBview).

![Die HMIview-Einstellungen: der Bildschirm, auf den das Projekt zeichnet](img/configure-04-display.png)

## OPC UA und EtherCAT

- **OPC UA** - jede Variable des Projekts ist ein Knoten des eigenen
  Servers des Pi (`opc.tcp://<Adresse>:4840`, `ns=1;s=<Name>`); eine
  Variable lässt sich mit einem Haken in der Variablenliste vom Server
  fernhalten. Sonst wird nichts eingestellt.
- **EtherCAT** - ein Master auf einem USB-Ethernet-Adapter für I/O-Klemmen;
  für Servoantriebe mit kurzem Buszyklus ist ein Raspberry Pi 4 oder 5 die
  bessere Wahl.

## WEBview

Das Board liefert seine Bedienseite an jeden Browser im Netzwerk - öffnen Sie die Adresse des Boards. Die Seite wird im Editor wie ein Bildschirm gezeichnet.

![Die Einstellungen der Seite WEBview](img/configure-06-webview.png)

---

[← Runtime installieren](install.de.md) | [Übersicht](README.de.md) | [Beispielprojekte →](examples/README.de.md)
