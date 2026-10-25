---
title: 'Olimex ESP32-GATEWAY : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY - brochage
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Matériel et câblage

## Ce dont vous avez besoin

- L'Olimex ESP32-GATEWAY.
- Un câble de données USB-C - pour le chargement et pour l'alimentation (5 V).
- Un câble Ethernet et un port libre sur votre réseau.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- L'exemple all-in-one utilise le bouton (GPIO34) et la LED (GPIO33) propres à la carte - rien d'autre à câbler.

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| USB 5 V | le connecteur USB-C | alimentation et programmation |

## Brochage

![Olimex ESP32-GATEWAY - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
| 2 | SPI MOSI | ⚠ broche de strapping |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ utilisée par la carte |
| 6 | flash SPI du module | ⚠ utilisée par la carte |
| 7 | flash SPI du module | ⚠ utilisée par la carte |
| 8 | flash SPI du module | ⚠ utilisée par la carte |
| 9 | flash SPI du module | ⚠ utilisée par la carte |
| 10 | flash SPI du module | ⚠ utilisée par la carte |
| 11 | flash SPI du module | ⚠ utilisée par la carte |
| 13 | free (SPI CS line) |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ broche de strapping |
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ utilisée par la carte |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ utilisée par la carte |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ utilisée par la carte |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ utilisée par la carte |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ utilisée par la carte |
| 23 | Ethernet MDC (LAN8710A) | ⚠ utilisée par la carte |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ utilisée par la carte |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ utilisée par la carte |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ utilisée par la carte |
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | libre - le bouton de la carte | ⚠ entrée seule, ADC1 |

La barrette **EXT** de 20 broches porte les broches libres et les lignes
I2C / SPI. La LED de la carte est sur GPIO33 et son bouton sur GPIO34 (une
entrée seule). Peu de broches restent libres : davantage d'E/S passent par
Modbus TCP ou par des puces I2C.

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme.
- Les broches GPIO sont en 3,3 V. Un signal 24 V demande un optocoupleur
  ou un adaptateur de niveau ; une bobine de relais demande un driver (un
  module relais en possède un).

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
