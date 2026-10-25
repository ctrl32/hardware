---
title: 'Makerfabs MaTouch ESP32-P4 7": Beispiel Car cockpit'
slug: car-cockpit
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Die Bedienseite des Beispiels car cockpit für den Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Car cockpit

Ein Kombiinstrument an einem J1939-Fahrzeugbus - Tacho und Drehzahlmesser, Gang, Kraftstoff, Kühlmittel, die Warnleuchten, die Steuergeräte am Bus, der aktive Fehlercode in Worten und die Einstellungen des Fahrers.

**Download:** [car-cockpit.prj32](car-cockpit.prj32) - öffnen Sie es im ctrl32-Editor (**File → Open**).

## Was es tut

Fünf Bildschirme auf dem 7"-Glas:

- **Cockpit** - Tacho und Drehzahlmesser, der Gang, Kraftstoff,
  Kühlmittel und Batterie, Kilometerzähler und Tageskilometer, die Uhr,
  die Blinker und die Warnleuchten.
- **Engine** - die Werte des Motors im Detail.
- **Bus** - das **J1939**-Netzwerk: der Knoten des Panels, Motor,
  Getriebe und Bremsen und ob sie antworten, die DM1-Leuchten, jedes
  Signal mit seiner Parametergruppe.
- **Faults** - die Alarmliste und der aktive Fehlercode des Motors
  (SPN / FMI / Anzahl) mit seiner Bedeutung in Worten.
- **Settings** - Demo-Modus, Einheiten, die Geschwindigkeitswarnung,
  der rote Drehzahlbereich, die Kühlmittel- und Kraftstoffwarnungen,
  das Serviceintervall.

Die Kommunikation ist **SAE J1939** auf dem CAN des Boards (ein
3,3-V-Transceiver an GPIO47 / GPIO48, 250 kbit/s): Motor, Getriebe und
Bremsen senden ihre Parametergruppen, und das Panel liest sie - damit
ein Wert ankommt, ist kein Programm nötig. Im **Demo-Modus**
(standardmäßig ein) fährt das Programm SIM einen Zyklus: anfahren,
schalten, konstant fahren, bremsen, anhalten - und hin und wieder ein
Fehler.

## Die Bildschirme

**Cockpit**

![Der Bildschirm Cockpit: Tacho und Drehzahlmesser, Gang, Kraftstoff, Kühlmittel und die Warnleuchten](img/cockpit.png)

**Bus**

![Der Bildschirm Bus mit dem J1939-Netzwerk: die Steuergeräte und die Signale, die das Panel liest](img/bus.png)

**Fehler**

![Der Bildschirm Faults: die Alarmliste und der aktive Fehlercode](img/faults.png)

## Öffnen und ausführen

1. Öffnen Sie `car-cockpit.prj32` im Editor.
2. Lassen Sie es laufen, wie es ist, im Demo-Modus; im Fahrzeug schließen Sie den CAN-Transceiver an GPIO47 / GPIO48 an und schalten den Demo-Modus auf dem Bildschirm Settings aus.
3. Starten Sie die **Simulation** (Symbolleiste), um es am PC auszuprobieren, oder laden Sie es auf das Board - siehe [Runtime installieren](../../install.de.md).

## Was Sie sehen sollten

Das Kombiinstrument erscheint im Demo-Modus: die Zeiger laufen durch
den Fahrzyklus, der Gang wechselt, die Blinker blinken. Schalten Sie
den Demo-Modus auf dem Bildschirm Settings aus und schließen Sie den
Bus an - die Anzeigen zeigen dann das Fahrzeug.


---

[← Beispielprojekte](../README.de.md) | [Übersicht](../../README.de.md)
