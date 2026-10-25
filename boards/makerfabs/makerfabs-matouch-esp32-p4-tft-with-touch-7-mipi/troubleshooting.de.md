---
title: 'Makerfabs MaTouch ESP32-P4 7": Fehlersuche'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- troubleshooting
---

# Fehlersuche

| Symptom | Ursache | Abhilfe |
|---|---|---|
| Der COM-Port erscheint nicht | Das Kabel führt nur Strom, oder der CH340-Treiber fehlt | Verwenden Sie ein USB-C-Datenkabel; installieren Sie den CH340-Treiber (WCH CH341SER); versuchen Sie einen anderen USB-Port. |
| Das Board startet neu, wenn der Bildschirm aufleuchtet | Das Netzteil trägt die Hintergrundbeleuchtung nicht | Verwenden Sie ein Netzteil mit 5 V / 2 A oder einen aktiven USB-Hub. |
| Der Bildschirm bleibt dunkel, nachdem die Runtime geschrieben wurde | Noch kein Projekt auf dem Board | Übertragen Sie das Projekt (F5); ein Board ohne Projekt zeigt auf dem Glas nichts. |
| Der Touch reagiert nicht oder an der falschen Stelle | Die Ausrichtung des Projekts weicht davon ab, wie das Board montiert ist | Stellen Sie die Ausrichtung auf der Seite HMIview ein und übertragen Sie erneut. |
| Das Netzwerk kommt nicht hoch | Kein DHCP-Server, oder kein Link am Port | Prüfen Sie die Link-LEDs an der Buchse; setzen Sie eine feste Adresse auf der Board-Seite; prüfen Sie bei WLAN den Netzwerknamen und das Passwort. |
| CAN bleibt stumm | Kein Transceiver, keine 120-Ohm-Terminierung oder eine andere Bitrate | Prüfen Sie den Transceiver an GPIO20 / GPIO21, einen 120-Ohm-Widerstand an beiden Enden des Busses und dieselbe Bitrate auf jedem Knoten. |
| Ein Modbus-RTU-Wert bleibt auf 0 | A und B vertauscht, eine falsche Unit oder Baudrate, oder der DE-Pin fehlt | Tauschen Sie A und B; prüfen Sie Unit, Baudrate und Parität; prüfen Sie, dass DE verdrahtet und benannt ist. |

Das Fenster **Messages** des Editors und der **Diagnosepuffer** des Boards (Online → Diagnostics) sagen, was die Runtime entschieden hat und warum - lesen Sie sie zuerst.

---

[← Beispielprojekte](examples/README.de.md) | [Übersicht](README.de.md)
