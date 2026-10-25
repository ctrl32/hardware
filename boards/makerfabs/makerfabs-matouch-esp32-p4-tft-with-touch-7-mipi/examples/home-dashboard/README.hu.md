---
title: 'Makerfabs MaTouch ESP32-P4 7": Home dashboard példa'
slug: home-dashboard
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.jpg
image_alt: A(z) Makerfabs MaTouch ESP32-P4 7" home dashboard példájának kezelőoldala
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Home dashboard

Az egész ház vezérlőpanelje sötét, matt üveg stílusban - helyiségenkénti fűtés, energia napelemmel és akkumulátorral, világítás, a garázs és az időjárás -, mögötte egy szimulált házzal.

**Letöltés:** [home-dashboard.prj32](home-dashboard.prj32) - nyisd meg a ctrl32 szerkesztőben (**File → Open**).

## Mit csinál

Hat képernyő a ház fényképei fölött, mindegyik matt üveg kártyák
sorozata:

- **Home** - az idő, az időjárás, a helyiségek, a riasztó és a
  jelenetek.
- **Weather** - a mai nap és a következő napok.
- **Climate** - hat helyiség, mindegyik a hőmérsékletével, az
  alapjelével és a fűtéssel; a hőszivattyú és a melegvíz-tartály.
- **Energy** - a napelemek teljesítménye, a ház fogyasztása, az
  akkumulátor és a hálózat, a nap kWh-i.
- **Lights** - a helyiségek világítása és a jeleneteik.
- **Access** - a garázskapu, az autótöltő, a riasztó.

A **SIM** program maga a ház: a külső hőmérséklet követi a napszakot, a
napelemek teljesítménye a napot, a fogyasztásnak reggeli és esti csúcsa
van, a helyiségek hiszterézissel fűtenek az alapjelükre. Cseréld le a
változóit a Modbus, MQTT vagy CAN eszközeidre, hogy egy valódi házat
vezérelj.

## A képernyők

**Kezdőlap**

![A dashboard Home képernyője: idő, időjárás, helyiségek, riasztó és jelenetek](img/home.jpg)

**Klíma**

![A Climate képernyő: hat helyiség a hőmérsékletükkel és az alapjeleikkel](img/climate.png)

**Energia**

![Az Energy képernyő: napelemek, a ház fogyasztása, akkumulátor és hálózat](img/energy.jpg)

## Megnyitás és futtatás

1. Nyisd meg a `home-dashboard.prj32` fájlt a szerkesztőben.
2. Futtasd úgy, ahogy van - a ház szimulált; valódi házhoz cseréld le a SIM program változóit a saját eszközeidre.
3. Indítsd el a **szimulációt** (eszköztár), hogy kipróbáld a PC-n, vagy töltsd le a panelre - lásd [A runtime telepítése](../../install.hu.md).

## Amit látnod kell

A Home képernyő megjelenik az idővel, az időjárással és a
helyiségekkel; az értékek változnak, ahogy a szimulált nap telik. Egy
helyiség alapjelére koppintva megváltoztatod azt, és a helyiség
felfűt rá.


---

[← Példaprojektek](../README.hu.md) | [Áttekintés](../../README.hu.md)
