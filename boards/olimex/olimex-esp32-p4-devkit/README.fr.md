---
title: Olimex ESP32-P4-DevKit
slug: olimex-esp32-p4-devkit
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-devkit/
image: img/board-01.jpg
image_alt: Carte Olimex ESP32-P4-DevKit avec la prise Ethernet et les barrettes de broches
tags:
- esp32-p4
- ethernet
- olimex
---

# Olimex ESP32-P4-DevKit

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Carte Olimex ESP32-P4-DevKit avec la prise Ethernet et les barrettes de broches](img/board-01.jpg)

L'Olimex ESP32-P4-DevKit est une petite carte open source avec l'ESP32-P4 - l'ESP32 le plus rapide, double cœur à 400 MHz avec 32 Mo de PSRAM - et Ethernet 100 Mb. Elle n'a pas de Wi-Fi : c'est une commande filaire. Avec ctrl32, elle exécute les plus grands programmes qu'un ESP32 puisse faire tourner - 4096 variables - avec sa page opérateur dans tout navigateur (WEBview), Modbus TCP et MQTT avec TLS.

**Convient pour :**

- Un automate filaire avec un grand programme et de nombreux appareils Modbus
- Une passerelle avec une logique conséquente entre Modbus TCP et MQTT
- Le développement de votre propre carte P4

Page de la carte dans le catalogue : [Olimex ESP32-P4-DevKit](https://ctrl32.com/hardware/boards/olimex-esp32-p4-devkit/)

![Olimex ESP32-P4-DevKit - brochage : la fonction de chaque GPIO dans ctrl32](pinout/pinout.png)

## Ce que ctrl32 sait faire sur cette carte

<!-- capabilities:start -->
| Fonction | Sur cette carte | Remarques |
|---|---|---|
| Puce | ESP32-P4 (ESP32-P4NRW32) |  |
| Mémoire | 16 MB flash, 32 MB PSRAM |  |
| Taille du programme | 4096 variables, 512 alarmes, 1024 blocs | vérifié par l'éditeur avant un téléchargement |
| Entrées / sorties numériques | 11 GPIO libres | voir le brochage |
| Entrées analogiques | via un convertisseur A/N I2C (ADS1115) |  |
| Ethernet | oui - IP101GRI |  |
| Wi-Fi | non |  |
| CAN (TWAI) | 1 - sur des broches libres | nécessite un transceiver externe |
| Modbus RTU (RS-485) | oui - sur des broches libres | nécessite un transceiver externe |
| Modbus TCP | client et serveur |  |
| MQTT | oui (TLS aussi) | découverte Home Assistant |
| WEBview | oui | la page opérateur dans tout navigateur |
| Écran / tactile (HMI) | non | la page opérateur est WEBview |
| USB | USB-C (Native USB) |  |
| Alimentation | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Ce qui n'est pas pris en charge

- Les connecteurs de l'écran MIPI DSI et de la caméra CSI - cette carte fonctionne sans écran dans ctrl32 (la page opérateur est WEBview).
- Le lecteur microSD - ctrl32 garde le programme et les écrans dans la mémoire flash de la carte.

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
- [Makerfabs MaTouch ESP32-P4 7"](../../makerfabs/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.fr.md) - l'ESP32-P4 avec un écran tactile 7"

