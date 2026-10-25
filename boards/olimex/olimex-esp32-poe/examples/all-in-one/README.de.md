---
title: 'Olimex ESP32-PoE: Beispiel All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/screen.png
image_alt: Die Bedienseite des Beispiels all-in-one für den Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- example
---

# All-in-one

Eine Pumpe, gesteuert über den Taster des Boards, die Bedienseite und Home Assistant, mit Füllstandseingang, Laufzeit-Timer, Füllstandsalarm und einem Modbus-TCP-Energiezähler.

**Download:** [all-in-one.prj32](all-in-one.prj32) - öffnen Sie es im ctrl32-Editor (**File → Open**).

## Was es tut

Das Programm ist eine kleine Pumpensteuerung - die Form der meisten
Maschinen:

- **Start** kommt vom Taster des Boards (BUT1), von der Schaltfläche
  **Start** auf der Bedienseite oder von Home Assistant über MQTT.
- **Stopp** kommt von der Schaltfläche **Stop**, von einem niedrigen
  Füllstand oder vom Ablauf der Laufzeit - die Selbsthaltung (Latch)
  nimmt den Ausgang an GPIO33 zurück.
- Der **Füllstand** ist ein Analogeingang an GPIO35 (0 bis 3,3 V,
  skaliert auf 0 bis 100 %). Unter 10 % stoppt die Pumpe und ein Alarm
  wird ausgelöst; über 15 % darf sie wieder anlaufen (Hysterese).
- Die **Laufzeit** wird auf der Seite in Minuten eingestellt und
  übersteht einen Stromausfall (eine remanente Variable).
- Ein **Modbus-TCP**-Energiezähler im Netzwerk liefert die Netzspannung
  (Register 0, Eingangsregister, Unit 1 unter 192.168.1.60 - ändern Sie
  das auf Ihren Zähler). Über 253 V wird ein Alarm ausgelöst.
- **CAN** (ein Transceiver an GPIO4 / GPIO36) sendet Füllstand und
  Pumpenzustand alle 100 ms im Telegramm 0x181 und empfängt einen
  Sollwert in 0x201.
- **MQTT** veröffentlicht Füllstand, Pumpenzustand und Spannung an
  einen Home-Assistant-Broker, der sie von selbst findet (Discovery);
  die Pumpe lässt sich aus Home Assistant starten.
- **WEBview** liefert die Bedienseite - die Pumpe, den Füllstand, seinen
  Trend und die Alarme - an jeden Browser im Netzwerk.

## Das Programm

![Das Kontaktplan-Programm des Beispiels](img/ladder.png)

## Die Bedienseite

![Die Bedienseite in der Simulation](img/screen.png)

## Öffnen und ausführen

1. Öffnen Sie `all-in-one.prj32` im Editor.
2. Ändern Sie die Adressen (das Modbus-Gerät, den MQTT-Broker) auf die Ihres Netzwerks.
3. Starten Sie die **Simulation** (Symbolleiste), um es am PC auszuprobieren, oder laden Sie es auf das Board - siehe [Runtime installieren](../../install.de.md).

## Was Sie sehen sollten

Drehen Sie das Potentiometer auf und drücken Sie BUT1: Das Relais an
GPIO33 schaltet ein und die Pumpen-LED auf der Seite leuchtet. Drehen
Sie das Potentiometer unter 10 %: Die Pumpe stoppt und der Alarm
erscheint in der Tabelle. In Home Assistant erscheint das Board mit
Füllstand, Pumpe und Spannung.


---

[← Beispielprojekte](../README.de.md) | [Übersicht](../../README.de.md)
