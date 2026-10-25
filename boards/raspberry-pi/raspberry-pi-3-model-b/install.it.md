---
title: Installare il runtime ctrl32 sulla Raspberry Pi 3 Model B+
slug: install
sidebar_position: 30
image: img/install-03-prepare.png
image_alt: L'editor ctrl32 prepara la Raspberry Pi 3 Model B+
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- install
---

# Installare il runtime ctrl32

Il runtime Linux di ctrl32 è il programma sulla scheda che esegue il tuo progetto - il ciclo PLC, la schermata sul monitor, WEBview, OPC UA e i bus. L'editor lo installa tramite la rete; non si digita alcun comando Linux.

## 1. Scrivere la scheda SD

Scrivi **Raspberry Pi OS Lite (64-bit)** sulla scheda con il Raspberry Pi
Imager. *Lite* è voluto: il runtime disegna lo schermo da solo e non ha
bisogno di un desktop. Nelle impostazioni dell'Imager, prima di scrivere,
imposta:

- un **hostname** che riconoscerai in rete,
- un **utente** e la sua **password**,
- **SSH abilitato**,
- il Wi-Fi solo se il Pi non sarà collegato via cavo.

Inserisci la scheda nel Pi, collega Ethernet e il monitor e accendilo.

![Raspberry Pi 3 Model B+](img/board-01.jpg)

## 2. Creare il progetto

Avvia l'editor ctrl32 e scegli **New project** (Ctrl+N). Inserisci il **nome** del progetto, scegli **Raspberry Pi** sotto **Linux** e premi **Create project**.

![La procedura guidata New project con il Raspberry Pi selezionato](img/install-02-new-project.png)

Per partire invece dall'esempio pronto, apri il [progetto all-in-one](examples/all-in-one/README.it.md) (**File → Open**).

## 3. Preparare la scheda

Scegli **Online → Prepare a Linux device**. Inserisci l'**indirizzo** della scheda, l'**utente** e la **password** del passo 1 e premi **Look at the device**: l'editor accede, legge che scheda è ed elenca cosa farà - guardare non cambia nulla. Poi premi **Prepare it**: l'editor copia il runtime, lo installa come servizio, lo avvia e attende che risponda. Da quel momento la scheda avvia il runtime a ogni boot.

![Prepare a Linux device: che scheda è e i passi che l'editor eseguirà](img/install-03-prepare.png)

Lascia selezionato **Do not ask for the password again**: l'editor deposita la propria chiave sulla scheda e le visite successive richiedono solo l'indirizzo. La password viene usata una volta e mai memorizzata.

Sotto il piano, **Operating system of this device** contiene ciò che
appartiene al Pi anziché al progetto: l'HAT CAN (una riga per ogni chip
CAN su SPI), la liberazione della porta seriale per un HAT RS-485, I2C, un
indirizzo fisso e il kernel real-time per EtherCAT. Spunta ciò che il tuo
Pi monta; ogni riga spuntata è un passo, e il Pi si riavvia solo quando è
cambiata un'impostazione di boot.

## 4. Scaricare il progetto

Inserisci l'indirizzo della scheda nel selettore di porta della barra degli strumenti e premi il pulsante di download (F5). Il runtime carica il progetto e la schermata compare sul monitor.

![La barra degli strumenti: il selettore di porta e il pulsante Download](img/install-05-download.png)

## 5. Verifica che funzioni

- **ONLINE** (l'icona della spina) mostra i valori in tempo reale nei rung, nelle variabili e sulla schermata.
- **WEBview**: `http://<indirizzo>:8080` in un browser della stessa rete.
- **OPC UA**: `opc.tcp://<indirizzo>:4840` - ogni variabile è un nodo, `ns=1;s=<nome>`.

![Il programma ladder in esecuzione - verde significa che la corrente scorre](img/install-06-running.png)

| Porta | Cosa ci gira |
|---|---|
| 8080 | WEBview, il caricamento del programma, la ricerca del dispositivo |
| 4840 | il server OPC UA |
| 3232 | la connessione online dell'editor |

Qualcosa non funziona? Vedi [Risoluzione dei problemi](troubleshooting.it.md).

*Schermate: editor ctrl32 1.07.*

---

[← Hardware e cablaggio](hardware.it.md) | [Panoramica](README.it.md) | [Configurare →](configure.it.md)
