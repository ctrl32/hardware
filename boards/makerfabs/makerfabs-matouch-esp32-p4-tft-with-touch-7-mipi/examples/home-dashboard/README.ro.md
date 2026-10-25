---
title: 'Makerfabs MaTouch ESP32-P4 7": exemplul Home dashboard'
slug: home-dashboard
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.jpg
image_alt: Pagina operatorului din exemplul home dashboard pentru Makerfabs MaTouch ESP32-P4 7"
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

Un panou de comandă pentru toată casa, în stil întunecat de sticlă mată - încălzire pe fiecare cameră, energie cu fotovoltaice și baterie, lumini, garajul și vremea - cu o casă simulată în spate.

**Descărcare:** [home-dashboard.prj32](home-dashboard.prj32) - deschide-l în editorul ctrl32 (**File → Open**).

## Ce face

Șase ecrane peste fotografii ale casei, fiecare un set de carduri de
sticlă mată:

- **Home** - ora, vremea, camerele, alarma și scenele.
- **Weather** - azi și zilele următoare.
- **Climate** - șase camere, fiecare cu temperatura ei, valoarea de
  referință și încălzirea; pompa de căldură și boilerul de apă caldă.
- **Energy** - producția fotovoltaică, consumul casei, bateria și
  rețeaua, kWh-ii zilei.
- **Lights** - luminile camerelor și scenele lor.
- **Access** - ușa garajului, încărcătorul mașinii, alarma.

Programul **SIM** este casa: temperatura exterioară urmează ziua,
producția fotovoltaică soarele, consumul are vârfurile de dimineață și
de seară, camerele se încălzesc cu histerezis până la valorile lor de
referință. Înlocuiește variabilele lui cu dispozitivele tale Modbus,
MQTT sau CAN pentru a comanda o casă reală.

## Ecranele

**Acasă**

![Ecranul Home al dashboard-ului: ora, vremea, camerele, alarma și scenele](img/home.jpg)

**Climat**

![Ecranul Climate: șase camere cu temperaturile și valorile lor de referință](img/climate.png)

**Energie**

![Ecranul Energy: fotovoltaice, consumul casei, bateria și rețeaua](img/energy.jpg)

## Deschide-l și rulează-l

1. Deschide `home-dashboard.prj32` în editor.
2. Rulează-l așa cum este - casa este simulată; pentru o casă reală înlocuiește variabilele programului SIM cu dispozitivele tale.
3. Pornește **simularea** (bara de instrumente) pentru a-l încerca pe PC sau descarcă-l pe placă - vezi [Instalarea runtime-ului](../../install.ro.md).

## Ce ar trebui să vezi

Ecranul Home apare cu ora, vremea și camerele; valorile se mișcă pe
măsură ce trece ziua simulată. O atingere pe valoarea de referință a
unei camere o schimbă, iar camera se încălzește până la ea.


---

[← Proiecte exemplu](../README.ro.md) | [Prezentare](../../README.ro.md)
