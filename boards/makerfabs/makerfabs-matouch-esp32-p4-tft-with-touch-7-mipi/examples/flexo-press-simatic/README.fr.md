---
title: 'Makerfabs MaTouch ESP32-P4 7" : exemple Flexo press on a SIMATIC'
slug: flexo-press-simatic
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: La page opérateur de l'exemple flexo press on a simatic pour la Makerfabs MaTouch ESP32-P4 7"
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

L'IHM d'une presse flexographique huit couleurs commandée par un SIMATIC S7-1200 - la presse avec sa bande en mouvement, seize servos d'impression, le repérage, les sécheurs, les travaux en recettes et le diagnostic, via le protocole S7.

**Téléchargement :** [flexo-press-simatic.prj32](flexo-press-simatic.prj32) - ouvrez-le dans l'éditeur ctrl32 (**File → Open**).

## Ce qu'il fait

Six pages sur un pupitre industriel clair :

- **Overview** - la presse en dessin avec la bande qui défile dessus,
  les témoins de synchronisation des groupes, les températures des
  sécheurs, les tensions de bande et les longueurs de bobine ; START
  (avec confirmation), STOP, JOG, RESET.
- **Sections** - les seize servos d'impression : cylindres porte-clichés
  et anilox, synchronisés, défaut, vitesse, validés.
- **Register** - l'erreur de repérage de chaque groupe et la
  correction.
- **Heating** - les chambres de séchage et le sécheur de pont.
- **Jobs** - le travail sous forme de **recette** conservée dans le
  pupitre : charger, enregistrer, supprimer.
- **Diagnostics** - les alarmes, la liaison avec l'automate et une
  courbe de la vitesse et de la tension.

Le pupitre dialogue avec un **SIMATIC S7-1200** via **+7** (le
protocole S7, ISO-on-TCP) : il lit le bloc d'état DB100 de l'automate
toutes les 100 ms et écrit ses consignes et ses commandes dans DB101 -
rien d'autre n'est nécessaire dans l'automate. En **mode démo** (activé
par défaut), le programme SIM fait tourner la presse sur le pupitre
lui-même.

## Les écrans

**Vue d'ensemble**

![La page Overview : le dessin de la presse avec la bande en mouvement, les tensions et les sécheurs](img/overview.png)

**Groupes**

![La page Sections : seize servos d'impression avec leur état](img/sections.png)

**Travaux**

![La page Jobs : le travail sous forme de recette conservée dans le pupitre](img/jobs.png)

## L'ouvrir et l'exécuter

1. Ouvrez `flexo-press-simatic.prj32` dans l'éditeur.
2. Exécutez-le tel quel en mode démo ; avec un automate, réglez son adresse sur la page +7 et créez les deux blocs de données DB100 / DB101.
3. Lancez la **simulation** (barre d'outils) pour l'essayer sur le PC, ou chargez-le dans la carte - voir [Installer le runtime](../../install.fr.md).

## Ce que vous devriez voir

La vue d'ensemble apparaît en mode démo. Appuyez sur START et
confirmez : la ligne accélère, la bande défile sur le dessin et les
tensions se stabilisent. Désactivez le mode démo sur la page
Diagnostics et réglez l'adresse de l'automate - le pupitre affiche
alors la vraie presse.


---

[← Projets d'exemple](../README.fr.md) | [Vue d'ensemble](../../README.fr.md)
