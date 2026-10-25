---
title: 'Makerfabs MaTouch ESP32-P4 7": příklad Flexo press on a SIMATIC'
slug: flexo-press-simatic
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Stránka operátora příkladu flexo press on a simatic pro desku Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Flexo press on a SIMATIC

HMI osmibarevného flexotiskového stroje řízeného PLC SIMATIC S7-1200 - stroj s pohybujícím se pásem, šestnáct tiskových servopohonů, soutisk, sušiče, zakázky jako receptury a diagnostika, přes protokol S7.

**Stáhnout:** [flexo-press-simatic.prj32](flexo-press-simatic.prj32) - otevři ho v editoru ctrl32 (**File → Open**).

## Co dělá

Šest stránek na světlém průmyslovém panelu:

- **Overview** - stroj jako výkres, po kterém se pohybuje pás,
  kontrolky synchronizace sekcí, teploty sušičů, tahy pásu a délky
  rolí; START (s potvrzením), STOP, JOG, RESET.
- **Sections** - šestnáct tiskových servopohonů: tiskové válce a
  aniloxy, synchronizace, porucha, rychlost, povolení.
- **Register** - chyba soutisku každé sekce a její korekce.
- **Heating** - sušicí komory a mostový sušič.
- **Jobs** - zakázka jako **receptura** uložená v panelu: načíst,
  uložit, smazat.
- **Diagnostics** - alarmy, spojení s PLC a trend rychlosti a tahu.

Panel komunikuje s PLC **SIMATIC S7-1200** přes **+7** (protokol S7,
ISO-on-TCP): každých 100 ms čte stavový blok PLC DB100 a do DB101
zapisuje žádané hodnoty a příkazy - v PLC není potřeba nic jiného.
V **demo režimu** (ve výchozím stavu zapnutý) program SIM provozuje
stroj přímo v panelu.

## Obrazovky

**Přehled**

![Stránka přehledu: výkres stroje s pohybujícím se pásem, tahy a sušiče](img/overview.png)

**Sekce**

![Stránka sekcí: šestnáct tiskových servopohonů s jejich stavem](img/sections.png)

**Zakázky**

![Stránka zakázek: zakázka jako receptura uložená v panelu](img/jobs.png)

## Otevři a spusť

1. Otevři `flexo-press-simatic.prj32` v editoru.
2. Spusť ho tak, jak je, v demo režimu; s PLC nastav jeho adresu na stránce +7 a vytvoř dva datové bloky DB100 / DB101.
3. Spusť **simulaci** (panel nástrojů) a vyzkoušej ho na PC, nebo ho nahraj do desky - viz [Nahrání runtime](../../install.cs.md).

## Co bys měl vidět

Přehled naběhne v demo režimu. Stiskni START a potvrď: linka se
rozjede, pás se pohybuje po výkresu a tahy se ustálí. Vypni demo režim
na stránce Diagnostics a nastav adresu PLC - panel pak zobrazuje
skutečný stroj.


---

[← Vzorové projekty](../README.cs.md) | [Přehled](../../README.cs.md)
