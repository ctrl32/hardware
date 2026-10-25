---
title: 'Makerfabs MaTouch ESP32-P4 7": příklad Car cockpit'
slug: car-cockpit
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Stránka operátora příkladu car cockpit pro desku Makerfabs MaTouch ESP32-P4 7"
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

Přístrojový panel na vozidlové sběrnici J1939 - rychloměr a otáčkoměr, převodový stupeň, palivo, chladicí kapalina, výstražné kontrolky, řídicí jednotky na sběrnici, aktivní kód závady slovy a nastavení řidiče.

**Stáhnout:** [car-cockpit.prj32](car-cockpit.prj32) - otevři ho v editoru ctrl32 (**File → Open**).

## Co dělá

Pět obrazovek na 7" skle:

- **Cockpit** - rychloměr a otáčkoměr, převodový stupeň, palivo,
  chladicí kapalina a baterie, počitadlo kilometrů a denní počitadlo,
  hodiny, blinkry a výstražné kontrolky.
- **Engine** - hodnoty motoru podrobně.
- **Bus** - síť **J1939**: uzel panelu, motor, převodovka a brzdy a
  jestli odpovídají, kontrolky DM1, každý signál se svou skupinou
  parametrů.
- **Faults** - seznam alarmů a aktivní kód závady motoru (SPN / FMI /
  počet) s jeho významem slovy.
- **Settings** - demo režim, jednotky, varování před rychlostí, červené
  pole otáček, varování chladicí kapaliny a paliva, servisní interval.

Komunikace je **SAE J1939** na CAN desky (3,3V převodník na GPIO47 /
GPIO48, 250 kbit/s): motor, převodovka a brzdy vysílají své skupiny
parametrů a panel je čte - aby hodnota přišla, není potřeba žádný
program. V **demo režimu** (ve výchozím stavu zapnutý) program SIM
jede jízdní cyklus: rozjede se, řadí, jede ustálenou rychlostí, brzdí,
zastaví - a občas přijde závada.

## Obrazovky

**Kokpit**

![Obrazovka kokpitu: rychloměr a otáčkoměr, převodový stupeň, palivo, chladicí kapalina a výstražné kontrolky](img/cockpit.png)

**Sběrnice**

![Obrazovka sběrnice J1939: řídicí jednotky a signály, které panel čte](img/bus.png)

**Závady**

![Obrazovka závad: seznam alarmů a aktivní kód závady](img/faults.png)

## Otevři a spusť

1. Otevři `car-cockpit.prj32` v editoru.
2. Spusť ho tak, jak je, v demo režimu; ve vozidle připoj převodník CAN na GPIO47 / GPIO48 a vypni demo režim na obrazovce Settings.
3. Spusť **simulaci** (panel nástrojů) a vyzkoušej ho na PC, nebo ho nahraj do desky - viz [Nahrání runtime](../../install.cs.md).

## Co bys měl vidět

Panel naběhne v demo režimu: ručičky se hýbou podle jízdního cyklu,
převodový stupeň se mění, blinkry blikají. Vypni demo režim na
obrazovce Settings a připoj sběrnici - ukazatele pak zobrazují vozidlo.


---

[← Vzorové projekty](../README.cs.md) | [Přehled](../../README.cs.md)
