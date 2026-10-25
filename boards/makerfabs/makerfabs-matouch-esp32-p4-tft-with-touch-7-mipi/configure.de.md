---
title: Makerfabs MaTouch ESP32-P4 7" im ctrl32-Editor einrichten
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Die Board-Seite des Makerfabs MaTouch ESP32-P4 7" im Editor
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Das Board einrichten

## Die Board-Seite

Doppelklicken Sie auf das Board im Gerätebaum. Die Seite zeigt, was das Board trägt, und jeden Pin: ein freier Pin bekommt mit einem Klick eine Variable - einen Eingang, einen Ausgang oder an einem analogfähigen Pin einen Analogeingang.

![Die Board-Seite: die freien Pins und was jeder kann](img/configure-01-board.png)

## Netzwerk

Der Ethernet-Port startet von selbst und bezieht seine Adresse von Ihrem
Router (DHCP). Das WLAN des ESP32-C6 wird auf der Seite **WiFi** des
Gerätebaums eingestellt - der Netzwerkname und das Passwort. Eine feste
Adresse wird auf der Board-Seite in ihrem Abschnitt **Network** gesetzt.


## Eingänge, Ausgänge und Variablen

Jedes Signal des Programms ist eine **Variable**. Eine Variable an einem Pin liest oder treibt den Pin; eine Analogvariable sagt, was daran angeschlossen ist (eine Spannung, 4-20 mA, ein Thermistor), und ihren Bereich in Einheiten.

![Die Variablen des All-in-one-Beispiels](img/configure-03-variables.png)

## Kommunikation

**Modbus TCP.** Ein Gerät im Netzwerk wird unter **Ethernet → Modbus TCP master** hinzugefügt; seine Register werden zu Variablen.

**Modbus RTU / RS-485.** Das Board hat keinen RS-485-Transceiver: setzen Sie ein 3,3-V-Transceiver-Modul auf freie Pins (TX, RX und den Richtungspin DE) und benennen Sie sie auf der Board-Seite - das Beispiel nutzt GPIO4 / GPIO5 / GPIO32. ctrl32 ist dann Modbus-RTU-Master oder -Slave auf dieser Leitung.

**CAN.** Der ESP32-P4 hat einen CAN-Controller (TWAI). Das Board hat keinen CAN-Transceiver: setzen Sie ein 3,3-V-Transceiver-Modul auf zwei freie Pins und benennen Sie sie auf der Board-Seite (**Bus pins**) - das Beispiel nutzt GPIO20 / GPIO21. CANopen-Geräte, rohe CAN-Telegramme und die Fahrzeugbusse (J1939) laufen alle darauf.

**MQTT.** Das Board veröffentlicht gewählte Variablen an einen Broker; im Home-Assistant-Modus findet der Broker sie von selbst, und eine mit *write* markierte Variable lässt sich von dort setzen.

![Die Seite MQTT: der Broker und die veröffentlichten Variablen](img/configure-05-mqtt.png)

## Display und Touch

Das Projekt wird in den 1024 x 600 des Glases gezeichnet. Die Seite HMIview
legt die Ausrichtung fest (wie montiert oder gedreht - der Touch folgt),
die Größe der WEBview-Zeichenfläche und den Startbildschirm. Der Touch
braucht keine Einrichtung: der GT911-Controller ist Teil des Boards.

![Die HMIview-Einstellungen: der Bildschirm, auf den das Projekt zeichnet](img/configure-04-display.png)

## WEBview

Das Board liefert seine Bedienseite an jeden Browser im Netzwerk - öffnen Sie die Adresse des Boards. Die Seite wird im Editor wie ein Bildschirm gezeichnet.

![Die Einstellungen der Seite WEBview](img/configure-06-webview.png)

---

[← Runtime installieren](install.de.md) | [Übersicht](README.de.md) | [Beispielprojekte →](examples/README.de.md)
