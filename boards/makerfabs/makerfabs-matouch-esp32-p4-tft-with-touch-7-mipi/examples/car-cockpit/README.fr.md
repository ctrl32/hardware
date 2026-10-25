---
title: 'Makerfabs MaTouch ESP32-P4 7" : exemple Car cockpit'
slug: car-cockpit
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: La page opérateur de l'exemple car cockpit pour la Makerfabs MaTouch ESP32-P4 7"
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

Un combiné d'instruments sur un bus véhicule J1939 - compteur de vitesse et compte-tours, rapport engagé, carburant, liquide de refroidissement, les témoins d'alerte, les calculateurs du bus, le code de défaut actif en clair et les réglages du conducteur.

**Téléchargement :** [car-cockpit.prj32](car-cockpit.prj32) - ouvrez-le dans l'éditeur ctrl32 (**File → Open**).

## Ce qu'il fait

Cinq écrans sur la dalle 7" :

- **Cockpit** - compteur de vitesse et compte-tours, le rapport engagé,
  le carburant, le liquide de refroidissement et la batterie, le
  compteur kilométrique et le journalier, l'horloge, les clignotants et
  les témoins d'alerte.
- **Engine** - les valeurs du moteur en détail.
- **Bus** - le réseau **J1939** : le nœud du pupitre, le moteur, la
  boîte de vitesses et les freins et s'ils répondent, les témoins DM1,
  chaque signal avec son groupe de paramètres.
- **Faults** - la liste des alarmes et le code de défaut actif du
  moteur (SPN / FMI / nombre) avec sa signification en clair.
- **Settings** - le mode démo, les unités, l'alerte de vitesse, la zone
  rouge, les alertes de liquide de refroidissement et de carburant,
  l'intervalle d'entretien.

La communication est **SAE J1939** sur le CAN de la carte (un
transceiver 3,3 V sur GPIO47 / GPIO48, 250 kbit/s) : le moteur, la
boîte de vitesses et les freins diffusent leurs groupes de paramètres
et le pupitre les lit - aucun programme n'est nécessaire pour qu'une
valeur arrive. En **mode démo** (activé par défaut), le programme SIM
déroule un cycle : démarrage, passages de rapports, croisière,
freinage, arrêt - et de temps en temps un défaut.

## Les écrans

**Cockpit**

![L'écran Cockpit : compteur de vitesse et compte-tours, rapport, carburant, liquide de refroidissement et témoins d'alerte](img/cockpit.png)

**Bus**

![L'écran du bus J1939 : les calculateurs et les signaux que lit le pupitre](img/bus.png)

**Défauts**

![L'écran Faults : la liste des alarmes et le code de défaut actif](img/faults.png)

## L'ouvrir et l'exécuter

1. Ouvrez `car-cockpit.prj32` dans l'éditeur.
2. Exécutez-le tel quel en mode démo ; sur un véhicule, branchez le transceiver CAN sur GPIO47 / GPIO48 et désactivez le mode démo sur l'écran Settings.
3. Lancez la **simulation** (barre d'outils) pour l'essayer sur le PC, ou chargez-le dans la carte - voir [Installer le runtime](../../install.fr.md).

## Ce que vous devriez voir

Le combiné apparaît en mode démo : les aiguilles suivent le cycle de
conduite, le rapport change, les clignotants clignotent. Désactivez le
mode démo sur l'écran Settings et branchez le bus - les instruments
affichent alors le véhicule.


---

[← Projets d'exemple](../README.fr.md) | [Vue d'ensemble](../../README.fr.md)
