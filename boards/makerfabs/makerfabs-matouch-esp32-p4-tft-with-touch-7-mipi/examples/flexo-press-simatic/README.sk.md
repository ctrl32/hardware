---
title: 'Makerfabs MaTouch ESP32-P4 7": príklad Flexo press on a SIMATIC'
slug: flexo-press-simatic
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Stránka operátora príkladu flexo press on a simatic pre dosku Makerfabs MaTouch ESP32-P4 7"
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

HMI osemfarebného flexotlačového stroja riadeného SIMATIC S7-1200 - stroj s pohybujúcim sa pásom, šestnásť tlačových servopohonov, register, sušiče, zákazky ako recepty a diagnostika, cez protokol S7.

**Stiahnuť:** [flexo-press-simatic.prj32](flexo-press-simatic.prj32) - otvor ho v editore ctrl32 (**File → Open**).

## Čo robí

Šesť stránok na svetlom priemyselnom paneli:

- **Overview** - stroj ako výkres, po ktorom sa hýbe pás, kontrolky
  synchronizácie sekcií, teploty sušičov, ťahy pásu a dĺžky rolí;
  START (s potvrdením), STOP, JOG, RESET.
- **Sections** - šestnásť tlačových servopohonov: tlačové valce a
  aniloxy, synchronizácia, porucha, rýchlosť, povolenie.
- **Register** - chyba registra každej sekcie a korekcia.
- **Heating** - sušiace komory a mostový sušič.
- **Jobs** - zákazka ako **recept** uložený v paneli: načítať, uložiť,
  zmazať.
- **Diagnostics** - alarmy, spojenie s PLC a priebeh rýchlosti a ťahu.

Panel komunikuje so **SIMATIC S7-1200** cez **+7** (protokol S7,
ISO-on-TCP): každých 100 ms číta stavový blok PLC DB100 a do DB101
zapisuje žiadané hodnoty a príkazy - v PLC netreba nič iné. V **demo
režime** (štandardne zapnutý) program SIM prevádzkuje stroj priamo v
paneli.

## Obrazovky

**Prehľad**

![Stránka prehľadu: výkres stroja s pohybujúcim sa pásom, ťahy a sušiče](img/overview.png)

**Sekcie**

![Stránka sekcií: šestnásť tlačových servopohonov s ich stavom](img/sections.png)

**Zákazky**

![Stránka zákaziek: zákazka ako recept uložený v paneli](img/jobs.png)

## Otvor a spusti

1. Otvor `flexo-press-simatic.prj32` v editore.
2. Spusti ho tak, ako je, v demo režime; s PLC nastav jeho adresu na stránke +7 a vytvor dva dátové bloky DB100 / DB101.
3. Spusti **simuláciu** (panel nástrojov) a vyskúšaj ho na PC, alebo ho nahraj do dosky - pozri [Nahratie runtime](../../install.sk.md).

## Čo by si mal vidieť

Prehľad nabehne v demo režime. Stlač START a potvrď: linka sa rozbehne,
pás sa hýbe po výkrese a ťahy sa ustália. Vypni demo režim na stránke
Diagnostics a nastav adresu PLC - panel potom zobrazuje skutočný stroj.


---

[← Vzorové projekty](../README.sk.md) | [Prehľad](../../README.sk.md)
