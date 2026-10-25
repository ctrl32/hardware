---
title: Olimex ESP32-GATEWAY
slug: olimex-esp32-gateway
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-gateway/
image: img/board-01.jpg
image_alt: Carte Olimex ESP32-GATEWAY avec la prise Ethernet et le connecteur USB-C
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Olimex ESP32-GATEWAY

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Carte Olimex ESP32-GATEWAY avec la prise Ethernet et le connecteur USB-C](img/board-01.jpg)

L'Olimex ESP32-GATEWAY est une carte ESP32 compacte avec Ethernet 100 Mb et Wi-Fi - assez petite pour une boîte de dérivation. Avec ctrl32, c'est une passerelle avec sa propre logique : des appareils Modbus TCP lus et publiés via MQTT, un programme ladder dans la puce et sa page opérateur dans tout navigateur (WEBview).

**Convient pour :**

- Une passerelle Modbus TCP vers MQTT avec sa propre logique
- Une petite commande dans une boîte de dérivation, sur Ethernet
- La domotique - lire des compteurs, commuter via des modules d'E/S Modbus

Page de la carte dans le catalogue : [Olimex ESP32-GATEWAY](https://ctrl32.com/hardware/boards/olimex-esp32-gateway/)

![Olimex ESP32-GATEWAY - brochage : la fonction de chaque GPIO dans ctrl32](pinout/pinout.png)

## Ce que ctrl32 sait faire sur cette carte

<!-- capabilities:start -->
| Fonction | Sur cette carte | Remarques |
|---|---|---|
| Puce | ESP32 (ESP32-WROOM-32E-N4) |  |
| Mémoire | 4 MB flash |  |
| Taille du programme | 128 variables, 32 alarmes, 128 blocs | vérifié par l'éditeur avant un téléchargement |
| Entrées / sorties numériques | 3 GPIO libres | 1 dont entrées seules |
| Entrées analogiques | 2 sur la puce (ADC1) | GPIO33, GPIO34 |
| Ethernet | oui - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - sur des broches libres | nécessite un transceiver externe |
| Modbus RTU (RS-485) | oui - sur des broches libres | nécessite un transceiver externe |
| Modbus TCP | client et serveur |  |
| MQTT | oui | découverte Home Assistant |
| WEBview | oui | la page opérateur dans tout navigateur |
| Écran / tactile (HMI) | non | la page opérateur est WEBview |
| USB | USB-C (CH340 USB-UART) |  |
| Alimentation | 5 V USB |  |
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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.fr.md) - Ethernet et Power over Ethernet

