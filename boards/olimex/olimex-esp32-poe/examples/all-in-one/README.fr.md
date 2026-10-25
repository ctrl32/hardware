---
title: 'Olimex ESP32-PoE : exemple All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/screen.png
image_alt: La page opérateur de l'exemple all-in-one pour la Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- example
---

# All-in-one

Une pompe commandée par le bouton de la carte, la page opérateur et Home Assistant, avec une entrée de niveau, une minuterie de marche, une alarme de niveau et un compteur d'énergie Modbus TCP.

**Téléchargement :** [all-in-one.prj32](all-in-one.prj32) - ouvrez-le dans l'éditeur ctrl32 (**File → Open**).

## Ce qu'il fait

Le programme est une petite commande de pompe - la forme de la plupart
des machines :

- **Start** vient du bouton de la carte (BUT1), du bouton **Start** de
  la page opérateur, ou de Home Assistant via MQTT.
- **Stop** vient du bouton **Stop**, d'un niveau bas ou de la fin de la
  durée de marche - l'auto-maintien coupe la sortie sur GPIO33.
- Le **niveau** est une entrée analogique sur GPIO35 (0 à 3,3 V mis à
  l'échelle de 0 à 100 %). Sous 10 % la pompe s'arrête et une alarme
  est levée ; au-dessus de 15 % elle peut redémarrer (hystérésis).
- La **durée de marche** se règle sur la page en minutes et est
  conservée lors d'une coupure de courant (une variable rémanente).
- Un compteur d'énergie **Modbus TCP** sur le réseau donne la tension
  du secteur (registre 0, registres d'entrée, unité 1 à 192.168.1.60 -
  remplacez-la par celle de votre compteur). Au-dessus de 253 V, une
  alarme est levée.
- **CAN** (un transceiver sur GPIO4 / GPIO36) envoie le niveau et
  l'état de la pompe dans la trame 0x181 toutes les 100 ms et reçoit une
  consigne dans 0x201.
- **MQTT** publie le niveau, l'état de la pompe et la tension vers un
  broker Home Assistant, qui les trouve de lui-même (discovery) ; la
  pompe peut être démarrée depuis Home Assistant.
- **WEBview** sert la page opérateur - la pompe, le niveau, sa courbe
  et les alarmes - à tout navigateur du réseau.

## Le programme

![Le programme ladder de l'exemple](img/ladder.png)

## La page opérateur

![La page opérateur dans la simulation](img/screen.png)

## L'ouvrir et l'exécuter

1. Ouvrez `all-in-one.prj32` dans l'éditeur.
2. Remplacez les adresses (l'appareil Modbus, le broker MQTT) par celles de votre réseau.
3. Lancez la **simulation** (barre d'outils) pour l'essayer sur le PC, ou chargez-le dans la carte - voir [Installer le runtime](../../install.fr.md).

## Ce que vous devriez voir

Potentiomètre tourné vers le haut, appuyez sur BUT1 : le relais sur
GPIO33 s'enclenche et la LED de la pompe s'allume sur la page. Tournez
le potentiomètre sous 10 % : la pompe s'arrête et l'alarme apparaît
dans le tableau. Dans Home Assistant, la carte apparaît avec son
niveau, sa pompe et sa tension.


---

[← Projets d'exemple](../README.fr.md) | [Vue d'ensemble](../../README.fr.md)
