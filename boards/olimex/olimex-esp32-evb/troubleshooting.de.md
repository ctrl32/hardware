---
title: 'Olimex ESP32-EVB: Fehlersuche'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-EVB
tags:
- esp32
- ethernet
- can
- relay
- olimex
- troubleshooting
---

# Fehlersuche

| Symptom | Ursache | Abhilfe |
|---|---|---|
| Der COM-Port erscheint nicht, die Portauswahl bleibt leer | Das Kabel führt nur Strom, oder der USB-Treiber fehlt | Verwenden Sie ein Datenkabel; installieren Sie den Treiber des USB-Chips des Boards; probieren Sie einen anderen USB-Port. |
| Flash runtime bleibt beim Verbinden stehen | Ein anderes Programm belegt den Port | Schließen Sie den seriellen Monitor oder das andere Werkzeug, das den Port offen hält, und versuchen Sie es erneut. |
| Das Board startet alle paar Sekunden neu | Der USB-Port liefert nicht genug Strom | Verwenden Sie einen USB-Hub mit eigener Versorgung oder ein 5-V-Netzteil mit mindestens 1 A. |
| Das Netzwerk kommt nicht hoch | Kein DHCP-Server oder kein Link am Port | Prüfen Sie die Link-LEDs an der Buchse; vergeben Sie auf der Board-Seite eine feste Adresse; probieren Sie einen anderen Port des Switches. |
| Das Board wird unter seinem .local-Namen nicht gefunden | Das Netzwerk blockiert mDNS (Multicast) | Verwenden Sie die IP-Adresse des Boards - die Client-Liste des Routers und Find devices im Editor zeigen sie. |
| Ein Ausgang tut nichts | Der Pin ist nur ein Eingang, oder der falsche Pin wurde angegeben | Prüfen Sie den Pin auf der Board-Seite - reine Eingangspins sind markiert; legen Sie den Ausgang auf einen freien I/O-Pin. |
| Ein Modbus-Wert bleibt auf 0 | Geräteadresse, Unit oder Register ist falsch | Prüfen Sie IP und Unit des Geräts im Gerätebaum und das Register im Handbuch des Geräts. |
| CAN bleibt stumm | Kein 120-Ohm-Abschluss oder eine andere Bitrate | Setzen Sie an beide Enden des Busses einen 120-Ohm-Widerstand; stellen Sie an jedem Knoten dieselbe Bitrate ein. |

Das Fenster **Messages** des Editors und der **Diagnosepuffer** des Boards (Online → Diagnostics) sagen, was die Runtime entschieden hat und warum - lesen Sie sie zuerst.

---

[← Beispielprojekte](examples/README.de.md) | [Übersicht](README.de.md)
