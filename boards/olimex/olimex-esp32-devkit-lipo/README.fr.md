---
title: Olimex ESP32-DevKit-LiPo
slug: olimex-esp32-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-devkit-lipo/
image: img/board-01.jpg
image_alt: Carte Olimex ESP32-DevKit-LiPo avec ses deux barrettes de broches et le connecteur micro-USB
tags:
- esp32
- wifi
- battery
- olimex
---

# Olimex ESP32-DevKit-LiPo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Carte Olimex ESP32-DevKit-LiPo avec ses deux barrettes de broches et le connecteur micro-USB](img/board-01.jpg)

L'Olimex ESP32-DevKit-LiPo est une carte de développement ESP32 open source avec Wi-Fi, tous les GPIO du module sur deux barrettes et un chargeur Li-Po qui la maintient en marche lors d'une coupure de courant. Avec ctrl32, c'est un petit automate Wi-Fi : un programme ladder dans la puce, des entrées et des sorties sur ses broches, sa page opérateur dans tout navigateur (WEBview), Modbus TCP et MQTT.

**Convient pour :**

- Une commande Wi-Fi pour une pièce, une serre ou une pompe
- Un enregistreur de données secouru par batterie qui publie via MQTT
- Découvrir ctrl32 sur une plaque d'essai

Page de la carte dans le catalogue : [Olimex ESP32-DevKit-LiPo](https://ctrl32.com/hardware/boards/olimex-esp32-devkit-lipo/)

![Olimex ESP32-DevKit-LiPo - brochage : la fonction de chaque GPIO dans ctrl32](pinout/pinout.png)

## Ce que ctrl32 sait faire sur cette carte

<!-- capabilities:start -->
| Fonction | Sur cette carte | Remarques |
|---|---|---|
| Puce | ESP32 (ESP32-WROOM-32E-N4) |  |
| Mémoire | 4 MB flash |  |
| Taille du programme | 128 variables, 32 alarmes, 128 blocs | vérifié par l'éditeur avant un téléchargement |
| Entrées / sorties numériques | 19 GPIO libres | 4 dont entrées seules |
| Entrées analogiques | 6 sur la puce (ADC1) | GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO39 |
| Ethernet | non |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - sur des broches libres | nécessite un transceiver externe |
| Modbus RTU (RS-485) | oui - sur des broches libres | nécessite un transceiver externe |
| Modbus TCP | client et serveur |  |
| MQTT | oui | découverte Home Assistant |
| WEBview | oui | la page opérateur dans tout navigateur |
| Écran / tactile (HMI) | non | la page opérateur est WEBview |
| USB | Micro-USB (CH340 USB-UART) |  |
| Alimentation | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ce qui n'est pas pris en charge

- Le Bluetooth - l'ESP32 l'a, ctrl32 ne l'utilise pas.
- Les entrées de mesure de la batterie et de l'alimentation (GPIO35 / GPIO39) sont des broches libres dans ctrl32, pas une jauge de batterie.

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
- Olimex ESP32-S3-DevKit-Lipo - la même idée avec l'ESP32-S3 et de la PSRAM

