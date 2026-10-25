---
title: 'Makerfabs MaTouch ESP32-P4 7": exemplul All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Pagina operatorului din exemplul all-in-one pentru Makerfabs MaTouch ESP32-P4 7"
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

Un motor comandat de pe ecranul tactil, de la două butoane și din Home Assistant, cu un indicator de presiune, un ventilator după o temperatură Modbus RTU, un contor de putere Modbus TCP, cadre CAN, un trend și alarmele.

**Descărcare:** [all-in-one.prj32](all-in-one.prj32) - deschide-l în editorul ctrl32 (**File → Open**).

## Ce face

Programul este un mic controler de mașină:

- **Start** vine de la un buton pe GPIO47, de la **Start** de pe ecran
  sau din Home Assistant prin MQTT; **Stop** de la un buton pe GPIO48,
  de la **Stop** de pe ecran sau de la creșterea presiunii peste
  valoarea de referință care sosește prin **CAN** (cadrul 0x201).
- Automenținerea comandă ieșirea motorului pe **GPIO33**; un contor
  păstrează numărul de porniri și la o pană de curent.
- **Presiunea** este o intrare analogică printr-un **ADS1115** pe
  magistrala I2C (0-10 V printr-un divizor 1:4, 0-10 bar) și pleacă pe
  CAN la fiecare 100 ms (cadrul 0x181).
- **Temperatura** vine de la un senzor **Modbus RTU** (unit 1,
  registrul de intrare 1, 0,1 °C); un ventilator o urmează cu
  histerezis.
- Un contor **Modbus TCP** dă puterea consumată.
- Trei **ecrane** pe sticlă: prezentarea generală, un trend și
  alarmele; o pagină mai simplă în orice browser (WEBview).

## Programul

![Programul ladder al exemplului](img/ladder.png)

## Pagina operatorului

![Pagina operatorului rulând în simulare](img/screen.png)

## Deschide-l și rulează-l

1. Deschide `all-in-one.prj32` în editor.
2. Schimbă adresele (dispozitivul Modbus, brokerul MQTT) cu cele ale rețelei tale.
3. Pornește **simularea** (bara de instrumente) pentru a-l încerca pe PC sau descarcă-l pe placă - vezi [Instalarea runtime-ului](../../install.ro.md).

## Ce ar trebui să vezi

Prezentarea generală apare pe sticlă. Apasă **Start**: LED-ul
motorului se aprinde și contorul de porniri crește. Indicatorul arată
presiunea, ecranul Trend o desenează împreună cu temperatura, iar pe
ecranul Alarms apare o alarmă când presiunea trece de 8 bar.


---

[← Proiecte exemplu](../README.ro.md) | [Prezentare](../../README.ro.md)
