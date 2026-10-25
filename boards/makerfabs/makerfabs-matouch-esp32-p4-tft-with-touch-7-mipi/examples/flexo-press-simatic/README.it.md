---
title: 'Makerfabs MaTouch ESP32-P4 7": esempio Flexo press on a SIMATIC'
slug: flexo-press-simatic
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: La pagina operatore dell'esempio flexo press on a simatic per la Makerfabs MaTouch ESP32-P4 7"
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

L'HMI di una macchina da stampa flessografica a otto colori comandata da un SIMATIC S7-1200 - la macchina con il nastro in movimento, sedici servo di stampa, il registro, gli essiccatori, le commesse come ricette e la diagnostica, tramite il protocollo S7.

**Download:** [flexo-press-simatic.prj32](flexo-press-simatic.prj32) - aprilo nell'editor ctrl32 (**File → Open**).

## Cosa fa

Sei pagine su un pannello industriale chiaro:

- **Overview** - la macchina da stampa come disegno con il nastro che
  vi scorre sopra, le spie di sincronismo dei gruppi, le temperature
  degli essiccatori, le tensioni del nastro e le lunghezze delle
  bobine; START (con conferma), STOP, JOG, RESET.
- **Sections** - i sedici servo di stampa: cilindri portacliché e
  anilox, in sincronismo, guasto, velocità, abilitato.
- **Register** - l'errore di registro di ogni gruppo e la correzione.
- **Heating** - le camere di essiccazione e l'essiccatore a ponte.
- **Jobs** - la commessa come **ricetta** conservata sul pannello:
  caricare, salvare, eliminare.
- **Diagnostics** - gli allarmi, il collegamento al PLC e un trend di
  velocità e tensione.

Il pannello comunica con un **SIMATIC S7-1200** tramite **+7** (il
protocollo S7, ISO-on-TCP): legge ogni 100 ms il blocco di stato DB100
del PLC e scrive i suoi setpoint e comandi in DB101 - nel PLC non
serve altro. In **modalità demo** (attiva per impostazione predefinita)
il programma SIM fa funzionare la macchina da stampa sul pannello
stesso.

## Le schermate

**Panoramica**

![La pagina Overview: il disegno della macchina da stampa con il nastro in movimento, tensioni ed essiccatori](img/overview.png)

**Gruppi**

![La pagina Sections: sedici servo di stampa con il loro stato](img/sections.png)

**Commesse**

![La pagina Jobs: la commessa come ricetta conservata sul pannello](img/jobs.png)

## Aprirlo ed eseguirlo

1. Apri `flexo-press-simatic.prj32` nell'editor.
2. Eseguilo così com'è in modalità demo; con un PLC imposta il suo indirizzo nella pagina +7 e crea i due blocchi dati DB100 / DB101.
3. Avvia la **simulazione** (barra degli strumenti) per provarlo sul PC, oppure scaricalo sulla scheda - vedi [Installare il runtime](../../install.it.md).

## Cosa dovresti vedere

La panoramica compare in modalità demo. Premi START e conferma: la
linea accelera, il nastro scorre sul disegno e le tensioni si
stabilizzano. Disattiva la modalità demo nella pagina Diagnostics e
imposta l'indirizzo del PLC - il pannello mostra allora la macchina da
stampa reale.


---

[← Progetti di esempio](../README.it.md) | [Panoramica](../../README.it.md)
