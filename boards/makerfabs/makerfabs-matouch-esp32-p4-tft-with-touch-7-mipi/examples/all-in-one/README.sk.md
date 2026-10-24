---
title: 'Makerfabs MaTouch ESP32-P4 7": príklad All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Stránka operátora príkladu all-in-one pre dosku Makerfabs MaTouch ESP32-P4 7"
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

Motor ovládaný z dotykovej obrazovky, dvoma tlačidlami a z Home Assistant, s ukazovateľom tlaku, ventilátorom podľa teploty z Modbus RTU, elektromerom Modbus TCP, rámcami CAN, priebehom a alarmami.

**Stiahnuť:** [all-in-one.prj32](all-in-one.prj32) - otvor ho v editore ctrl32 (**File → Open**).

## Čo robí

Program je malé riadenie stroja:

- **Štart** príde z tlačidla na GPIO47, zo **Start** na obrazovke alebo
  z Home Assistant cez MQTT; **Stop** z tlačidla na GPIO48, zo **Stop**
  na obrazovke alebo keď tlak stúpne nad žiadanú hodnotu, ktorá
  prichádza cez **CAN** (rámec 0x201).
- Pamäť (latch) ovláda výstup motora na **GPIO33**; počítadlo drží
  počet štartov aj cez výpadok napájania.
- **Tlak** je analógový vstup cez **ADS1115** na zbernici I2C (0-10 V
  cez delič 1:4, 0-10 bar) a každých 100 ms ide von cez CAN (rámec
  0x181).
- **Teplota** prichádza zo senzora **Modbus RTU** (unit 1, vstupný
  register 1, 0,1 °C); ventilátor ju sleduje s hysteréziou.
- Elektromer **Modbus TCP** dáva odoberaný výkon.
- Tri **obrazovky** na skle: prehľad, priebeh a alarmy; jednoduchšia
  stránka v ľubovoľnom prehliadači (WEBview).

## Program

![Ladder program príkladu](img/ladder.png)

## Stránka operátora

![Stránka operátora v simulácii](img/screen.png)

## Otvor a spusti

1. Otvor `all-in-one.prj32` v editore.
2. Zmeň adresy (zariadenie Modbus, broker MQTT) na adresy svojej siete.
3. Spusti **simuláciu** (panel nástrojov) a vyskúšaj ho na PC, alebo ho nahraj do dosky - pozri [Nahratie runtime](../../install.sk.md).

## Čo by si mal vidieť

Na skle sa objaví prehľad. Stlač **Start**: LED motora sa rozsvieti a
počítadlo štartov stúpne. Ukazovateľ zobrazuje tlak, obrazovka Trend ho
kreslí spolu s teplotou a keď tlak prekročí 8 bar, na obrazovke Alarms
sa objaví alarm.


---

[← Vzorové projekty](../README.sk.md) | [Prehľad](../../README.sk.md)
