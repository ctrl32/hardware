---
title: Olimex ESP32-PoE-ISO
slug: olimex-esp32-poe-iso
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe-iso/
image: img/board-01.jpg
image_alt: Carte Olimex ESP32-PoE-ISO avec la prise Ethernet et l'alimentation PoE isolée
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Olimex ESP32-PoE-ISO

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Carte Olimex ESP32-PoE-ISO avec la prise Ethernet et l'alimentation PoE isolée](img/board-01.jpg)

L'Olimex ESP32-PoE-ISO est l'ESP32-PoE avec une alimentation Power over Ethernet isolée galvaniquement : un seul câble réseau l'alimente et porte sa liaison, et un PC peut rester branché en USB pendant que la carte fonctionne sur PoE. Avec ctrl32, c'est un automate compact pour armoire - un programme ladder dans la puce, sa page opérateur dans tout navigateur (WEBview), Modbus TCP vers des compteurs et des modules d'E/S, et MQTT vers Home Assistant.

**Convient pour :**

- Un petit automate en armoire, alimenté par un switch PoE
- Une passerelle Modbus TCP qui lit des compteurs et les publie via MQTT
- La domotique - une pièce ou une chaufferie sur un seul câble

Page de la carte dans le catalogue : [Olimex ESP32-PoE-ISO](https://ctrl32.com/hardware/boards/olimex-esp32-poe-iso/)

![Olimex ESP32-PoE-ISO - brochage : la fonction de chaque GPIO dans ctrl32](pinout/pinout.png)

## Ce que ctrl32 sait faire sur cette carte

<!-- capabilities:start -->
| Fonction | Sur cette carte | Remarques |
|---|---|---|
| Puce | ESP32 (ESP32-WROOM-32E-N4) |  |
| Mémoire | 4 MB flash |  |
| Taille du programme | 128 variables, 32 alarmes, 128 blocs | vérifié par l'éditeur avant un téléchargement |
| Entrées / sorties numériques | 6 GPIO libres | 3 dont entrées seules |
| Entrées analogiques | 4 sur la puce (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | oui - LAN8710A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - sur des broches libres | nécessite un transceiver externe |
| Modbus RTU (RS-485) | oui - sur des broches libres | nécessite un transceiver externe |
| Modbus TCP | client et serveur |  |
| MQTT | oui | découverte Home Assistant |
| WEBview | oui | la page opérateur dans tout navigateur |
| Écran / tactile (HMI) | non | la page opérateur est WEBview |
| USB | Micro-USB (CH340T USB-UART) |  |
| Alimentation | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Ce qui n'est pas pris en charge

- Le Bluetooth - l'ESP32 l'a, ctrl32 ne l'utilise pas.
- Le lecteur microSD - ctrl32 garde le programme et les écrans dans la mémoire flash propre de la puce.
- L'entrée batterie fonctionne comme une fonction propre de la carte ; ctrl32 ne lit pas le niveau de la batterie.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.fr.md) - la même carte sans l'alimentation isolée
- Olimex ESP32-POE2 - la génération suivante

