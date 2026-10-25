---
title: 'Raspberry Pi 3 Model B+: Fehlersuche'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Raspberry Pi 3 Model B+
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- troubleshooting
---

# Fehlersuche

| Symptom | Ursache | Abhilfe |
|---|---|---|
| Look at the device kann keine Verbindung aufbauen | SSH ist aus, die Adresse ist falsch oder der PC ist in einem anderen Netzwerk | Aktivieren Sie SSH in den Einstellungen des Imagers und schreiben Sie die Karte neu; pingen Sie die Adresse vom PC aus an. |
| Prepare bietet keine Installation an | Die ctrl32-Runtime ist auf dem Pi bereits installiert | Eine installierte Runtime wird mit Flash runtime und der Adresse des Pi in der Port-Auswahl aktualisiert. |
| Der Monitor bleibt nach dem Übertragen des Projekts schwarz | Der Monitor wurde erst nach dem Hochfahren angeschlossen, oder das Projekt hat keinen Bildschirm | Schließen Sie den Monitor an, bevor Sie den Pi einschalten; fügen Sie dem Projekt einen Bildschirm hinzu. |
| WEBview öffnet sich nicht | Der falsche Port | Öffnen Sie http://<Adresse>:8080 - die Runtime liefert auf Port 8080. |
| Der USB-RS485-Adapter verschwindet | Unterspannung - das Netzteil ist zu schwach | Verwenden Sie das offizielle 27-W-Netzteil. |
| CAN bleibt stumm | Der Treiber des HAT ist nicht geladen, keine Terminierung oder eine andere Bitrate | Haken Sie den HAT in Prepare a Linux device an; ein 120-Ohm-Widerstand an beiden Enden des Busses; dieselbe Bitrate auf jedem Knoten. |
| Ein OPC-UA-Client sieht keine Variablen | Die Variable ist vom Server ferngehalten, oder eine Firewall blockiert Port 4840 | Prüfen Sie den OPC-UA-Haken in der Variablenliste; öffnen Sie Port 4840. |

Das Fenster **Messages** des Editors und der **Diagnosepuffer** des Boards (Online → Diagnostics) sagen, was die Runtime entschieden hat und warum - lesen Sie sie zuerst.

---

[← Beispielprojekte](examples/README.de.md) | [Übersicht](README.de.md)
