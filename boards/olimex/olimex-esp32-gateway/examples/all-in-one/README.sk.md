---
title: 'Olimex ESP32-GATEWAY: príklad All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-gateway/
image: img/screen.png
image_alt: Stránka operátora príkladu all-in-one pre dosku Olimex ESP32-GATEWAY
tags:
- esp32
- ethernet
- gateway
- olimex
- example
---

# All-in-one

Výstup motora so štartom a stopom, časom chodu, elektromerom Modbus TCP, MQTT a stránkou operátora v prehliadači.

**Stiahnuť:** [all-in-one.prj32](all-in-one.prj32) - otvor ho v editore ctrl32 (**File → Open**).

## Čo robí

Program je malé riadenie stroja - tvar väčšiny strojov:

- **Štart** príde z tlačidla na GPIO34, z tlačidla **Start** na stránke operátora alebo z Home Assistant cez MQTT.
- **Stop** príde z tlačidla **Stop**, z nízkej hladiny alebo po uplynutí času chodu - pamäť (latch) vypne výstup na **GPIO33**.
- **Čas chodu** sa nastavuje v minútach a prežije výpadok napájania.
- **Hladina** je premenná nastavená na stránke (doske neostal voľný analógový pin).
- Elektromer **Modbus TCP** v sieti dáva odber (192.168.1.60 - zmeň na adresu svojho elektromera).
- **MQTT** posiela hodnoty do brokera Home Assistant, ktorý si ich nájde sám; výstup sa dá spustiť aj z Home Assistant.
- **WEBview** zobrazí stránku operátora v ľubovoľnom prehliadači v sieti.

## Program

![Ladder program príkladu](img/ladder.png)

## Stránka operátora

![Stránka operátora v simulácii](img/screen.png)

## Otvor a spusti

1. Otvor `all-in-one.prj32` v editore.
2. Zmeň adresy (zariadenie Modbus, broker MQTT) na adresy svojej siete.
3. Spusti **simuláciu** (panel nástrojov) a vyskúšaj ho na PC, alebo ho nahraj do dosky - pozri [Nahratie runtime](../../install.sk.md).

## Čo by si mal vidieť

Stlač tlačidlo na GPIO34: výstup na GPIO33 sa zapne a jeho LED na stránke sa rozsvieti. Po uplynutí času chodu sa sám vypne. V Home Assistant sa doska objaví so svojimi hodnotami.


---

[← Vzorové projekty](../README.sk.md) | [Prehľad](../../README.sk.md)
