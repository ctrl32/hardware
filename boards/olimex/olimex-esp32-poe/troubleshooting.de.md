---
title: 'Olimex ESP32-PoE: Fehlersuche'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- troubleshooting
---

# Fehlersuche

| Symptom | Ursache | Abhilfe |
|---|---|---|
| Der COM-Port erscheint nicht, die Portauswahl bleibt leer | Das Kabel führt nur Strom, oder der CH340-Treiber fehlt | Verwenden Sie ein Datenkabel; installieren Sie den CH340-Treiber (WCH CH341SER); probieren Sie einen anderen USB-Port. |
| Flash runtime bleibt beim Verbinden stehen | Ein anderes Programm hält den Port | Schließen Sie den seriellen Monitor oder das andere Werkzeug, das den Port offen hat, und versuchen Sie es erneut. |
| Das Board startet alle paar Sekunden neu | Der USB-Port liefert den Strom nicht, während Ethernet startet | Verwenden Sie einen aktiven USB-Hub oder ein 5-V-Netzteil mit mindestens 1 A, oder betreiben Sie das Board an PoE (ohne USB). |
| Das Netzwerk kommt nicht hoch | Kein DHCP-Server, oder kein Link am Port | Prüfen Sie die Link-LEDs an der Buchse; vergeben Sie eine feste Adresse auf der Ethernet-Seite; probieren Sie einen anderen Port des Switches. |
| Das Board wird unter seinem .local-Namen nicht gefunden | Das Netzwerk blockiert mDNS (Multicast) | Verwenden Sie die IP-Adresse des Boards - die Client-Liste des Routers und Find devices im Editor zeigen sie. |
| USB trennt sich oder der PC meldet einen Fehler, sobald das PoE-Kabel eingesteckt wird | USB und PoE gleichzeitig angeschlossen an einem Board, das nicht galvanisch getrennt ist | Ziehen Sie sofort eines von beiden ab. Spielen Sie zuerst über USB auf, betreiben Sie dann an PoE - oder verwenden Sie das ESP32-PoE-ISO. |
| Ein Ausgang an GPIO34 bis GPIO39 tut nichts | Diese Pins sind reine Eingänge | Legen Sie den Ausgang auf GPIO33, GPIO4 oder GPIO5. |
| Ein Modbus-Wert bleibt auf 0 | Die Geräteadresse, die Unit oder das Register ist falsch, oder das Gerät liegt in einem anderen Subnetz | Prüfen Sie IP und Unit des Geräts im Gerätebaum und das Register im Handbuch des Geräts; pingen Sie das Gerät vom PC aus an. |

Das Fenster **Messages** des Editors und der **Diagnosepuffer** des Boards (Online → Diagnostics) sagen, was die Runtime entschieden hat und warum - lesen Sie sie zuerst.

---

[← Beispielprojekte](examples/README.de.md) | [Übersicht](README.de.md)
