---
title: 'Makerfabs MaTouch ESP32-P4 7": Beispiel Home dashboard'
slug: home-dashboard
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.jpg
image_alt: Die Bedienseite des Beispiels home dashboard für den Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Home dashboard

Ein Steuerpanel für das ganze Haus im dunklen Milchglas-Stil - Heizung je Raum, Energie mit PV und Batterie, Licht, die Garage und das Wetter - mit einem simulierten Haus dahinter.

**Download:** [home-dashboard.prj32](home-dashboard.prj32) - öffnen Sie es im ctrl32-Editor (**File → Open**).

## Was es tut

Sechs Bildschirme über Fotografien des Hauses, jeder ein Satz
Milchglas-Karten:

- **Home** - die Uhrzeit, das Wetter, die Räume, der Alarm und die
  Szenen.
- **Weather** - heute und die nächsten Tage.
- **Climate** - sechs Räume, jeder mit seiner Temperatur, seinem
  Sollwert und der Heizung; die Wärmepumpe und der Warmwasserspeicher.
- **Energy** - die PV-Leistung, der Hausverbrauch, die Batterie und das
  Netz, die kWh des Tages.
- **Lights** - die Leuchten der Räume und ihre Szenen.
- **Access** - das Garagentor, die Wallbox, der Alarm.

Das Programm **SIM** ist das Haus: die Außentemperatur folgt dem Tag,
die PV-Leistung der Sonne, der Verbrauch hat seine Morgen- und
Abendspitze, die Räume heizen mit Hysterese auf ihre Sollwerte.
Ersetzen Sie seine Variablen durch Ihre Modbus-, MQTT- oder CAN-Geräte,
um ein echtes Haus zu steuern.

## Die Bildschirme

**Startseite**

![Der Bildschirm Home des Dashboards: Uhrzeit, Wetter, Räume, Alarm und Szenen](img/home.jpg)

**Klima**

![Der Bildschirm Climate: sechs Räume mit ihren Temperaturen und Sollwerten](img/climate.png)

**Energie**

![Der Bildschirm Energy: PV, Hausverbrauch, Batterie und Netz](img/energy.jpg)

## Öffnen und ausführen

1. Öffnen Sie `home-dashboard.prj32` im Editor.
2. Lassen Sie es laufen, wie es ist - das Haus ist simuliert; für ein echtes Haus ersetzen Sie die Variablen des Programms SIM durch Ihre Geräte.
3. Starten Sie die **Simulation** (Symbolleiste), um es am PC auszuprobieren, oder laden Sie es auf das Board - siehe [Runtime installieren](../../install.de.md).

## Was Sie sehen sollten

Der Bildschirm Home erscheint mit der Uhrzeit, dem Wetter und den
Räumen; die Werte bewegen sich, während der simulierte Tag vergeht. Ein
Tippen auf den Sollwert eines Raums ändert ihn, und der Raum heizt sich
darauf auf.


---

[← Beispielprojekte](../README.de.md) | [Übersicht](../../README.de.md)
