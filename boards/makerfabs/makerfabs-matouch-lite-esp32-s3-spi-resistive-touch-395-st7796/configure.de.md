---
title: Makerfabs MaTouch Lite ESP32-S3 3.95" im ctrl32-Editor einrichten
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Die Board-Seite des Makerfabs MaTouch Lite ESP32-S3 3.95" im Editor
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Das Board einrichten

## Die Board-Seite

Doppelklicken Sie auf das Board im Gerätebaum. Die Seite zeigt, was das Board trägt, und jeden Pin: ein freier Pin bekommt mit einem Klick eine Variable - einen Eingang, einen Ausgang oder an einem analogfähigen Pin einen Analogeingang.

![Die Board-Seite: die freien Pins und was jeder kann](img/configure-01-board.png)

## Netzwerk

Das Board verbindet sich mit Ihrem WLAN: Öffnen Sie die Seite **WiFi** im
Gerätebaum und tragen Sie Name und Passwort des Netzwerks ein (das Beispiel
trägt Platzhalter). Eine feste Adresse vergeben Sie auf der Board-Seite
im Abschnitt **Network**.


## Eingänge, Ausgänge und Variablen

Jedes Signal des Programms ist eine **Variable**. Eine Variable an einem Pin liest oder treibt den Pin; eine Analogvariable sagt, was daran angeschlossen ist (eine Spannung, 4-20 mA, ein Thermistor), und ihren Bereich in Einheiten.

![Die Variablen des All-in-one-Beispiels](img/configure-03-variables.png)

## Kommunikation

**Modbus TCP.** Ein Gerät im Netzwerk wird unter **Ethernet → Modbus TCP master** hinzugefügt; seine Register werden zu Variablen.

**Modbus RTU / RS-485.** Das Board hat keinen RS-485-Transceiver und neben den I/O des Beispiels zu wenige freie Pins dafür; Modbus-Geräte werden über Modbus TCP im WLAN erreicht.

**CAN.** Der ESP32-S3 hat einen CAN-Controller (TWAI). Das Board hat keinen Transceiver: Setzen Sie ein 3,3-V-Transceiver-Modul auf zwei freie Pins und benennen Sie diese auf der Board-Seite (**Bus pins**); das Beispiel nutzt GPIO6 / GPIO7.

**MQTT.** Das Board veröffentlicht gewählte Variablen an einen Broker; im Home-Assistant-Modus findet der Broker sie von selbst, und eine mit *write* markierte Variable lässt sich von dort setzen.

![Die Seite MQTT: der Broker und die veröffentlichten Variablen](img/configure-05-mqtt.png)

## Display und Touch

Das Glas hat 320 x 480, hochkant wie montiert; die Seite HMIview dreht das
Bild (der Touch folgt) und legt den Startbildschirm fest. Der resistive
Touch braucht festen Druck - zeichnen Sie Schaltflächen mindestens 40 px
hoch.

![Die HMIview-Einstellungen: der Bildschirm, auf den das Projekt zeichnet](img/configure-04-display.png)

## WEBview

Das Board liefert seine Bedienseite an jeden Browser im Netzwerk - öffnen Sie die Adresse des Boards. Die Seite wird im Editor wie ein Bildschirm gezeichnet.

![Die Einstellungen der Seite WEBview](img/configure-06-webview.png)

---

[← Runtime installieren](install.de.md) | [Übersicht](README.de.md) | [Beispielprojekte →](examples/README.de.md)
