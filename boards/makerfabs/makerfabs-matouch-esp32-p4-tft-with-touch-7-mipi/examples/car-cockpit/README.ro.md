---
title: 'Makerfabs MaTouch ESP32-P4 7": exemplul Car cockpit'
slug: car-cockpit
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: Pagina operatorului din exemplul car cockpit pentru Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Car cockpit

Un bord de instrumente pe o magistrală de vehicul J1939 - indicatoare de viteză și turație, treapta, combustibilul, lichidul de răcire, lămpile de avertizare, unitățile de comandă de pe magistrală, codul de defect activ în cuvinte și setările șoferului.

**Descărcare:** [car-cockpit.prj32](car-cockpit.prj32) - deschide-l în editorul ctrl32 (**File → Open**).

## Ce face

Cinci ecrane pe sticla de 7":

- **Cockpit** - indicatoare de viteză și turație, treapta,
  combustibilul, lichidul de răcire și bateria, kilometrajul total și
  parțial, ceasul, semnalizările și lămpile de avertizare.
- **Engine** - valorile motorului în detaliu.
- **Bus** - rețeaua **J1939**: nodul panoului, motorul, transmisia și
  frânele și dacă răspund, lămpile DM1, fiecare semnal cu grupul lui
  de parametri.
- **Faults** - lista de alarme și codul de defect activ al motorului
  (SPN / FMI / număr) cu semnificația lui în cuvinte.
- **Settings** - modul demo, unitățile, avertizarea de viteză, zona
  roșie de turație, avertizările de lichid de răcire și combustibil,
  intervalul de service.

Comunicația este **SAE J1939** pe CAN-ul plăcii (un transceiver de
3,3 V pe GPIO47 / GPIO48, 250 kbit/s): motorul, transmisia și frânele
își difuzează grupurile de parametri, iar panoul le citește - nu e
nevoie de niciun program pentru ca o valoare să sosească. În **modul
demo** (activ implicit) programul SIM conduce un ciclu: pornește de pe
loc, schimbă treptele, rulează constant, frânează, oprește - și din
când în când un defect.

## Ecranele

**Cockpit**

![Ecranul Cockpit: indicatoare de viteză și turație, treapta, combustibilul, lichidul de răcire și lămpile de avertizare](img/cockpit.png)

**Magistrală**

![Ecranul magistralei J1939: unitățile de comandă și semnalele pe care le citește panoul](img/bus.png)

**Defecte**

![Ecranul Faults: lista de alarme și codul de defect activ](img/faults.png)

## Deschide-l și rulează-l

1. Deschide `car-cockpit.prj32` în editor.
2. Rulează-l așa cum este, în modul demo; pe un vehicul conectează transceiverul CAN la GPIO47 / GPIO48 și oprește modul demo pe ecranul Settings.
3. Pornește **simularea** (bara de instrumente) pentru a-l încerca pe PC sau descarcă-l pe placă - vezi [Instalarea runtime-ului](../../install.ro.md).

## Ce ar trebui să vezi

Bordul apare în modul demo: acele parcurg ciclul de condus, treapta se
schimbă, semnalizările clipesc. Oprește modul demo pe ecranul Settings
și conectează magistrala - indicatoarele arată atunci vehiculul.


---

[← Proiecte exemplu](../README.ro.md) | [Prezentare](../../README.ro.md)
