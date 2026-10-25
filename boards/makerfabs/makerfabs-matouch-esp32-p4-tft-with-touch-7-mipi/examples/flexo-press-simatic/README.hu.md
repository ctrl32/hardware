---
title: 'Makerfabs MaTouch ESP32-P4 7": Flexo press on a SIMATIC példa'
slug: flexo-press-simatic
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: A(z) Makerfabs MaTouch ESP32-P4 7" flexo press on a simatic példájának kezelőoldala
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

Egy SIMATIC S7-1200 által vezérelt nyolcszínes flexonyomógép HMI-je - a gép a futó pályával, tizenhat nyomóművi szervó, a regiszter, a szárítók, a munkák receptként és a diagnosztika, az S7 protokollon keresztül.

**Letöltés:** [flexo-press-simatic.prj32](flexo-press-simatic.prj32) - nyisd meg a ctrl32 szerkesztőben (**File → Open**).

## Mit csinál

Hat oldal egy világos ipari panelen:

- **Overview** - a gép rajzként, rajta a futó pályával, a nyomóművek
  szinkronlámpái, a szárítók hőmérséklete, a pályafeszültségek és a
  tekercshosszak; START (megerősítéssel), STOP, JOG, RESET.
- **Sections** - a tizenhat nyomóművi szervó: nyomóformahengerek és
  aniloxhengerek, szinkronban, hiba, fordulatszám, engedélyezve.
- **Register** - minden nyomómű regiszterhibája és a korrekció.
- **Heating** - a szárítókamrák és a hídszárító.
- **Jobs** - a munka a panelen tárolt **receptként**: betöltés,
  mentés, törlés.
- **Diagnostics** - a riasztások, a PLC kapcsolat és a sebesség és a
  pályafeszültség trendje.

A panel egy **SIMATIC S7-1200**-zal beszél a **+7**-en keresztül (az
S7 protokoll, ISO-on-TCP): 100 ms-onként kiolvassa a PLC DB100
állapotblokkját, és a DB101-be írja az alapjeleit és parancsait - a
PLC-ben ennél többre nincs szükség. **Demó módban** (alapértelmezés
szerint be van kapcsolva) a SIM program magán a panelen futtatja a
gépet.

## A képernyők

**Áttekintés**

![Az Overview oldal: a gép rajza a futó pályával, a pályafeszültségekkel és a szárítókkal](img/overview.png)

**Nyomóművek**

![A Sections oldal: tizenhat nyomóművi szervó az állapotukkal](img/sections.png)

**Munkák**

![A Jobs oldal: a munka a panelen tárolt receptként](img/jobs.png)

## Megnyitás és futtatás

1. Nyisd meg a `flexo-press-simatic.prj32` fájlt a szerkesztőben.
2. Futtasd úgy, ahogy van, demó módban; PLC-vel állítsd be a címét a +7 oldalon, és hozd létre a két adatblokkot, a DB100-at és a DB101-et.
3. Indítsd el a **szimulációt** (eszköztár), hogy kipróbáld a PC-n, vagy töltsd le a panelre - lásd [A runtime telepítése](../../install.hu.md).

## Amit látnod kell

Az áttekintés demó módban jelenik meg. Nyomd meg a START gombot, és
erősítsd meg: a gép felgyorsul, a pálya végigfut a rajzon, és a
pályafeszültségek beállnak. Kapcsold ki a demó módot a Diagnostics
oldalon, és állítsd be a PLC címét - a panel ezután a valódi gépet
mutatja.


---

[← Példaprojektek](../README.hu.md) | [Áttekintés](../../README.hu.md)
