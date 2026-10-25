---
title: Olimex ESP32-EVB
slug: olimex-esp32-evb
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-evb/
image: img/board-01.jpg
image_alt: Carte Olimex ESP32-EVB avec ses deux relais, la prise Ethernet et le bornier CAN
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Olimex ESP32-EVB

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 240x320](https://img.shields.io/badge/HMI-240x320-0891b2)

![Carte Olimex ESP32-EVB avec ses deux relais, la prise Ethernet et le bornier CAN](img/board-01.jpg)

L'Olimex ESP32-EVB est une carte ESP32 conçue pour la commande : deux relais (10 A / 250 VAC), un transceiver CAN, Ethernet et Wi-Fi sur une seule carte. Avec ctrl32, c'est un automate prêt à l'emploi - les relais et le bouton sont des variables d'un programme ladder, le CAN dialogue avec des variateurs et des nœuds d'E/S, et la page opérateur fonctionne dans tout navigateur (WEBview). Un écran tactile 2,8" optionnel sur le connecteur UEXT en fait un petit pupitre.

**Convient pour :**

- Une commande à relais - chauffage, pompes, éclairage - avec Ethernet
- Un maître CAN pour un variateur ou des nœuds d'E/S CANopen
- Un thermostat ou un petit pupitre avec l'écran 2,8" optionnel

Page de la carte dans le catalogue : [Olimex ESP32-EVB](https://ctrl32.com/hardware/boards/olimex-esp32-evb/)

![Olimex ESP32-EVB - brochage : la fonction de chaque GPIO dans ctrl32](pinout/pinout.png)

## Ce que ctrl32 sait faire sur cette carte

<!-- capabilities:start -->
| Fonction | Sur cette carte | Remarques |
|---|---|---|
| Puce | ESP32 (ESP32-WROOM-32E-N4) |  |
| Mémoire | 4 MB flash |  |
| Taille du programme | 128 variables, 32 alarmes, 128 blocs | vérifié par l'éditeur avant un téléchargement |
| Entrées / sorties numériques | 6 GPIO libres | 2 dont entrées seules |
| Entrées analogiques | 4 sur la puce (ADC1) | GPIO32, GPIO33, GPIO34, GPIO36 |
| Ethernet | oui - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 |  |
| Modbus RTU (RS-485) | oui - sur des broches libres | nécessite un transceiver externe |
| Modbus TCP | client et serveur |  |
| MQTT | oui | découverte Home Assistant |
| WEBview | oui | la page opérateur dans tout navigateur |
| Écran / tactile (HMI) | - 240x320, - |  |
| USB | Micro-USB (CH340T USB-UART) |  |
| Alimentation | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ce qui n'est pas pris en charge

- Le Bluetooth.
- Le récepteur et l'émetteur IR - ctrl32 ne les utilise pas sur cette carte.
- Le lecteur microSD - ctrl32 garde le programme et les écrans dans la mémoire flash propre de la puce.

## Le guide

| Étape | Page |
|---|---|
| 1 | [Matériel et câblage](hardware.fr.md) - ce dont vous avez besoin, l'alimentation, le brochage |
| 2 | [Installer le runtime](install.fr.md) - l'éditeur, la carte, le premier chargement |
| 3 | [Configurer](configure.fr.md) - réseau, E/S, communication |
| 4 | [Projets d'exemple](examples/README.fr.md) - tout ce que fait la carte, prêt à ouvrir |
| - | [Dépannage](troubleshooting.fr.md) |

## Fichiers

-

## Étapes suivantes

- [documentation ctrl32](https://ctrl32.com/docs/) - l'éditeur, les langages, chaque bloc
- [Télécharger l'éditeur](https://ctrl32.com/download/)
- [Toutes les cartes testées](../../README.fr.md)
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.fr.md) - Ethernet et Power over Ethernet

