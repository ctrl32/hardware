---
title: 'Makerfabs MaTouch ESP32-P4 7": příklad All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Stránka operátora příkladu all-in-one pro desku Makerfabs MaTouch ESP32-P4 7"
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

Motor ovládaný z dotykové obrazovky, dvěma tlačítky a z Home Assistantu, s ukazatelem tlaku, ventilátorem podle teploty z Modbus RTU, elektroměrem Modbus TCP, rámci CAN, trendem a alarmy.

**Stáhnout:** [all-in-one.prj32](all-in-one.prj32) - otevři ho v editoru ctrl32 (**File → Open**).

## Co dělá

Program je malé řízení stroje:

- **Start** přijde z tlačítka na GPIO47, z tlačítka **Start** na
  obrazovce nebo z Home Assistantu přes MQTT; **Stop** z tlačítka na
  GPIO48, z tlačítka **Stop** na obrazovce, nebo když tlak stoupne nad
  žádanou hodnotu, která přichází přes **CAN** (rámec 0x201).
- Samodržný obvod (latch) ovládá výstup motoru na **GPIO33**;
  počitadlo drží počet startů i přes výpadek napájení.
- **Tlak** je analogový vstup přes **ADS1115** na sběrnici I2C (0-10 V
  přes dělič 1:4, 0-10 bar) a každých 100 ms odchází přes CAN (rámec
  0x181).
- **Teplota** přichází z čidla **Modbus RTU** (unit 1, vstupní
  registr 1, 0,1 °C); ventilátor ji sleduje s hysterezí.
- Elektroměr **Modbus TCP** dává odebíraný výkon.
- Tři **obrazovky** na skle: přehled, trend a alarmy; jednodušší
  stránka v libovolném prohlížeči (WEBview).

## Program

![Ladder program příkladu](img/ladder.png)

## Stránka operátora

![Stránka operátora v simulaci](img/screen.png)

## Otevři a spusť

1. Otevři `all-in-one.prj32` v editoru.
2. Změň adresy (zařízení Modbus, broker MQTT) na adresy své sítě.
3. Spusť **simulaci** (panel nástrojů) a vyzkoušej ho na PC, nebo ho nahraj do desky - viz [Nahrání runtime](../../install.cs.md).

## Co bys měl vidět

Na skle se objeví přehled. Stiskni **Start**: LED motoru se rozsvítí a
počitadlo startů se zvýší. Ukazatel zobrazuje tlak, obrazovka Trend ho
kreslí spolu s teplotou, a když tlak překročí 8 bar, na obrazovce
Alarms se objeví alarm.


---

[← Vzorové projekty](../README.cs.md) | [Přehled](../../README.cs.md)
