---
title: LaskaKit ESPlan
slug: laskakit-esplan
sidebar_position: 10
hardware: /hardware/boards/laskakit-esplan/
image: img/board-01.jpg
image_alt: Carte LaskaKit ESPlan avec la prise Ethernet, le bornier RS-485 et le bornier d'alimentation
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# LaskaKit ESPlan

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Carte LaskaKit ESPlan avec la prise Ethernet, le bornier RS-485 et le bornier d'alimentation](img/board-01.jpg)

La LaskaKit ESPlan est une carte industrielle à ESP32 : Ethernet 10/100, une interface RS-485 protégée avec terminaison commutable, le Wi-Fi et une alimentation large de 7-40 V sur un bornier à vis (ou PoE avec un module additionnel). Avec ctrl32, c'est un maître ou un esclave Modbus RTU en armoire - un programme ladder dans la puce, des appareils RS-485 lus et écrits, les valeurs sur Modbus TCP, MQTT et sa page opérateur (WEBview).

**Convient pour :**

- Un maître Modbus RTU pour compteurs, capteurs et variateurs, alimenté en 24 V
- Une passerelle Modbus RTU / TCP avec sa propre logique
- L'automatisation du bâtiment en armoire

Page de la carte dans le catalogue : [LaskaKit ESPlan](https://ctrl32.com/hardware/boards/laskakit-esplan/)

![LaskaKit ESPlan - brochage : la fonction de chaque GPIO dans ctrl32](pinout/pinout.png)

## Ce que ctrl32 sait faire sur cette carte

<!-- capabilities:start -->
| Fonction | Sur cette carte | Remarques |
|---|---|---|
| Puce | ESP32 (ESP32-WROOM-32E-N4) |  |
| Mémoire | 4 MB flash |  |
| Taille du programme | 128 variables, 32 alarmes, 128 blocs | vérifié par l'éditeur avant un téléchargement |
| Entrées / sorties numériques | 5 GPIO libres | 2 dont entrées seules |
| Entrées analogiques | 2 sur la puce (ADC1) | GPIO35, GPIO39 |
| Ethernet | oui - LAN8720A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - sur des broches libres | nécessite un transceiver externe |
| Modbus RTU (RS-485) | oui |  |
| Modbus TCP | client et serveur |  |
| MQTT | oui | découverte Home Assistant |
| WEBview | oui | la page opérateur dans tout navigateur |
| Écran / tactile (HMI) | non | la page opérateur est WEBview |
| USB | USB-C (CH9102 USB-UART) |  |
| Alimentation | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Ce qui n'est pas pris en charge

- Le Bluetooth - l'ESP32 l'a, ctrl32 ne l'utilise pas.
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

