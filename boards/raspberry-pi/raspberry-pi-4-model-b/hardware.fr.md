---
title: 'Raspberry Pi 4 Model B : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Raspberry Pi 4 Model B - brochage
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Matériel et câblage

## Ce dont vous avez besoin

- Un Raspberry Pi 4 Model B (2 Go ou plus recommandés).
- Une carte microSD (16 Go ou plus) et le [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
- L'alimentation USB-C officielle (5 V / 3 A).
- Un câble Ethernet sur le même réseau que le PC.
- Pour l'IHM : un moniteur HDMI (câble micro-HDMI) ou un écran DSI ; avec un moniteur tactile, son USB.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- En option, pour l'exemple all-in-one : un adaptateur USB-RS485 avec un module d'E/S Modbus RTU et un capteur de température ; un HAT CAN (MCP2515 ou MCP251xFD).

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| USB-C | le connecteur d'alimentation | 5 V / 3 A - l'alimentation officielle |
| PoE | via un HAT PoE | en option |

!!! warning "Sous-tension"
    Avec une alimentation plus faible, le Pi réduit sa fréquence et limite
    le courant USB - un adaptateur USB-RS485 ou un moniteur tactile peut
    alors décrocher. Utilisez l'alimentation officielle.

## Brochage

![Raspberry Pi 4 Model B - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
| 2 | I2C1 SDA - puces I2C, RTC |  |
| 3 | I2C1 SCL |  |
| 4 | libre - non utilisée par ctrl32 | ⚠  |
| 8 | SPI0 CE0 - HAT CAN |  |
| 9 | SPI0 MISO - HAT CAN |  |
| 10 | SPI0 MOSI - HAT CAN |  |
| 11 | SPI0 SCLK - HAT CAN |  |
| 14 | UART TX - HAT RS-485 |  |
| 15 | UART RX - HAT RS-485 |  |
| 17 | libre - non utilisée par ctrl32 | ⚠  |
| 22 | libre - non utilisée par ctrl32 | ⚠  |
| 25 | Interruption du HAT CAN (MCP2515) |  |
| 27 | libre - non utilisée par ctrl32 | ⚠  |

Sur une carte Linux, les bus sont des **noms de périphériques**, pas des
broches : le runtime ouvre ce que nomment les réglages de l'appareil -
`can0` pour un HAT CAN ou un adaptateur USB, `/dev/ttyUSB0` pour un
adaptateur USB-RS485 (ou l'UART propre du Pi avec un HAT RS-485).
**Prepare a Linux device** les configure (étape 3 de l'installation). Le
second port Ethernet pour EtherCAT est un adaptateur Ethernet USB.

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme.
- Éteignez le Pi avant de couper son alimentation chaque fois que c'est
  possible - le runtime garde les valeurs rémanentes en sécurité, le
  système d'exploitation préfère un arrêt propre.

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
