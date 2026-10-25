---
title: Configurare la Raspberry Pi 3 Model B+ nell'editor ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: La pagina della scheda Raspberry Pi 3 Model B+ nell'editor
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Configurare la scheda

## La pagina della scheda

Fai doppio clic sulla scheda nell'albero dei dispositivi. La pagina mostra cosa porta la scheda e ogni pin: un pin libero riceve una variabile con un clic - un ingresso, un'uscita o, su un pin con funzione analogica, un ingresso analogico.

![La pagina della scheda: i pin liberi e cosa sa fare ciascuno](img/configure-01-board.png)

## Rete

Il Pi conserva le impostazioni di rete del suo sistema operativo: DHCP dal
router, a meno che **Prepare a Linux device** non abbia impostato un
indirizzo fisso. Lo trovi tramite il suo hostname o con **Find devices**
nell'editor.


## Ingressi, uscite e variabili

Ogni segnale del programma è una **variabile**. Una variabile su un pin legge o pilota il pin; una variabile analogica dice cosa vi è collegato (una tensione, 4-20 mA, un termistore) e il suo campo in unità.

![Le variabili dell'esempio all-in-one](img/configure-03-variables.png)

## Comunicazione

**Modbus TCP.** Un dispositivo in rete si aggiunge sotto **Ethernet → Modbus TCP master**; i suoi registri diventano variabili.

**Modbus RTU / RS-485.** Un adattatore USB-RS485 (`/dev/ttyUSB0`, la direzione commuta da sola) oppure un HAT RS-485 sulla UART del Pi. ctrl32 vi è master o slave Modbus RTU, fino a quattro linee.

**CAN.** Il CAN arriva da un HAT CAN su SPI (MCP2515, MCP251xFD) o da un adattatore CAN USB; il runtime lo usa come interfaccia SocketCAN (`can0`, fino a quattro bus). Prepare a Linux device aggiunge il driver dell'HAT; il bit rate è quello del progetto.

**MQTT.** La scheda pubblica le variabili scelte su un broker; nella modalità Home Assistant il broker le trova da solo, e una variabile contrassegnata *write* si può impostare da lì.

![La pagina MQTT: il broker e le variabili pubblicate](img/configure-05-mqtt.png)

## Display

Il runtime disegna sul monitor HDMI collegato (o su un display DSI) e vi
adatta la scala del progetto; l'esempio è disegnato a 1280 x 720. Il touch
USB di un monitor touch funziona senza driver. Senza monitor il Pi
fornisce le sue schermate solo ai browser (WEBview).

![Le impostazioni HMIview: lo schermo su cui disegna il progetto](img/configure-04-display.png)

## OPC UA ed EtherCAT

- **OPC UA** - ogni variabile del progetto è un nodo del server proprio
  del Pi (`opc.tcp://<indirizzo>:4840`, `ns=1;s=<nome>`); una variabile
  si può escludere con una spunta nell'elenco delle variabili. Non si
  imposta nient'altro.
- **EtherCAT** - un master su un adattatore Ethernet USB per terminali
  I/O; per servoazionamenti con un ciclo di bus breve un Raspberry Pi 4 o
  5 è la scelta migliore.

## WEBview

La scheda fornisce la sua pagina operatore a qualsiasi browser della rete - apri l'indirizzo della scheda. La pagina si disegna nell'editor come una schermata.

![Le impostazioni della pagina WEBview](img/configure-06-webview.png)

---

[← Installare il runtime](install.it.md) | [Panoramica](README.it.md) | [Progetti di esempio →](examples/README.it.md)
