---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Carte Olimex ESP32-P4-PC avec la prise Ethernet, les ports USB et le connecteur HDMI
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Carte Olimex ESP32-P4-PC avec la prise Ethernet, les ports USB et le connecteur HDMI](img/board-01.jpg)

L'Olimex ESP32-P4-PC est un petit ordinateur sur l'ESP32-P4 - double cœur à 400 MHz avec 32 Mo de PSRAM - avec Ethernet 100 Mb, quatre ports USB hôte, HDMI, audio et une batterie Li-Po qui le maintient en marche lors d'une coupure de courant. Avec ctrl32, c'est une commande filaire avec le plus grand programme qu'un ESP32 exécute - 4096 variables - sa page opérateur dans tout navigateur (WEBview), Modbus TCP, MQTT avec TLS, et CAN ou RS-485 sur les broches libres de sa barrette.

**Convient pour :**

- Un automate filaire qui traverse une coupure de courant sur sa propre batterie
- Une passerelle avec une logique conséquente entre Modbus TCP, CAN et MQTT
- Une commande en boîtier, alimentée par PoE (avec l'extension)

Page de la carte dans le catalogue : [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC - brochage : la fonction de chaque GPIO dans ctrl32](pinout/pinout.png)

## Ce que ctrl32 sait faire sur cette carte

<!-- capabilities:start -->
| Fonction | Sur cette carte | Remarques |
|---|---|---|
| Puce | ESP32-P4 (ESP32-P4NRW32) |  |
| Mémoire | 16 MB flash, 32 MB PSRAM |  |
| Taille du programme | 4096 variables, 512 alarmes, 1024 blocs | vérifié par l'éditeur avant un téléchargement |
| Entrées / sorties numériques | 15 GPIO libres | voir le brochage |
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
| Alimentation | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Ce qui n'est pas pris en charge

- La sortie HDMI et les connecteurs MIPI DSI / CSI - cette carte fonctionne sans écran dans ctrl32 (la page opérateur est WEBview).
- Les ports USB hôte et la sortie audio.
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

| Fichier | Quoi |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | le brochage, en vectoriel (aussi en [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | d'où viennent les photos, les schémas et les modèles |

## Étapes suivantes

- [documentation ctrl32](https://ctrl32.com/docs/) - l'éditeur, les langages, chaque bloc
- [Télécharger l'éditeur](https://ctrl32.com/download/)
- [Toutes les cartes testées](../../README.fr.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.fr.md) - le même ESP32-P4 sur une carte plus petite

