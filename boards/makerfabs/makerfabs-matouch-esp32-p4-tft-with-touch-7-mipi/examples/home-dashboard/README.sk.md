---
title: 'Makerfabs MaTouch ESP32-P4 7": príklad Home dashboard'
slug: home-dashboard
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.jpg
image_alt: Stránka operátora príkladu home dashboard pre dosku Makerfabs MaTouch ESP32-P4 7"
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

Ovládací panel celého domu v tmavom štýle matného skla - kúrenie po miestnostiach, energia s FV a batériou, svetlá, garáž a počasie - so simulovaným domom za ním.

**Stiahnuť:** [home-dashboard.prj32](home-dashboard.prj32) - otvor ho v editore ctrl32 (**File → Open**).

## Čo robí

Šesť obrazoviek nad fotografiami domu, každá je sada matných kariet:

- **Home** - čas, počasie, miestnosti, alarm a scény.
- **Weather** - dnešok a ďalšie dni.
- **Climate** - šesť miestností, každá so svojou teplotou, žiadanou
  hodnotou a kúrením; tepelné čerpadlo a zásobník teplej vody.
- **Energy** - výkon FV, odber domu, batéria a sieť, kWh za deň.
- **Lights** - svetlá miestností a ich scény.
- **Access** - garážová brána, nabíjačka auta, alarm.

Program **SIM** je dom: vonkajšia teplota sleduje deň, výkon FV slnko,
odber má rannú a večernú špičku, miestnosti sa s hysteréziou vykurujú
na svoje žiadané hodnoty. Nahraď jeho premenné svojimi zariadeniami
Modbus, MQTT alebo CAN a budeš riadiť skutočný dom.

## Obrazovky

**Domov**

![Domovská obrazovka panelu: čas, počasie, miestnosti, alarm a scény](img/home.jpg)

**Klíma**

![Obrazovka klímy: šesť miestností s ich teplotami a žiadanými hodnotami](img/climate.png)

**Energia**

![Obrazovka energie: FV, odber domu, batéria a sieť](img/energy.jpg)

## Otvor a spusti

1. Otvor `home-dashboard.prj32` v editore.
2. Spusti ho tak, ako je - dom je simulovaný; pre skutočný dom nahraď premenné programu SIM svojimi zariadeniami.
3. Spusti **simuláciu** (panel nástrojov) a vyskúšaj ho na PC, alebo ho nahraj do dosky - pozri [Nahratie runtime](../../install.sk.md).

## Čo by si mal vidieť

Objaví sa domovská obrazovka s časom, počasím a miestnosťami; hodnoty
sa hýbu, ako plynie simulovaný deň. Ťuknutím na žiadanú hodnotu
miestnosti ju zmeníš a miestnosť sa na ňu vykúri.


---

[← Vzorové projekty](../README.sk.md) | [Prehľad](../../README.sk.md)
