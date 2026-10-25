---
title: Raspberry Pi 5
slug: raspberry-pi-5
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-5/
image: img/board-01.jpg
image_alt: Carte Raspberry Pi 5, vue de dessus
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Raspberry Pi 5

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Carte Raspberry Pi 5, vue de dessus](img/board-01.jpg)

Le Raspberry Pi 5 fait tourner le runtime Linux ctrl32 - la plus grande cible de ctrl32 : des dizaines de milliers de variables, une IHM sur le moniteur HDMI, un serveur OPC UA pour le SCADA, des variateurs EtherCAT, CAN et RS-485 via des HAT ou des adaptateurs USB, et la vision industrielle avec une caméra. L'éditeur installe le runtime par le réseau ; le Pi le démarre ensuite à chaque démarrage.

**Convient pour :**

- Une commande de ligne avec une IHM sur un moniteur HDMI et OPC UA vers le SCADA
- Un maître EtherCAT pour des servovariateurs
- Une passerelle entre Modbus, CAN, OPC UA et MQTT

Page de la carte dans le catalogue : [Raspberry Pi 5](https://ctrl32.com/hardware/boards/raspberry-pi-5/)

![Raspberry Pi 5 - brochage : la fonction de chaque GPIO dans ctrl32](pinout/pinout.png)

## Ce que ctrl32 sait faire sur cette carte

<!-- capabilities:start -->
| Fonction | Sur cette carte | Remarques |
|---|---|---|
| Puce | Linux |  |
| Taille du programme | 20480 variables, 4096 alarmes, 40960 blocs | vérifié par l'éditeur avant un téléchargement |
| Entrées / sorties numériques | via des modules d'E/S | Modbus, CANopen, EtherCAT |
| Ethernet | oui |  |
| Wi-Fi | Wi-Fi 5 (2.4 + 5 GHz) |  |
| CAN | via un HAT CAN ou un adaptateur USB | SocketCAN, jusqu'à 4 bus |
| Modbus RTU (RS-485) | oui | un adaptateur USB ou un HAT |
| Modbus TCP | client et serveur |  |
| MQTT | oui (TLS aussi) | découverte Home Assistant |
| WEBview | oui | la page opérateur dans tout navigateur |
| Serveur OPC UA | oui |  |
| EtherCAT master | oui | sur un second port Ethernet |
| Écran (HMI) | HDMI ou un écran DSI | ou sans écran avec WEBview |
| USB | USB-C |  |
| Alimentation | USB-C PD 5 V / 5 A |  |
<!-- capabilities:end -->

### Ce qui n'est pas pris en charge

- La barrette GPIO de 40 broches comme E/S du programme - les entrées et les sorties passent par des modules d'E/S (Modbus RTU / TCP, CANopen, EtherCAT) ; la barrette porte les bus des HAT.
- Le Bluetooth.
- Un environnement de bureau - le runtime dessine l'écran lui-même ; le système qu'il attend est Raspberry Pi OS Lite.

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
| [raspberry-pi-5-mechanical-drawing.pdf](datasheets/raspberry-pi-5-mechanical-drawing.pdf) | Raspberry Pi 5 mechanical drawing |
| [raspberry-pi-5-rp1-peripherals.pdf](datasheets/raspberry-pi-5-rp1-peripherals.pdf) | RP1 peripherals |
| [raspberry-pi-5-3d.zip](3d/raspberry-pi-5-3d.zip) | Modèle 3D (GLB, zippé) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | d'où viennent les photos, les schémas et les modèles |

## Étapes suivantes

- [documentation ctrl32](https://ctrl32.com/docs/) - l'éditeur, les langages, chaque bloc
- [Télécharger l'éditeur](https://ctrl32.com/download/)
- Toutes les cartes testées
- Raspberry Pi 4 Model B
- Raspberry Pi 3 Model B+
- [Le runtime Linux](https://ctrl32.com/docs/linux-runtime/) - ce qu'il fait et ses limites

