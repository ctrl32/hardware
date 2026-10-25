---
title: LaskaKit ESPlan im ctrl32-Editor einrichten
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Die Board-Seite des LaskaKit ESPlan im Editor
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Das Board einrichten

## Die Board-Seite

Doppelklicken Sie auf das Board im Gerätebaum. Die Seite zeigt, was das Board trägt, und jeden Pin: ein freier Pin bekommt mit einem Klick eine Variable - einen Eingang, einen Ausgang oder an einem analogfähigen Pin einen Analogeingang.

![Die Board-Seite: die freien Pins und was jeder kann](img/configure-01-board.png)

## Netzwerk

Der Ethernet-Port startet von selbst und bezieht seine Adresse von Ihrem
Router (DHCP). Eine feste Adresse vergeben Sie auf der Board-Seite im
Abschnitt **Network**; WLAN auf der Seite **WiFi** im Gerätebaum.


## Eingänge, Ausgänge und Variablen

Jedes Signal des Programms ist eine **Variable**. Eine Variable an einem Pin liest oder treibt den Pin; eine Analogvariable sagt, was daran angeschlossen ist (eine Spannung, 4-20 mA, ein Thermistor), und ihren Bereich in Einheiten.

![Die Variablen des All-in-one-Beispiels](img/configure-03-variables.png)

## Kommunikation

**Modbus TCP.** Ein Gerät im Netzwerk wird unter **Ethernet → Modbus TCP master** hinzugefügt; seine Register werden zu Variablen.

**Modbus RTU / RS-485.** Das Board trägt seinen RS-485-Transceiver (WS3081, geschützt). ctrl32 ist ein Modbus-RTU-Master - die Geräte und ihre Register werden im Gerätebaum unter RS485 hinzugefügt - oder ein Modbus-RTU-Slave, den andere Master lesen.

**CAN.** Der ESP32 hat einen CAN-Controller (TWAI). Das Board hat keinen CAN-Transceiver: setzen Sie ein 3,3-V-Transceiver-Modul an zwei freie Pins und benennen Sie sie auf der Board-Seite (Bus pins) - CANopen-Geräte, rohe CAN-Frames und die Fahrzeugbusse (J1939) laufen dann darauf.

**MQTT.** Das Board veröffentlicht gewählte Variablen an einen Broker; im Home-Assistant-Modus findet der Broker sie von selbst, und eine mit *write* markierte Variable lässt sich von dort setzen.

![Die Seite MQTT: der Broker und die veröffentlichten Variablen](img/configure-05-mqtt.png)

## WEBview

Das Board liefert seine Bedienseite an jeden Browser im Netzwerk - öffnen Sie die Adresse des Boards. Die Seite wird im Editor wie ein Bildschirm gezeichnet.

![Die Einstellungen der Seite WEBview](img/configure-06-webview.png)

---

[← Runtime installieren](install.de.md) | [Übersicht](README.de.md) | [Beispielprojekte →](examples/README.de.md)
