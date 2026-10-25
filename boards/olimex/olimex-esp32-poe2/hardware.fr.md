---
title: 'Olimex ESP32-POE2 : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-POE2 - brochage
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Matériel et câblage

## Ce dont vous avez besoin

- L'Olimex ESP32-POE2.
- Un câble de données USB-C - pour le premier chargement du runtime.
- Pour l'alimentation : un switch / injecteur PoE (IEEE 802.3at, classe 4 pour les 25 W complets), ou une alimentation USB 5 V.
- Un câble Ethernet et un port libre sur votre réseau.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- En option, pour l'exemple all-in-one : le bouton BUT1 est sur la carte ; un module relais ou une LED sur GPIO4 (UEXT) ; un potentiomètre (10 k) entre 3,3 V et GND avec son curseur sur GPIO36 ; un transceiver CAN 3,3 V sur GPIO5 (TX) / GPIO39 (RX).

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| PoE | la prise Ethernet | IEEE 802.3at classe 4, jusqu'à 25 W |
| USB 5 V | le connecteur USB-C | la voie du premier chargement |
| Batterie Li-Po | le connecteur de batterie | chargée sur la carte |

Alimentée par Ethernet, la carte alimente des circuits externes : **24 V /
0,75 A ou 12 V / 1,5 A** (un cavalier choisit), **5 V / 1,5 A** et
**3,3 V / 1 A**, 25 W au total.

!!! danger "Ne branchez jamais l'USB et le PoE en même temps"
    L'ESP32-POE2 n'est **pas isolée galvaniquement** de l'alimentation
    Ethernet. Chargez le runtime par USB avec le câble Ethernet débranché
    (ou depuis un port sans PoE), puis faites fonctionner la carte sur PoE.

## Brochage

![Olimex ESP32-POE2 - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ utilisée par la carte |
| 2 | SPI MOSI | ⚠ broche de strapping |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | flash SPI du module | ⚠ utilisée par la carte |
| 7 | flash SPI du module | ⚠ utilisée par la carte |
| 8 | flash SPI du module | ⚠ utilisée par la carte |
| 9 | flash SPI du module | ⚠ utilisée par la carte |
| 10 | flash SPI du module | ⚠ utilisée par la carte |
| 11 | flash SPI du module | ⚠ utilisée par la carte |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ utilisée par la carte |
| 13 | I2C SDA |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ broche de strapping |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ utilisée par la carte |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ utilisée par la carte |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ utilisée par la carte |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ utilisée par la carte |
| 23 | Ethernet MDC (LAN8710A) | ⚠ utilisée par la carte |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ utilisée par la carte |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ utilisée par la carte |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ utilisée par la carte |
| 33 | I2C SCL |  |
| 34 | libre - le bouton de la carte | ⚠ entrée seule, ADC1 |
| 36 | free (UART RX line) | ⚠ entrée seule, ADC1 |
| 39 | libre - entrée | ⚠ entrée seule, ADC1 |

Les broches libres se trouvent sur les barrettes **EXT** et sur le
connecteur **UEXT**. GPIO34 à GPIO39 sont des entrées seules. La PSRAM du
module occupe GPIO16 / GPIO17, si bien que l'horloge Ethernet passe sur
GPIO0 et que l'I2C utilise GPIO13 / GPIO33.

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme.
- Les broches GPIO sont en 3,3 V. Une entrée 24 V demande un optocoupleur
  ou un adaptateur de niveau ; une bobine de relais demande un driver (un
  module relais en possède un).

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
