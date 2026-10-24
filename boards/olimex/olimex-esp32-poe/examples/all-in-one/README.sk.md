---
title: 'Olimex ESP32-PoE: príklad All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/screen.png
image_alt: Stránka operátora príkladu all-in-one pre dosku Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- example
---

# All-in-one

Čerpadlo ovládané tlačidlom na doske, stránkou operátora a Home Assistant, so vstupom hladiny, časovačom chodu, alarmom hladiny a elektromerom Modbus TCP.

**Stiahnuť:** [all-in-one.prj32](all-in-one.prj32) - otvor ho v editore ctrl32 (**File → Open**).

## Čo robí

Program je malé riadenie čerpadla - tvar väčšiny strojov:

- **Štart** príde z tlačidla na doske (BUT1), z tlačidla **Start** na
  stránke operátora alebo z Home Assistant cez MQTT.
- **Stop** príde z tlačidla **Stop**, z nízkej hladiny alebo po
  uplynutí času chodu - pamäť (latch) vypne výstup na GPIO33.
- **Hladina** je analógový vstup na GPIO35 (0 až 3,3 V prepočítané na
  0 až 100 %). Pod 10 % sa čerpadlo zastaví a vznikne alarm; nad 15 %
  môže znova bežať (hysterézia).
- **Čas chodu** sa nastavuje na stránke v minútach a prežije výpadok
  napájania (zachovávaná premenná).
- Elektromer **Modbus TCP** v sieti dáva napätie siete (register 0,
  vstupné registre, unit 1 na 192.168.1.60 - zmeň na svoj elektromer).
  Nad 253 V vznikne alarm.
- **CAN** (prevodník na GPIO4 / GPIO36) posiela hladinu a stav čerpadla
  v rámci 0x181 každých 100 ms a prijíma žiadanú hodnotu v 0x201.
- **MQTT** posiela hladinu, stav čerpadla a napätie do brokera Home
  Assistant, ktorý si ich nájde sám (discovery); čerpadlo sa dá spustiť
  aj z Home Assistant.
- **WEBview** zobrazuje stránku operátora - čerpadlo, hladinu, jej
  priebeh a alarmy - v ľubovoľnom prehliadači v sieti.

## Program

![Ladder program príkladu](img/ladder.png)

## Stránka operátora

![Stránka operátora v simulácii](img/screen.png)

## Otvor a spusti

1. Otvor `all-in-one.prj32` v editore.
2. Zmeň adresy (zariadenie Modbus, broker MQTT) na adresy svojej siete.
3. Spusti **simuláciu** (panel nástrojov) a vyskúšaj ho na PC, alebo ho nahraj do dosky - pozri [Nahratie runtime](../../install.sk.md).

## Čo by si mal vidieť

S vytočeným potenciometrom stlač BUT1: relé na GPIO33 zopne a LED
čerpadla na stránke sa rozsvieti. Stoč potenciometer pod 10 %: čerpadlo
sa zastaví a v tabuľke sa objaví alarm. V Home Assistant sa doska objaví
s hladinou, čerpadlom a napätím.


---

[← Vzorové projekty](../README.sk.md) | [Prehľad](../../README.sk.md)
