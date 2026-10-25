---
title: Configurare la Olimex ESP32-EVB nell'editor ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: La pagina della scheda Olimex ESP32-EVB nell'editor
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Configurare la scheda

## La pagina della scheda

Fai doppio clic sulla scheda nell'albero dei dispositivi. La pagina mostra cosa porta la scheda e ogni pin: un pin libero riceve una variabile con un clic - un ingresso, un'uscita o, su un pin con funzione analogica, un ingresso analogico.

![La pagina della scheda: i pin liberi e cosa sa fare ciascuno](img/configure-01-board.png)

## Rete

La porta Ethernet si avvia da sola e prende l'indirizzo dal tuo router
(DHCP). Un indirizzo fisso si imposta nella pagina della scheda, nella
sezione **Network**; il Wi-Fi nella pagina **WiFi** dell'albero dei
dispositivi.


## Ingressi, uscite e variabili

Ogni segnale del programma è una **variabile**. Una variabile su un pin legge o pilota il pin; una variabile analogica dice cosa vi è collegato (una tensione, 4-20 mA, un termistore) e il suo campo in unità.

![Le variabili dell'esempio all-in-one](img/configure-03-variables.png)

## Comunicazione

**Modbus TCP.** Un dispositivo in rete si aggiunge sotto **Ethernet → Modbus TCP master**; i suoi registri diventano variabili.

**Modbus RTU / RS-485.** La scheda non ha un transceiver RS-485: collega un modulo transceiver a 3,3 V a pin liberi (TX, RX e il pin di direzione DE) e indicali nella pagina della scheda (Bus pins) - ctrl32 è allora master o slave Modbus RTU su quella linea. I dispositivi Modbus TCP in rete non richiedono nulla.

**CAN.** L'ESP32 ha un controller CAN (TWAI) e questa scheda porta il suo transceiver: CAN_H / CAN_L sul morsetto, GPIO5 / GPIO35. I dispositivi CANopen (un azionamento, nodi I/O), i frame CAN grezzi e i bus veicolari (J1939) funzionano tutti su di esso.

**MQTT.** La scheda pubblica le variabili scelte su un broker; nella modalità Home Assistant il broker le trova da solo, e una variabile contrassegnata *write* si può impostare da lì.

![La pagina MQTT: il broker e le variabili pubblicate](img/configure-05-mqtt.png)

## Display e touch

Con il MOD-LCD2.8RTP sul connettore UEXT il progetto può avere delle
schermate (240 x 320, verticale o ruotato). La scheda non ha PSRAM: con il
display acceso il runtime riserva la sua memoria allo schermo e gestisce
la rete solo su Ethernet (niente Wi-Fi, niente MQTT). Per questo l'esempio
all-in-one non ha schermate; WEBview funziona in entrambi i casi.

![Le impostazioni HMIview: lo schermo su cui disegna il progetto](img/configure-04-display.png)

## WEBview

La scheda fornisce la sua pagina operatore a qualsiasi browser della rete - apri l'indirizzo della scheda. La pagina si disegna nell'editor come una schermata.

![Le impostazioni della pagina WEBview](img/configure-06-webview.png)

---

[← Installare il runtime](install.it.md) | [Panoramica](README.it.md) | [Progetti di esempio →](examples/README.it.md)
