---
title: Configurer la LaskaKit ESPlan dans l'éditeur ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: La page de la carte LaskaKit ESPlan dans l'éditeur
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Configurer la carte

## La page de la carte

Double-cliquez sur la carte dans l'arbre des appareils. La page montre ce que porte la carte et chaque broche : une broche libre reçoit une variable en un clic - une entrée, une sortie, ou sur une broche analogique une entrée analogique.

![La page de la carte : les broches libres et ce que chacune sait faire](img/configure-01-board.png)

## Réseau

Le port Ethernet démarre de lui-même et reçoit son adresse de votre
routeur (DHCP). Une adresse fixe se définit sur la page de la carte, dans
sa section **Network** ; le Wi-Fi sur la page **WiFi** de l'arbre des
appareils.


## Entrées, sorties et variables

Chaque signal du programme est une **variable**. Une variable sur une broche lit ou pilote la broche ; une variable analogique indique ce qui y est raccordé (une tension, 4-20 mA, une thermistance) et sa plage en unités.

![Les variables de l'exemple tout-en-un](img/configure-03-variables.png)

## Communication

**Modbus TCP.** Un appareil du réseau s'ajoute sous **Ethernet → Modbus TCP master** ; ses registres deviennent des variables.

**Modbus RTU / RS-485.** La carte porte son transceiver RS-485 (WS3081, protégé). ctrl32 est un maître Modbus RTU - les appareils et leurs registres s'ajoutent dans l'arbre des appareils sous RS485 - ou un esclave Modbus RTU que d'autres maîtres lisent.

**CAN.** Le ESP32 possède un contrôleur CAN (TWAI). La carte n'a pas de transceiver CAN : placez un module transceiver 3,3 V sur deux broches libres et indiquez-les sur la page de la carte (Bus pins) - les appareils CANopen, les trames CAN brutes et les bus véhicule (J1939) y fonctionnent alors.

**MQTT.** La carte publie des variables choisies vers un broker ; en mode Home Assistant, le broker les trouve de lui-même, et une variable marquée *write* peut être réglée depuis là.

![La page MQTT : le broker et les variables publiées](img/configure-05-mqtt.png)

## WEBview

La carte sert sa page opérateur à tout navigateur du réseau - ouvrez l'adresse de la carte. La page se dessine dans l'éditeur comme un écran.

![Les réglages de la page WEBview](img/configure-06-webview.png)

---

[← Installer le runtime](install.fr.md) | [Vue d'ensemble](README.fr.md) | [Projets d'exemple →](examples/README.fr.md)
