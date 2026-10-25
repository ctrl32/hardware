---
title: 'Makerfabs MaTouch ESP32-P4 7": Beispiel All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Die Bedienseite des Beispiels all-in-one für den Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# All-in-one

Ein Motor, gesteuert vom Touchscreen, von zwei Tastern und aus Home Assistant, mit einer Druckanzeige, einem Lüfter nach einer Modbus-RTU-Temperatur, einem Modbus-TCP-Leistungszähler, CAN-Telegrammen, einem Trend und den Alarmen.

**Download:** [all-in-one.prj32](all-in-one.prj32) - öffnen Sie es im ctrl32-Editor (**File → Open**).

## Was es tut

Das Programm ist eine kleine Maschinensteuerung:

- **Start** kommt von einem Taster an GPIO47, von **Start** auf dem
  Bildschirm oder aus Home Assistant über MQTT; **Stopp** von einem
  Taster an GPIO48, von **Stop** auf dem Bildschirm oder wenn der Druck
  über den Sollwert steigt, der über **CAN** ankommt (Telegramm 0x201).
- Die Selbsthaltung treibt den Motorausgang an **GPIO33**; ein Zähler
  hält die Zahl der Starts über einen Stromausfall.
- Der **Druck** ist ein Analogeingang über einen **ADS1115** am I2C-Bus
  (0-10 V über einen 1:4-Teiler, 0-10 bar) und geht alle 100 ms über
  CAN hinaus (Telegramm 0x181).
- Die **Temperatur** kommt von einem **Modbus-RTU**-Sensor (Unit 1,
  Input-Register 1, 0,1 °C); ein Lüfter folgt ihr mit Hysterese.
- Ein **Modbus-TCP**-Zähler liefert die bezogene Leistung.
- Drei **Bildschirme** auf dem Glas: die Übersicht, ein Trend und die
  Alarme; eine einfachere Seite in jedem Browser (WEBview).

## Das Programm

![Das Kontaktplan-Programm des Beispiels](img/ladder.png)

## Die Bedienseite

![Die Bedienseite in der Simulation](img/screen.png)

## Öffnen und ausführen

1. Öffnen Sie `all-in-one.prj32` im Editor.
2. Ändern Sie die Adressen (das Modbus-Gerät, den MQTT-Broker) auf die Ihres Netzwerks.
3. Starten Sie die **Simulation** (Symbolleiste), um es am PC auszuprobieren, oder laden Sie es auf das Board - siehe [Runtime installieren](../../install.de.md).

## Was Sie sehen sollten

Die Übersicht erscheint auf dem Glas. Drücken Sie **Start**: die
Motor-LED leuchtet und der Startzähler zählt hoch. Die Anzeige zeigt
den Druck, der Bildschirm Trend zeichnet ihn zusammen mit der
Temperatur, und auf dem Bildschirm Alarms erscheint ein Alarm, wenn der
Druck über 8 bar steigt.


---

[← Beispielprojekte](../README.de.md) | [Übersicht](../../README.de.md)
