---
title: Configurer la Makerfabs MaTouch Lite ESP32-S3 3.95" dans l'éditeur ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: La page de la carte Makerfabs MaTouch Lite ESP32-S3 3.95" dans l'éditeur
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Configurer la carte

## La page de la carte

Double-cliquez sur la carte dans l'arbre des appareils. La page montre ce que porte la carte et chaque broche : une broche libre reçoit une variable en un clic - une entrée, une sortie, ou sur une broche analogique une entrée analogique.

![La page de la carte : les broches libres et ce que chacune sait faire](img/configure-01-board.png)

## Réseau

La carte rejoint votre Wi-Fi : ouvrez la page **WiFi** de l'arbre des
appareils et saisissez le nom et le mot de passe du réseau (l'exemple
contient des valeurs de remplacement). Une adresse fixe se définit sur la
page de la carte, dans sa section **Network**.


## Entrées, sorties et variables

Chaque signal du programme est une **variable**. Une variable sur une broche lit ou pilote la broche ; une variable analogique indique ce qui y est raccordé (une tension, 4-20 mA, une thermistance) et sa plage en unités.

![Les variables de l'exemple tout-en-un](img/configure-03-variables.png)

## Communication

**Modbus TCP.** Un appareil du réseau s'ajoute sous **Ethernet → Modbus TCP master** ; ses registres deviennent des variables.

**Modbus RTU / RS-485.** La carte n'a pas de transceiver RS-485 et trop peu de broches libres pour en ajouter un à côté des E/S de l'exemple ; les appareils Modbus sont joints via Modbus TCP sur le Wi-Fi.

**CAN.** L'ESP32-S3 possède un contrôleur CAN (TWAI). La carte n'a pas de transceiver : placez un module transceiver 3,3 V sur deux broches libres et indiquez-les sur la page de la carte (**Bus pins**) ; l'exemple utilise GPIO6 / GPIO7.

**MQTT.** La carte publie des variables choisies vers un broker ; en mode Home Assistant, le broker les trouve de lui-même, et une variable marquée *write* peut être réglée depuis là.

![La page MQTT : le broker et les variables publiées](img/configure-05-mqtt.png)

## Écran et tactile

La dalle fait 320 x 480, en portrait telle que montée ; la page HMIview
tourne l'image (le tactile suit) et définit l'écran de démarrage. Le
tactile résistif demande des appuis fermes - dessinez des boutons d'au
moins 40 px de haut.

![Les réglages HMIview : l'écran sur lequel le projet dessine](img/configure-04-display.png)

## WEBview

La carte sert sa page opérateur à tout navigateur du réseau - ouvrez l'adresse de la carte. La page se dessine dans l'éditeur comme un écran.

![Les réglages de la page WEBview](img/configure-06-webview.png)

---

[← Installer le runtime](install.fr.md) | [Vue d'ensemble](README.fr.md) | [Projets d'exemple →](examples/README.fr.md)
