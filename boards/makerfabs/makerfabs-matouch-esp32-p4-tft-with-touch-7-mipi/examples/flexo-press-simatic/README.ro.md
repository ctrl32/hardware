---
title: 'Makerfabs MaTouch ESP32-P4 7": exemplul Flexo press on a SIMATIC'
slug: flexo-press-simatic
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Pagina operatorului din exemplul flexo press on a simatic pentru Makerfabs MaTouch ESP32-P4 7"
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

HMI-ul unei prese flexografice în opt culori comandate de un SIMATIC S7-1200 - presa cu banda în mișcare, șaisprezece servo de tipar, registrul, uscătoarele, comenzile ca rețete și diagnosticul, prin protocolul S7.

**Descărcare:** [flexo-press-simatic.prj32](flexo-press-simatic.prj32) - deschide-l în editorul ctrl32 (**File → Open**).

## Ce face

Șase pagini pe un panou industrial luminos:

- **Overview** - presa ca desen cu banda mișcându-se peste el, lămpile
  de sincronizare ale secțiunilor, temperaturile uscătoarelor,
  tensiunile benzii și lungimile rolelor; START (cu confirmare), STOP,
  JOG, RESET.
- **Sections** - cele șaisprezece servo de tipar: cilindri port-clișeu
  și anilox, sincronizat, defect, viteză, activat.
- **Register** - eroarea de registru a fiecărei secțiuni și corecția.
- **Heating** - camerele de uscare și uscătorul punte.
- **Jobs** - comanda ca **rețetă** păstrată pe panou: încărcare,
  salvare, ștergere.
- **Diagnostics** - alarmele, legătura cu PLC-ul și un trend al vitezei
  și tensiunii.

Panoul comunică cu un **SIMATIC S7-1200** prin **+7** (protocolul S7,
ISO-on-TCP): citește blocul de stare DB100 al PLC-ului la fiecare
100 ms și scrie valorile de referință și comenzile în DB101 - în PLC nu
mai e nevoie de nimic altceva. În **modul demo** (activ implicit)
programul SIM rulează presa chiar pe panou.

## Ecranele

**Prezentare**

![Pagina Overview: desenul presei cu banda în mișcare, tensiunile și uscătoarele](img/overview.png)

**Secțiuni**

![Pagina Sections: șaisprezece servo de tipar cu starea lor](img/sections.png)

**Comenzi**

![Pagina Jobs: comanda ca rețetă păstrată pe panou](img/jobs.png)

## Deschide-l și rulează-l

1. Deschide `flexo-press-simatic.prj32` în editor.
2. Rulează-l așa cum este, în modul demo; cu un PLC setează-i adresa pe pagina +7 și creează cele două blocuri de date DB100 / DB101.
3. Pornește **simularea** (bara de instrumente) pentru a-l încerca pe PC sau descarcă-l pe placă - vezi [Instalarea runtime-ului](../../install.ro.md).

## Ce ar trebui să vezi

Prezentarea generală apare în modul demo. Apasă START și confirmă:
linia accelerează, banda se mișcă peste desen și tensiunile se
stabilizează. Oprește modul demo pe pagina Diagnostics și setează
adresa PLC-ului - panoul arată atunci presa reală.


---

[← Proiecte exemplu](../README.ro.md) | [Prezentare](../../README.ro.md)
