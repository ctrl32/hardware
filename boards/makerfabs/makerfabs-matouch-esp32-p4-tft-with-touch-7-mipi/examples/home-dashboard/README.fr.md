---
title: 'Makerfabs MaTouch ESP32-P4 7" : exemple Home dashboard'
slug: home-dashboard
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.jpg
image_alt: La page opérateur de l'exemple home dashboard pour la Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Home dashboard

Un écran de commande pour toute la maison dans un style sombre en verre dépoli - le chauffage pièce par pièce, l'énergie avec photovoltaïque et batterie, l'éclairage, le garage et la météo - avec une maison simulée derrière.

**Téléchargement :** [home-dashboard.prj32](home-dashboard.prj32) - ouvrez-le dans l'éditeur ctrl32 (**File → Open**).

## Ce qu'il fait

Six écrans sur des photographies de la maison, chacun un ensemble de
cartes en verre dépoli :

- **Home** - l'heure, la météo, les pièces, l'alarme et les scènes.
- **Weather** - aujourd'hui et les jours suivants.
- **Climate** - six pièces, chacune avec sa température, sa consigne et
  le chauffage ; la pompe à chaleur et le ballon d'eau chaude.
- **Energy** - la production photovoltaïque, la consommation de la
  maison, la batterie et le réseau, les kWh du jour.
- **Lights** - les éclairages des pièces et leurs scènes.
- **Access** - la porte du garage, la borne de recharge, l'alarme.

Le programme **SIM** est la maison : la température extérieure suit la
journée, la production photovoltaïque le soleil, la consommation a ses
pointes du matin et du soir, les pièces chauffent avec une hystérésis
jusqu'à leurs consignes. Remplacez ses variables par vos appareils
Modbus, MQTT ou CAN pour piloter une vraie maison.

## Les écrans

**Accueil**

![L'écran Home du tableau de bord : heure, météo, pièces, alarme et scènes](img/home.jpg)

**Climat**

![L'écran Climate : six pièces avec leurs températures et leurs consignes](img/climate.png)

**Énergie**

![L'écran Energy : photovoltaïque, consommation de la maison, batterie et réseau](img/energy.jpg)

## L'ouvrir et l'exécuter

1. Ouvrez `home-dashboard.prj32` dans l'éditeur.
2. Exécutez-le tel quel - la maison est simulée ; pour une vraie maison, remplacez les variables du programme SIM par vos appareils.
3. Lancez la **simulation** (barre d'outils) pour l'essayer sur le PC, ou chargez-le dans la carte - voir [Installer le runtime](../../install.fr.md).

## Ce que vous devriez voir

L'écran d'accueil apparaît avec l'heure, la météo et les pièces ; les
valeurs évoluent au fil de la journée simulée. Un appui sur la consigne
d'une pièce la modifie, et la pièce chauffe jusqu'à elle.


---

[← Projets d'exemple](../README.fr.md) | [Vue d'ensemble](../../README.fr.md)
