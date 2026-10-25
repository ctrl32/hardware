---
title: 'Makerfabs MaTouch ESP32-P4 7": Car cockpit példa'
slug: car-cockpit
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: A(z) Makerfabs MaTouch ESP32-P4 7" car cockpit példájának kezelőoldala
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

Műszerfal egy J1939 járműbuszon - sebesség- és fordulatszámmérő, fokozat, üzemanyag, hűtőfolyadék, a figyelmeztető lámpák, a buszon lévő vezérlőegységek, az aktív hibakód szavakban és a vezető beállításai.

**Letöltés:** [car-cockpit.prj32](car-cockpit.prj32) - nyisd meg a ctrl32 szerkesztőben (**File → Open**).

## Mit csinál

Öt képernyő a 7"-os kijelzőn:

- **Cockpit** - sebesség- és fordulatszámmérő, a fokozat, üzemanyag,
  hűtőfolyadék és akkumulátor, a kilométer-számláló és a napi
  számláló, az óra, az irányjelzők és a figyelmeztető lámpák.
- **Engine** - a motor értékei részletesen.
- **Bus** - a **J1939** hálózat: a panel csomópontja, a motor, a
  sebességváltó és a fékek, és hogy válaszolnak-e, a DM1 lámpák,
  minden jel a paramétercsoportjával.
- **Faults** - a riasztáslista és a motor aktív hibakódja
  (SPN / FMI / szám) a jelentésével szavakban.
- **Settings** - demó mód, mértékegységek, a sebességfigyelmeztetés, a
  piros tartomány, a hűtőfolyadék- és üzemanyag-figyelmeztetések, a
  szervizintervallum.

A kommunikáció **SAE J1939** a panel CAN-ján (egy 3,3 V-os adó-vevő a
GPIO47 / GPIO48 lábon, 250 kbit/s): a motor, a sebességváltó és a fékek
sugározzák a paramétercsoportjaikat, a panel pedig olvassa őket -
ahhoz, hogy egy érték megérkezzen, nem kell program. **Demó módban**
(alapértelmezés szerint be van kapcsolva) a SIM program egy ciklust
játszik le: elindul, vált, egyenletesen halad, fékez, megáll - és
időnként egy hiba.

## A képernyők

**Műszerfal**

![A Cockpit képernyő: sebesség- és fordulatszámmérő, fokozat, üzemanyag, hűtőfolyadék és a figyelmeztető lámpák](img/cockpit.png)

**Busz**

![A J1939 Bus képernyő: a vezérlőegységek és a jelek, amelyeket a panel olvas](img/bus.png)

**Hibák**

![A Faults képernyő: a riasztáslista és az aktív hibakód](img/faults.png)

## Megnyitás és futtatás

1. Nyisd meg a `car-cockpit.prj32` fájlt a szerkesztőben.
2. Futtasd úgy, ahogy van, demó módban; járművön kösd a CAN adó-vevőt a GPIO47 / GPIO48 lábra, és kapcsold ki a demó módot a Settings képernyőn.
3. Indítsd el a **szimulációt** (eszköztár), hogy kipróbáld a PC-n, vagy töltsd le a panelre - lásd [A runtime telepítése](../../install.hu.md).

## Amit látnod kell

A műszerfal demó módban jelenik meg: a mutatók végigmennek a
menetcikluson, a fokozat váltakozik, az irányjelzők villognak. Kapcsold
ki a demó módot a Settings képernyőn, és csatlakoztasd a buszt - a
műszerek ezután a járművet mutatják.


---

[← Példaprojektek](../README.hu.md) | [Áttekintés](../../README.hu.md)
