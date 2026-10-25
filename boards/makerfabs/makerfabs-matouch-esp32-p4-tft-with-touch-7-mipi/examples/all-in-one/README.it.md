---
title: 'Makerfabs MaTouch ESP32-P4 7": esempio All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: La pagina operatore dell'esempio all-in-one per la Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# All-in-one

Un motore comandato dallo schermo touch, da due pulsanti e da Home Assistant, con un manometro, un ventilatore che segue una temperatura Modbus RTU, un contatore di potenza Modbus TCP, frame CAN, un trend e gli allarmi.

**Download:** [all-in-one.prj32](all-in-one.prj32) - aprilo nell'editor ctrl32 (**File → Open**).

## Cosa fa

Il programma è un piccolo controllore di macchina:

- **Start** arriva da un pulsante su GPIO47, da **Start** sulla
  schermata o da Home Assistant tramite MQTT; **Stop** da un pulsante
  su GPIO48, da **Stop** sulla schermata, oppure quando la pressione
  sale sopra il setpoint che arriva tramite **CAN** (frame 0x201).
- L'autoritenuta pilota l'uscita motore su **GPIO33**; un contatore
  conserva il numero di avviamenti in caso di mancanza di corrente.
- La **pressione** è un ingresso analogico tramite un **ADS1115** sul
  bus I2C (0-10 V tramite un partitore 1:4, 0-10 bar) ed esce su CAN
  ogni 100 ms (frame 0x181).
- La **temperatura** arriva da un sensore **Modbus RTU** (unit 1,
  input register 1, 0,1 °C); un ventilatore la segue con isteresi.
- Un contatore **Modbus TCP** fornisce la potenza assorbita.
- Tre **schermate** sul vetro: la panoramica, un trend e gli allarmi;
  una pagina più semplice in qualsiasi browser (WEBview).

## Il programma

![Il programma ladder dell'esempio](img/ladder.png)

## La pagina operatore

![La pagina operatore in simulazione](img/screen.png)

## Aprirlo ed eseguirlo

1. Apri `all-in-one.prj32` nell'editor.
2. Cambia gli indirizzi (il dispositivo Modbus, il broker MQTT) con quelli della tua rete.
3. Avvia la **simulazione** (barra degli strumenti) per provarlo sul PC, oppure scaricalo sulla scheda - vedi [Installare il runtime](../../install.it.md).

## Cosa dovresti vedere

La panoramica compare sul vetro. Premi **Start**: il LED del motore si
accende e il contatore di avviamenti sale. Il manometro mostra la
pressione, la schermata Trend la disegna insieme alla temperatura, e
un allarme compare nella schermata Alarms quando la pressione supera
gli 8 bar.


---

[← Progetti di esempio](../README.it.md) | [Panoramica](../../README.it.md)
