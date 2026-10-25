---
title: 'Olimex ESP32-PoE: All-in-one példa'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/screen.png
image_alt: A(z) Olimex ESP32-PoE all-in-one példájának kezelőoldala
tags:
- esp32
- ethernet
- poe
- olimex
- example
---

# All-in-one

Egy szivattyú, amelyet a panel gombja, a kezelőoldal és Home Assistant vezérel, szintbemenettel, futásidő-időzítővel, szintriasztással és egy Modbus TCP fogyasztásmérővel.

**Letöltés:** [all-in-one.prj32](all-in-one.prj32) - nyisd meg a ctrl32 szerkesztőben (**File → Open**).

## Mit csinál

A program egy kis szivattyúvezérlés - a legtöbb gép ilyen felépítésű:

- A **Start** jöhet a panel gombjáról (BUT1), a kezelőoldal **Start**
  gombjáról vagy Home Assistantból MQTT-n keresztül.
- A **Stop** jöhet a **Stop** gombról, alacsony szintből vagy a
  futásidő lejártából - az öntartás ilyenkor lekapcsolja a GPIO33
  kimenetet.
- A **szint** egy analóg bemenet a GPIO35-ön (0-3,3 V 0-100 %-ra
  skálázva). 10 % alatt a szivattyú leáll és riasztás keletkezik;
  15 % felett újra indulhat (hiszterézis).
- A **futásidőt** az oldalon percben adod meg, és áramszünet után is
  megmarad (megőrzött változó).
- A hálózaton egy **Modbus TCP** fogyasztásmérő adja a hálózati
  feszültséget (0-s regiszter, bemeneti regiszterek, unit 1 a
  192.168.1.60 címen - írd át a saját mérődre). 253 V felett riasztás
  keletkezik.
- A **CAN** (egy adó-vevő a GPIO4 / GPIO36 lábon) 100 ms-onként
  elküldi a szintet és a szivattyú állapotát a 0x181 keretben, és
  alapjelet fogad a 0x201 keretben.
- Az **MQTT** közzéteszi a szintet, a szivattyú állapotát és a
  feszültséget egy Home Assistant brókernek, amely magától megtalálja
  őket (discovery); a szivattyú Home Assistantból is elindítható.
- A **WEBview** a kezelőoldalt - a szivattyút, a szintet, annak
  trendjét és a riasztásokat - a hálózat bármely böngészőjének
  kiszolgálja.

## A program

![A példa létraprogramja](img/ladder.png)

## A kezelőoldal

![A kezelőoldal a szimulációban](img/screen.png)

## Megnyitás és futtatás

1. Nyisd meg a `all-in-one.prj32` fájlt a szerkesztőben.
2. Írd át a címeket (a Modbus eszközét, az MQTT brókerét) a saját hálózatodéira.
3. Indítsd el a **szimulációt** (eszköztár), hogy kipróbáld a PC-n, vagy töltsd le a panelre - lásd [A runtime telepítése](../../install.hu.md).

## Amit látnod kell

Tekerd fel a potenciométert, és nyomd meg a BUT1 gombot: a GPIO33
reléje bekapcsol, és a szivattyú LED-je világít az oldalon. Tekerd le a
potenciométert 10 % alá: a szivattyú leáll, és a riasztás megjelenik a
táblázatban. Home Assistantban a panel megjelenik a szintjével, a
szivattyúval és a feszültséggel.


---

[← Példaprojektek](../README.hu.md) | [Áttekintés](../../README.hu.md)
