---
title: 'Makerfabs MaTouch ESP32-P4 7": příklad Home dashboard'
slug: home-dashboard
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.jpg
image_alt: Stránka operátora příkladu home dashboard pro desku Makerfabs MaTouch ESP32-P4 7"
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

Ovládací panel celého domu v tmavém stylu matného skla - topení po místnostech, energie s FV a baterií, světla, garáž a počasí - se simulovaným domem v pozadí.

**Stáhnout:** [home-dashboard.prj32](home-dashboard.prj32) - otevři ho v editoru ctrl32 (**File → Open**).

## Co dělá

Šest obrazovek nad fotografiemi domu, každá je sada matných karet:

- **Home** - čas, počasí, místnosti, alarm a scény.
- **Weather** - dnešek a další dny.
- **Climate** - šest místností, každá se svou teplotou, žádanou
  hodnotou a topením; tepelné čerpadlo a zásobník teplé vody.
- **Energy** - výkon FV, odběr domu, baterie a síť, kWh za den.
- **Lights** - světla v místnostech a jejich scény.
- **Access** - garážová vrata, nabíječka auta, alarm.

Program **SIM** je dům: venkovní teplota sleduje den, výkon FV slunce,
odběr má ranní a večerní špičku, místnosti se s hysterezí vytápějí na
své žádané hodnoty. Nahraď jeho proměnné svými zařízeními Modbus, MQTT
nebo CAN a budeš řídit skutečný dům.

## Obrazovky

**Domů**

![Domovská obrazovka panelu: čas, počasí, místnosti, alarm a scény](img/home.jpg)

**Klima**

![Obrazovka klimatu: šest místností s jejich teplotami a žádanými hodnotami](img/climate.png)

**Energie**

![Obrazovka energie: FV, odběr domu, baterie a síť](img/energy.jpg)

## Otevři a spusť

1. Otevři `home-dashboard.prj32` v editoru.
2. Spusť ho tak, jak je - dům je simulovaný; pro skutečný dům nahraď proměnné programu SIM svými zařízeními.
3. Spusť **simulaci** (panel nástrojů) a vyzkoušej ho na PC, nebo ho nahraj do desky - viz [Nahrání runtime](../../install.cs.md).

## Co bys měl vidět

Objeví se domovská obrazovka s časem, počasím a místnostmi; hodnoty se
hýbou, jak plyne simulovaný den. Klepnutím na žádanou hodnotu
místnosti ji změníš a místnost se na ni vytopí.


---

[← Vzorové projekty](../README.cs.md) | [Přehled](../../README.cs.md)
