---
title: 'Makerfabs MaTouch ESP32-P4 7" : exemple All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: La page opérateur de l'exemple all-in-one pour la Makerfabs MaTouch ESP32-P4 7"
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

Un moteur commandé depuis l'écran tactile, deux boutons et Home Assistant, avec un manomètre, un ventilateur selon une température Modbus RTU, un compteur de puissance Modbus TCP, des trames CAN, une courbe et les alarmes.

**Téléchargement :** [all-in-one.prj32](all-in-one.prj32) - ouvrez-le dans l'éditeur ctrl32 (**File → Open**).

## Ce qu'il fait

Le programme est une petite commande de machine :

- **Start** vient d'un bouton sur GPIO47, de **Start** sur l'écran, ou
  de Home Assistant via MQTT ; **Stop** d'un bouton sur GPIO48, de
  **Stop** sur l'écran, ou de la pression qui dépasse la consigne
  arrivant par **CAN** (trame 0x201).
- L'auto-maintien pilote la sortie moteur sur **GPIO33** ; un compteur
  conserve le nombre de démarrages lors d'une coupure de courant.
- La **pression** est une entrée analogique via un **ADS1115** sur le
  bus I2C (0-10 V via un diviseur 1:4, 0-10 bar) et part sur le CAN
  toutes les 100 ms (trame 0x181).
- La **température** vient d'un capteur **Modbus RTU** (unité 1,
  registre d'entrée 1, 0,1 °C) ; un ventilateur la suit avec une
  hystérésis.
- Un compteur **Modbus TCP** donne la puissance appelée.
- Trois **écrans** sur la dalle : la vue d'ensemble, une courbe et les
  alarmes ; une page plus simple dans tout navigateur (WEBview).

## Le programme

![Le programme ladder de l'exemple](img/ladder.png)

## La page opérateur

![La page opérateur dans la simulation](img/screen.png)

## L'ouvrir et l'exécuter

1. Ouvrez `all-in-one.prj32` dans l'éditeur.
2. Remplacez les adresses (l'appareil Modbus, le broker MQTT) par celles de votre réseau.
3. Lancez la **simulation** (barre d'outils) pour l'essayer sur le PC, ou chargez-le dans la carte - voir [Installer le runtime](../../install.fr.md).

## Ce que vous devriez voir

La vue d'ensemble apparaît sur la dalle. Appuyez sur **Start** : la LED
du moteur s'allume et le compteur de démarrages augmente. Le manomètre
affiche la pression, l'écran Trend la trace avec la température, et une
alarme apparaît sur l'écran Alarms quand la pression dépasse 8 bar.


---

[← Projets d'exemple](../README.fr.md) | [Vue d'ensemble](../../README.fr.md)
