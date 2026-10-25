---
title: 'Olimex ESP32-P4-PC: příklad All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/screen.png
image_alt: Stránka operátora příkladu all-in-one pro desku Olimex ESP32-P4-PC
tags:
- esp32-p4
- ethernet
- ups
- olimex
- example
---

# All-in-one

Výstup motoru se startem a stopem, dobou chodu, teplotou z Modbus RTU, rámci CAN, elektroměrem Modbus TCP, MQTT a stránkou operátora v prohlížeči.

**Stáhnout:** [all-in-one.prj32](all-in-one.prj32) - otevři ho v editoru ctrl32 (**File → Open**).

## Co dělá

Program je malé řízení stroje - tvar většiny strojů:

- **Start** přijde z tlačítka na GPIO14, z tlačítka **Start** na stránce operátora nebo z Home Assistant přes MQTT.
- **Stop** přijde z tlačítka **Stop**, z nízké hladiny nebo po uplynutí doby chodu - paměť (latch) vypne výstup na **GPIO2**.
- **Doba chodu** se nastavuje v minutách a přežije výpadek napájení.
- **Hladina** je proměnná nastavená na stránce (desce nezbyl volný analogový pin).
- Snímač **Modbus RTU** na RS-485 desky dává teplotu (unit 1, vstupní registr 1).
- **CAN** posílá hladinu a stav výstupu v rámci 0x181 každých 100 ms a přijímá žádanou hodnotu v rámci 0x201.
- Elektroměr **Modbus TCP** v síti dává odběr (192.168.1.60 - změň na adresu svého elektroměru).
- **MQTT** posílá hodnoty do brokeru Home Assistant, který si je najde sám; výstup lze spustit i z Home Assistant.
- **WEBview** zobrazí stránku operátora v libovolném prohlížeči v síti.

## Program

![Ladder program příkladu](img/ladder.png)

## Stránka operátora

![Stránka operátora v simulaci](img/screen.png)

## Otevři a spusť

1. Otevři `all-in-one.prj32` v editoru.
2. Změň adresy (zařízení Modbus, broker MQTT) na adresy své sítě.
3. Spusť **simulaci** (panel nástrojů) a vyzkoušej ho na PC, nebo ho nahraj do desky - viz [Nahrání runtime](../../install.cs.md).

## Co bys měl vidět

Stiskni tlačítko na GPIO14: výstup na GPIO2 se zapne a jeho LED na stránce se rozsvítí. Po uplynutí doby chodu se sám vypne. V Home Assistant se deska objeví se svými hodnotami.


---

[← Vzorové projekty](../README.cs.md) | [Přehled](../../README.cs.md)
