---
title: Makerfabs MaTouch ESP32-P4 7"
slug: makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/board-01.jpg
image_alt: Carte Makerfabs MaTouch ESP32-P4 7 pouces avec son écran tactile 1024x600
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Makerfabs MaTouch ESP32-P4 7"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 1024x600](https://img.shields.io/badge/HMI-1024x600-0891b2)

![Carte Makerfabs MaTouch ESP32-P4 7 pouces avec son écran tactile 1024x600](img/board-01.jpg)

La Makerfabs MaTouch ESP32-P4 7" est un écran tactile complet sur une seule carte : un afficheur MIPI de 1024 x 600 avec tactile capacitif, l'ESP32-P4 double cœur avec 32 Mo de PSRAM, Ethernet et le Wi-Fi 6 via un ESP32-C6. Avec ctrl32, c'est une IHM et un automate en un - des écrans dessinés dans l'éditeur tournent sur la dalle, un programme ladder tourne à côté, et les mêmes valeurs atteignent tout navigateur (WEBview), des appareils Modbus, le CAN et MQTT.

**Convient pour :**

- Un pupitre opérateur sur une machine, avec sa propre logique
- Un écran mural de maison connectée ou de gestion du bâtiment
- Une passerelle Modbus / CAN avec un écran

Page de la carte dans le catalogue : [Makerfabs MaTouch ESP32-P4 7"](https://ctrl32.com/hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/)

![Makerfabs MaTouch ESP32-P4 7" - brochage : la fonction de chaque GPIO dans ctrl32](pinout/pinout.png)

## Ce que ctrl32 sait faire sur cette carte

<!-- capabilities:start -->
| Fonction | Sur cette carte | Remarques |
|---|---|---|
| Puce | ESP32-P4 (ESP32-P4NRW32) |  |
| Mémoire | 16 MB flash, 32 MB PSRAM |  |
| Taille du programme | 4096 variables, 512 alarmes, 512 blocs | vérifié par l'éditeur avant un téléchargement |
| Entrées / sorties numériques | 12 GPIO libres | voir le brochage |
| Entrées analogiques | via un convertisseur A/N I2C (ADS1115) |  |
| Ethernet | oui - IP101GRI |  |
| Wi-Fi | Wi-Fi 6 (2.4 GHz) |  |
| CAN (TWAI) | 1 | nécessite un transceiver externe |
| Modbus RTU (RS-485) | oui | sur des broches libres, nécessite un transceiver externe |
| Modbus TCP | client et serveur |  |
| MQTT | oui (TLS aussi) | découverte Home Assistant |
| WEBview | oui | la page opérateur dans tout navigateur |
| Écran / tactile (HMI) | 7" 1024x600, GT911 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Alimentation | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Ce qui n'est pas pris en charge

- La caméra (SC2336 sur MIPI CSI) - ctrl32 ne fait de la vision que sur le runtime Linux 64 bits.
- Le codec audio, le microphone et la sortie haut-parleur.
- Le Bluetooth de l'ESP32-C6.
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
| [makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf](schematics/makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf) | MaTouch ESP32-P4 TFT with Touch 7“ V1.2 |
| [makerfabs-matouch-p4-7-display-datasheet.pdf](datasheets/makerfabs-matouch-p4-7-display-datasheet.pdf) | 7" 1024x600 MIPI display AML070JGI50 datasheet |
| [makerfabs-matouch-p4-es8311-datasheet.pdf](datasheets/makerfabs-matouch-p4-es8311-datasheet.pdf) | ES8311 audio codec datasheet |
| [esp32-p4-datasheet.pdf](datasheets/esp32-p4-datasheet.pdf) | ESP32-P4 datasheet (pre-release) |
| [makerfabs-matouch-p4-sc2336-camera-datasheet.pdf](datasheets/makerfabs-matouch-p4-sc2336-camera-datasheet.pdf) | SC2336 2 MP MIPI camera module datasheet |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | d'où viennent les photos, les schémas et les modèles |

## Étapes suivantes

- [documentation ctrl32](https://ctrl32.com/docs/) - l'éditeur, les langages, chaque bloc
- [Télécharger l'éditeur](https://ctrl32.com/download/)
- Toutes les cartes testées
- Makerfabs MaTouch Lite ESP32-S3 3.95" - la petite sœur
- [Écran de maison connectée sur la MaTouch ESP32-P4](https://ctrl32.com/examples/smart-home-control-panel-on-an-esp32-p4-7-touch-display/) - un exemple complet sur le web

