---
title: 'Makerfabs MaTouch ESP32-P4 7": Beispiel Flexo press on a SIMATIC'
slug: flexo-press-simatic
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Die Bedienseite des Beispiels flexo press on a simatic für den Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Flexo press on a SIMATIC

Das HMI einer Achtfarben-Flexodruckmaschine, gesteuert von einer SIMATIC S7-1200 - die Maschine mit laufender Bahn, sechzehn Druckwerk-Servos, das Register, die Trockner, Aufträge als Rezepte und die Diagnose, über das S7-Protokoll.

**Download:** [flexo-press-simatic.prj32](flexo-press-simatic.prj32) - öffnen Sie es im ctrl32-Editor (**File → Open**).

## Was es tut

Sechs Seiten auf einem hellen Industriepanel:

- **Overview** - die Maschine als Zeichnung mit der darüber laufenden
  Bahn, die Synchronleuchten der Druckwerke, die Trocknertemperaturen,
  die Bahnspannungen und die Rollenlängen; START (mit Bestätigung),
  STOP, JOG, RESET.
- **Sections** - die sechzehn Druckwerk-Servos: Plattenzylinder und
  Rasterwalzen, synchron, Störung, Drehzahl, freigegeben.
- **Register** - der Registerfehler jedes Druckwerks und die Korrektur.
- **Heating** - die Trockenkammern und der Brückentrockner.
- **Jobs** - der Auftrag als **Rezept** im Panel: laden, speichern,
  löschen.
- **Diagnostics** - die Alarme, die Verbindung zur SPS und ein Trend
  von Geschwindigkeit und Bahnspannung.

Das Panel spricht mit einer **SIMATIC S7-1200** über **+7** (das
S7-Protokoll, ISO-on-TCP): es liest alle 100 ms den Statusbaustein
DB100 der SPS und schreibt seine Sollwerte und Befehle in DB101 - mehr
ist in der SPS nicht nötig. Im **Demo-Modus** (standardmäßig ein)
betreibt das Programm SIM die Maschine auf dem Panel selbst.

## Die Bildschirme

**Übersicht**

![Die Seite Overview: die Maschinenzeichnung mit laufender Bahn, Bahnspannungen und Trocknern](img/overview.png)

**Druckwerke**

![Die Seite Sections: sechzehn Druckwerk-Servos mit ihrem Zustand](img/sections.png)

**Aufträge**

![Die Seite Jobs: der Auftrag als Rezept im Panel](img/jobs.png)

## Öffnen und ausführen

1. Öffnen Sie `flexo-press-simatic.prj32` im Editor.
2. Lassen Sie es laufen, wie es ist, im Demo-Modus; mit einer SPS stellen Sie ihre Adresse auf der Seite +7 ein und legen die beiden Datenbausteine DB100 / DB101 an.
3. Starten Sie die **Simulation** (Symbolleiste), um es am PC auszuprobieren, oder laden Sie es auf das Board - siehe [Runtime installieren](../../install.de.md).

## Was Sie sehen sollten

Die Übersicht erscheint im Demo-Modus. Drücken Sie START und bestätigen
Sie: die Maschine fährt hoch, die Bahn läuft über die Zeichnung und die
Bahnspannungen pendeln sich ein. Schalten Sie den Demo-Modus auf der
Seite Diagnostics aus und stellen Sie die Adresse der SPS ein - das
Panel zeigt dann die echte Maschine.


---

[← Beispielprojekte](../README.de.md) | [Übersicht](../../README.de.md)
