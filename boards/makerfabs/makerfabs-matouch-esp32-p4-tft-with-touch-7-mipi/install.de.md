---
title: Die ctrl32-Runtime auf dem Makerfabs MaTouch ESP32-P4 7" installieren
slug: install
sidebar_position: 30
image: img/install-04-flash-runtime.png
image_alt: Der ctrl32-Editor schreibt die Runtime auf den Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- install
---

# Die ctrl32-Runtime installieren

Die Runtime ist das Programm auf dem Board, das Ihr Projekt ausführt - den SPS-Zyklus, die Bildschirme, die Kommunikation. Sie kommt einmal auf das Board; danach ist jede Änderung des Projekts ein Download, der nichts als das Projekt überschreibt.

## 1. Das Board anschließen

Verbinden Sie das Board über das USB-Kabel mit dem PC. Am USB-C-Anschluss sitzt ein USB-UART-Wandler CH340K. Windows 10 und 11
installieren seinen Treiber von selbst; erscheint der Port nicht,
installieren Sie den CH340-Treiber des Chipherstellers (WCH) und stecken
Sie das Kabel erneut ein.

![Makerfabs MaTouch ESP32-P4 7"](img/board-01.jpg)

## 2. Das Projekt anlegen

Starten Sie den ctrl32-Editor und wählen Sie **New project** (Strg+N). Geben Sie den **Namen** des Projekts ein, wählen Sie **MaTouch ESP32-P4 7"** in der Liste der Boards (unter **Makerfabs**) und drücken Sie **Create project**.

![Der Assistent New project mit gewähltem Makerfabs MaTouch ESP32-P4 7"](img/install-02-new-project.png)

Um stattdessen mit dem fertigen Beispiel zu beginnen, öffnen Sie das [All-in-one-Projekt](examples/all-in-one/README.de.md) (**File → Open**).

## 3. Die Runtime schreiben

Wählen Sie den COM-Port des Boards in der Portauswahl der Symbolleiste, klicken Sie auf das Board im Gerätebaum und drücken Sie **Flash runtime**. Der Editor schreibt die Runtime, liest sie zurück und prüft sie; das dauert etwa eine Minute, und das Board startet neu. Das geschieht einmal - und erneut nur, wenn der Editor eine neue Runtime-Linie bringt.

![Der Dialog Flash runtime mit der Runtime für den Makerfabs MaTouch ESP32-P4 7"](img/install-04-flash-runtime.png)

## 4. Das Projekt laden

Drücken Sie die Download-Schaltfläche in der Symbolleiste (F5). Der Editor baut das Projekt, schreibt es in den inaktiven Programmslot des Boards, prüft es und schaltet erst dann um - ein fehlgeschlagener Download lässt das laufende Programm unberührt.

![Die Symbolleiste: die Portauswahl und die Download-Schaltfläche](img/install-05-download.png)

## 5. Prüfen, dass es läuft

Drücken Sie **ONLINE** (das Steckersymbol neben der Portauswahl), um das Programm auf dem Board zu beobachten: was leitet, ist grün, jede Variable trägt ihren Live-Wert. Ohne Board liefert die **Simulation** dieselbe Ansicht (die Schaltfläche neben ONLINE in der Symbolleiste).

![Das laufende Kontaktplan-Programm - grün heißt, Strom fließt](img/install-06-running.png)

Etwas geht nicht? Siehe [Fehlersuche](troubleshooting.de.md).

*Bildschirmfotos: ctrl32-Editor 1.07.*

---

[← Hardware und Verdrahtung](hardware.de.md) | [Übersicht](README.de.md) | [Einrichten →](configure.de.md)
