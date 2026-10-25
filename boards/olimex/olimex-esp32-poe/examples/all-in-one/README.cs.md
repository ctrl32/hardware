---
title: 'Olimex ESP32-PoE: příklad All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/screen.png
image_alt: Stránka operátora příkladu all-in-one pro desku Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- example
---

# All-in-one

Čerpadlo ovládané tlačítkem na desce, operátorskou stránkou a Home Assistant, se vstupem hladiny, časovačem chodu, alarmem hladiny a elektroměrem Modbus TCP.

**Stáhnout:** [all-in-one.prj32](all-in-one.prj32) - otevři ho v editoru ctrl32 (**File → Open**).

## Co dělá

Program je malé řízení čerpadla - tvar většiny strojů:

- **Start** přijde z tlačítka na desce (BUT1), z tlačítka **Start** na
  operátorské stránce nebo z Home Assistant přes MQTT.
- **Stop** přijde z tlačítka **Stop**, od nízké hladiny nebo po
  uplynutí doby chodu - paměť (latch) vypne výstup na GPIO33.
- **Hladina** je analogový vstup na GPIO35 (0 až 3,3 V přepočtené na
  0 až 100 %). Pod 10 % se čerpadlo zastaví a vznikne alarm; nad 15 %
  smí zase běžet (hystereze).
- **Doba chodu** se nastavuje na stránce v minutách a přežije výpadek
  napájení (remanentní proměnná).
- Elektroměr **Modbus TCP** v síti dává síťové napětí (registr 0,
  vstupní registry, unit 1 na 192.168.1.60 - změň na svůj elektroměr).
  Nad 253 V vznikne alarm.
- **CAN** (převodník na GPIO4 / GPIO36) posílá hladinu a stav čerpadla
  v rámci 0x181 každých 100 ms a přijímá žádanou hodnotu v 0x201.
- **MQTT** posílá hladinu, stav čerpadla a napětí do brokeru Home
  Assistant, který si je najde sám (discovery); čerpadlo jde spustit
  i z Home Assistant.
- **WEBview** zobrazuje operátorskou stránku - čerpadlo, hladinu, její
  průběh a alarmy - v libovolném prohlížeči v síti.

## Program

![Ladder program příkladu](img/ladder.png)

## Stránka operátora

![Stránka operátora v simulaci](img/screen.png)

## Otevři a spusť

1. Otevři `all-in-one.prj32` v editoru.
2. Změň adresy (zařízení Modbus, broker MQTT) na adresy své sítě.
3. Spusť **simulaci** (panel nástrojů) a vyzkoušej ho na PC, nebo ho nahraj do desky - viz [Nahrání runtime](../../install.cs.md).

## Co bys měl vidět

S vytočeným potenciometrem stiskni BUT1: relé na GPIO33 sepne a LED
čerpadla na stránce se rozsvítí. Otoč potenciometr pod 10 %: čerpadlo
se zastaví a v tabulce se objeví alarm. V Home Assistant se deska
objeví s hladinou, čerpadlem a napětím.


---

[← Vzorové projekty](../README.cs.md) | [Přehled](../../README.cs.md)
