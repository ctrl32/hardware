---
title: 'LaskaKit ESPlan : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: LaskaKit ESPlan - brochage
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Matériel et câblage

## Ce dont vous avez besoin

- La LaskaKit ESPlan.
- Un câble de données USB-C - pour le premier chargement du runtime.
- Pour l'alimentation : 12 ou 24 V DC sur le bornier à vis (7-40 V), ou 5 V par USB-C.
- Un câble Ethernet et un port libre sur votre réseau.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- En option, pour l'exemple all-in-one : un capteur de température Modbus RTU (unité 1) sur le bornier RS-485 ; un bouton-poussoir de GPIO16 à GND ; un potentiomètre (10 k) entre 3,3 V et GND avec son curseur sur GPIO35 ; un transceiver CAN 3,3 V sur GPIO14 (TX) / GPIO39 (RX).

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| 7-40 V DC | le bornier à vis | 12 ou 24 V recommandés |
| USB 5 V | le connecteur USB-C | la voie du premier chargement |
| PoE | via le module PoE optionnel (802.3af) | module additionnel |

## Brochage

![LaskaKit ESPlan - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
| 0 | free (LED0 line) | ⚠ broche de strapping |
| 4 | RS485 TX |  |
| 5 | Ethernet PHY power (LAN8720A) | ⚠ utilisée par la carte |
| 6 | flash SPI du module | ⚠ utilisée par la carte |
| 7 | flash SPI du module | ⚠ utilisée par la carte |
| 8 | flash SPI du module | ⚠ utilisée par la carte |
| 9 | flash SPI du module | ⚠ utilisée par la carte |
| 10 | flash SPI du module | ⚠ utilisée par la carte |
| 11 | flash SPI du module | ⚠ utilisée par la carte |
| 12 | SPI MISO | ⚠ broche de strapping |
| 13 | SPI MOSI |  |
| 14 | free (SPI SCLK line) |  |
| 15 | SPI CS | ⚠ broche de strapping |
| 16 | libre - E/S |  |
| 17 | Ethernet 50 MHz clock (LAN8720A) | ⚠ utilisée par la carte |
| 18 | Ethernet MDIO (LAN8720A) | ⚠ utilisée par la carte |
| 19 | Ethernet RMII TXD0 (LAN8720A) | ⚠ utilisée par la carte |
| 21 | Ethernet RMII TX_EN (LAN8720A) | ⚠ utilisée par la carte |
| 22 | Ethernet RMII TXD1 (LAN8720A) | ⚠ utilisée par la carte |
| 23 | Ethernet MDC (LAN8720A) | ⚠ utilisée par la carte |
| 25 | Ethernet RMII RXD0 (LAN8720A) | ⚠ utilisée par la carte |
| 26 | Ethernet RMII RXD1 (LAN8720A) | ⚠ utilisée par la carte |
| 27 | Ethernet RMII CRS_DV (LAN8720A) | ⚠ utilisée par la carte |
| 32 | TOUCH SCL |  |
| 33 | TOUCH SDA |  |
| 35 | libre - entrée | ⚠ entrée seule, ADC1 |
| 36 | RS485 RX |  |
| 39 | libre - entrée | ⚠ entrée seule, ADC1 |

**RS-485 :** A et B sur le bornier, le transceiver WS3081 sur GPIO4 (TX) /
GPIO36 (RX) ; un cavalier enclenche la terminaison de 120 ohms - placez-la
uniquement aux deux extrémités de la ligne. Les connecteurs **uSup**
portent l'I2C (GPIO33 / GPIO32) et le SPI. La LED de la carte est sur
GPIO0 (une broche de strapping - gardez-la comme sortie pilotée par le
programme).

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme.
- Les broches GPIO sont en 3,3 V. Un signal 24 V demande un optocoupleur
  ou un adaptateur de niveau ; une bobine de relais demande un driver (un
  module relais en possède un).

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
