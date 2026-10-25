---
title: Raspberry Pi 3 Model B+
slug: raspberry-pi-3-model-b
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-3-model-b/
image: img/board-01.jpg
image_alt: Carte Raspberry Pi 3 Model B+, vue de dessus
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Raspberry Pi 3 Model B+

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Carte Raspberry Pi 3 Model B+, vue de dessus](img/board-01.jpg)

Le Raspberry Pi 3 Model B+ fait tourner le runtime Linux ctrl32 : un grand programme, une IHM sur le moniteur HDMI, un serveur OPC UA pour le SCADA, CAN et RS-485 via des HAT ou des adaptateurs USB, Modbus et MQTT. Avec 1 Go de mémoire et un Cortex-A53 quadricœur, il convient à une commande de ligne ou à une passerelle ; la vision avec une caméra demande un Raspberry Pi 4 ou 5.

**Convient pour :**

- Une commande de ligne avec une IHM sur un moniteur HDMI et OPC UA vers le SCADA
- Un maître EtherCAT pour des servovariateurs
- Une passerelle entre Modbus, CAN, OPC UA et MQTT

Page de la carte dans le catalogue : [Raspberry Pi 3 Model B+](https://ctrl32.com/hardware/boards/raspberry-pi-3-model-b/)

![Raspberry Pi 3 Model B+ - brochage : la fonction de chaque GPIO dans ctrl32](pinout/pinout.png)

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
| USB | Micro-USB |  |
| Alimentation | 5 V USB |  |
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

-

## Étapes suivantes

- [documentation ctrl32](https://ctrl32.com/docs/) - l'éditeur, les langages, chaque bloc
- [Télécharger l'éditeur](https://ctrl32.com/download/)
- [Toutes les cartes testées](../../README.fr.md)
- [Raspberry Pi 5](../raspberry-pi-5/README.fr.md)
- [Raspberry Pi 4 Model B](../raspberry-pi-4-model-b/README.fr.md)
- [Le runtime Linux](https://ctrl32.com/docs/linux-runtime/) - ce qu'il fait et ses limites

