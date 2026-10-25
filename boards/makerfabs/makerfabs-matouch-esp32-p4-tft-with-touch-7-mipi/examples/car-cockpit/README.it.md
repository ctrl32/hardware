---
title: 'Makerfabs MaTouch ESP32-P4 7": esempio Car cockpit'
slug: car-cockpit
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: La pagina operatore dell'esempio car cockpit per la Makerfabs MaTouch ESP32-P4 7"
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

Un quadro strumenti su un bus veicolare J1939 - tachimetro e contagiri, marcia, carburante, liquido di raffreddamento, le spie, le centraline sul bus, il codice di guasto attivo a parole e le impostazioni del conducente.

**Download:** [car-cockpit.prj32](car-cockpit.prj32) - aprilo nell'editor ctrl32 (**File → Open**).

## Cosa fa

Cinque schermate sul vetro da 7":

- **Cockpit** - tachimetro e contagiri, la marcia, carburante, liquido
  di raffreddamento e batteria, il contachilometri totale e parziale,
  l'orologio, gli indicatori di direzione e le spie.
- **Engine** - i valori del motore in dettaglio.
- **Bus** - la rete **J1939**: il nodo del pannello, il motore, il
  cambio e i freni e se rispondono, le spie DM1, ogni segnale con il
  suo gruppo di parametri.
- **Faults** - l'elenco degli allarmi e il codice di guasto attivo del
  motore (SPN / FMI / conteggio) con il suo significato a parole.
- **Settings** - modalità demo, unità, l'avviso di velocità, la zona
  rossa, gli avvisi di liquido di raffreddamento e carburante,
  l'intervallo di manutenzione.

La comunicazione è **SAE J1939** sul CAN della scheda (un transceiver
a 3,3 V su GPIO47 / GPIO48, 250 kbit/s): il motore, il cambio e i
freni trasmettono i loro gruppi di parametri e il pannello li legge -
perché un valore arrivi non serve alcun programma. In **modalità demo**
(attiva per impostazione predefinita) il programma SIM esegue un ciclo:
parte, cambia marcia, viaggia, frena, si ferma - e ogni tanto un
guasto.

## Le schermate

**Cockpit**

![La schermata Cockpit: tachimetro e contagiri, marcia, carburante, liquido di raffreddamento e le spie](img/cockpit.png)

**Bus**

![La schermata Bus della rete J1939: le centraline e i segnali che il pannello legge](img/bus.png)

**Guasti**

![La schermata Faults: l'elenco degli allarmi e il codice di guasto attivo](img/faults.png)

## Aprirlo ed eseguirlo

1. Apri `car-cockpit.prj32` nell'editor.
2. Eseguilo così com'è in modalità demo; su un veicolo collega il transceiver CAN a GPIO47 / GPIO48 e disattiva la modalità demo nella schermata Settings.
3. Avvia la **simulazione** (barra degli strumenti) per provarlo sul PC, oppure scaricalo sulla scheda - vedi [Installare il runtime](../../install.it.md).

## Cosa dovresti vedere

Il quadro strumenti compare in modalità demo: le lancette seguono il
ciclo di guida, la marcia cambia, gli indicatori di direzione
lampeggiano. Disattiva la modalità demo nella schermata Settings e
collega il bus - gli strumenti mostrano allora il veicolo.


---

[← Progetti di esempio](../README.it.md) | [Panoramica](../../README.it.md)
