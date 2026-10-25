---
title: 'Olimex ESP32-EVB : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-EVB - brochage
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Matériel et câblage

## Ce dont vous avez besoin

- L'Olimex ESP32-EVB.
- Un câble de données micro-USB - pour le premier chargement du runtime.
- Pour l'alimentation : une alimentation USB 5 V, ou 5 V sur le bornier à vis.
- Un câble Ethernet et un port libre sur votre réseau.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- En option, pour l'exemple all-in-one : un potentiomètre (10 k) entre 3,3 V et GND avec son curseur sur GPIO36 (UEXT) ; un nœud CAN ou un adaptateur CAN et deux terminaisons de 120 ohms.
- En option : l'écran Olimex MOD-LCD2.8RTP (2,8 pouces, 240 x 320, tactile résistif) sur le connecteur UEXT.

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| USB 5 V | le connecteur micro-USB | la voie du premier chargement |
| 5 V DC | le bornier à vis | pour une armoire |
| Batterie Li-Po | le connecteur de batterie | chargée sur la carte |

!!! warning "Les relais commutent la tension du secteur"
    Câblez les contacts des relais uniquement carte hors tension, dans un
    boîtier, par une personne habilitée à intervenir sur les installations
    secteur. Les contacts supportent 10 A / 250 VAC ; un moteur ou un
    chauffage au-delà demande un contacteur piloté par le relais.

## Brochage

![Olimex ESP32-EVB - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ utilisée par la carte |
| 2 | TFT MOSI | ⚠ broche de strapping |
| 2 | SPI MOSI | ⚠ broche de strapping |
| 4 | free (UART TX line) |  |
| 5 | CAN TX |  |
| 6 | flash SPI du module | ⚠ utilisée par la carte |
| 7 | flash SPI du module | ⚠ utilisée par la carte |
| 8 | flash SPI du module | ⚠ utilisée par la carte |
| 9 | flash SPI du module | ⚠ utilisée par la carte |
| 10 | flash SPI du module | ⚠ utilisée par la carte |
| 11 | flash SPI du module | ⚠ utilisée par la carte |
| 13 | I2C SDA |  |
| 14 | TFT SCLK |  |
| 14 | SPI SCLK |  |
| 15 | TFT DC | ⚠ broche de strapping |
| 15 | SPI MISO | ⚠ broche de strapping |
| 16 | I2C SCL |  |
| 17 | TFT CS |  |
| 17 | free (SPI CS line) |  |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ utilisée par la carte |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ utilisée par la carte |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ utilisée par la carte |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ utilisée par la carte |
| 23 | Ethernet MDC (LAN8710A) | ⚠ utilisée par la carte |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ utilisée par la carte |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ utilisée par la carte |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ utilisée par la carte |
| 32 | free (REL1 line) | ADC1 |
| 33 | free (REL2 line) | ADC1 |
| 34 | libre - le bouton de la carte | ⚠ entrée seule, ADC1 |
| 35 | CAN RX |  |
| 36 | free (UART RX line) | ⚠ entrée seule, ADC1 |

**Relais :** REL1 sur GPIO32, REL2 sur GPIO33. **Bouton :** BUT1 sur
GPIO34 (entrée seule). **CAN :** le transceiver de la carte sur GPIO5 (TX)
/ GPIO35 (RX), CAN_H / CAN_L sur le bornier - terminez le bus par 120 ohms
aux deux extrémités. Le connecteur **UEXT** porte l'I2C (GPIO13 / GPIO16),
le SPI et un UART libre (GPIO4 / GPIO36) ; l'écran optionnel utilise ses
lignes SPI.

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme.
- Les broches GPIO sont en 3,3 V. Un signal 24 V demande un optocoupleur
  ou un adaptateur de niveau ; une bobine de relais demande un driver (un
  module relais en possède un).

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
