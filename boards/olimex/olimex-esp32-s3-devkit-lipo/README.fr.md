---
title: Olimex ESP32-S3-DevKit-Lipo
slug: olimex-esp32-s3-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-s3-devkit-lipo/
image: img/board-01.jpg
image_alt: Carte Olimex ESP32-S3-DevKit-Lipo avec ses deux connecteurs USB-C et ses barrettes de broches
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Olimex ESP32-S3-DevKit-Lipo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Carte Olimex ESP32-S3-DevKit-Lipo avec ses deux connecteurs USB-C et ses barrettes de broches](img/board-01.jpg)

L'Olimex ESP32-S3-DevKit-Lipo est une carte ESP32-S3 open source avec 8 Mo de flash, 8 Mo de PSRAM, le Wi-Fi, deux ports USB-C et un chargeur Li-Po. Le S3 avec PSRAM est la puce de référence de ctrl32 : un programme ladder à la taille de programme complète, sa page opérateur dans tout navigateur (WEBview), Modbus TCP et MQTT avec TLS - le tout en Wi-Fi.

**Convient pour :**

- Un automate Wi-Fi avec de la marge - 512 variables, TLS vers un broker cloud
- Une commande secourue par batterie qui continue de fonctionner lors d'une coupure de courant
- Le développement de votre propre carte sur l'ESP32-S3

Page de la carte dans le catalogue : [Olimex ESP32-S3-DevKit-Lipo](https://ctrl32.com/hardware/boards/olimex-esp32-s3-devkit-lipo/)

![Olimex ESP32-S3-DevKit-Lipo - brochage : la fonction de chaque GPIO dans ctrl32](pinout/pinout.png)

## Ce que ctrl32 sait faire sur cette carte

<!-- capabilities:start -->
| Fonction | Sur cette carte | Remarques |
|---|---|---|
| Puce | ESP32-S3 (ESP32-S3-WROOM-1-N8R8) |  |
| Mémoire | 8 MB flash, 8 MB PSRAM |  |
| Taille du programme | 512 variables, 128 alarmes, 1024 blocs | vérifié par l'éditeur avant un téléchargement |
| Entrées / sorties numériques | 21 GPIO libres | voir le brochage |
| Entrées analogiques | 9 sur la puce (ADC1) | GPIO1, GPIO2, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 |
| Ethernet | non |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - sur des broches libres | nécessite un transceiver externe |
| Modbus RTU (RS-485) | oui - sur des broches libres | nécessite un transceiver externe |
| Modbus TCP | client et serveur |  |
| MQTT | oui (TLS aussi) | découverte Home Assistant |
| WEBview | oui | la page opérateur dans tout navigateur |
| Écran / tactile (HMI) | non | la page opérateur est WEBview |
| USB | USB-C (CH340X USB-UART, Native USB) |  |
| Alimentation | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ce qui n'est pas pris en charge

- Le Bluetooth - l'ESP32-S3 l'a, ctrl32 ne l'utilise pas.
- Les entrées de mesure de la batterie et de l'alimentation (GPIO5 / GPIO6) sont des broches libres dans ctrl32, pas une jauge de batterie.

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
- [Olimex ESP32-DevKit-LiPo](../olimex-esp32-devkit-lipo/README.fr.md) - la version avec l'ESP32 classique

