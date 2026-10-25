---
title: Configurare la Makerfabs MaTouch ESP32-P4 7" nell'editor ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: La pagina della scheda Makerfabs MaTouch ESP32-P4 7" nell'editor
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Configurare la scheda

## La pagina della scheda

Fai doppio clic sulla scheda nell'albero dei dispositivi. La pagina mostra cosa porta la scheda e ogni pin: un pin libero riceve una variabile con un clic - un ingresso, un'uscita o, su un pin con funzione analogica, un ingresso analogico.

![La pagina della scheda: i pin liberi e cosa sa fare ciascuno](img/configure-01-board.png)

## Rete

La porta Ethernet si avvia da sola e prende l'indirizzo dal tuo router
(DHCP). Il Wi-Fi dell'ESP32-C6 si imposta nella pagina **WiFi** dell'albero
dei dispositivi - il nome della rete e la password. Un indirizzo fisso si
imposta nella pagina della scheda, nella sezione **Network**.


## Ingressi, uscite e variabili

Ogni segnale del programma è una **variabile**. Una variabile su un pin legge o pilota il pin; una variabile analogica dice cosa vi è collegato (una tensione, 4-20 mA, un termistore) e il suo campo in unità.

![Le variabili dell'esempio all-in-one](img/configure-03-variables.png)

## Comunicazione

**Modbus TCP.** Un dispositivo in rete si aggiunge sotto **Ethernet → Modbus TCP master**; i suoi registri diventano variabili.

**Modbus RTU / RS-485.** La scheda non ha un transceiver RS-485: collega un modulo transceiver a 3,3 V a pin liberi (TX, RX e il pin di direzione DE) e indicali nella pagina della scheda - l'esempio usa GPIO4 / GPIO5 / GPIO32. ctrl32 è allora master o slave Modbus RTU su quella linea.

**CAN.** L'ESP32-P4 ha un controller CAN (TWAI). La scheda non ha un transceiver CAN: collega un modulo transceiver a 3,3 V a due pin liberi e indicali nella pagina della scheda (**Bus pins**) - l'esempio usa GPIO20 / GPIO21. I dispositivi CANopen, i frame CAN grezzi e i bus veicolari (J1939) funzionano tutti su di esso.

**MQTT.** La scheda pubblica le variabili scelte su un broker; nella modalità Home Assistant il broker le trova da solo, e una variabile contrassegnata *write* si può impostare da lì.

![La pagina MQTT: il broker e le variabili pubblicate](img/configure-05-mqtt.png)

## Display e touch

Il progetto si disegna alla risoluzione propria del vetro, 1024 x 600. La
pagina HMIview imposta l'orientamento (come montato, oppure ruotato - il
touch segue), la dimensione dell'area di disegno WEBview e la schermata di
avvio. Il touch non richiede configurazione: il controller GT911 fa parte
della scheda.

![Le impostazioni HMIview: lo schermo su cui disegna il progetto](img/configure-04-display.png)

## WEBview

La scheda fornisce la sua pagina operatore a qualsiasi browser della rete - apri l'indirizzo della scheda. La pagina si disegna nell'editor come una schermata.

![Le impostazioni della pagina WEBview](img/configure-06-webview.png)

---

[← Installare il runtime](install.it.md) | [Panoramica](README.it.md) | [Progetti di esempio →](examples/README.it.md)
