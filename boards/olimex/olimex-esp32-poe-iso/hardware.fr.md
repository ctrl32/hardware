---
title: 'Olimex ESP32-PoE-ISO : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-PoE-ISO - brochage
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Matériel et câblage

## Ce dont vous avez besoin

- L'Olimex ESP32-PoE-ISO (la variante WROOM-32E, sans PSRAM).
- Un câble de données micro-USB - pour le premier chargement du runtime.
- Pour l'alimentation : un switch / injecteur PoE (IEEE 802.3af), ou une alimentation USB 5 V.
- Un câble Ethernet et un port libre sur votre réseau.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- En option, pour l'exemple all-in-one : le bouton BUT1 est sur la carte ; un module relais ou une LED avec une résistance sur GPIO4 (UEXT) ; un potentiomètre (10 k) entre 3,3 V et GND avec son curseur sur GPIO33 (EXT2) ; un transceiver CAN 3,3 V sur GPIO5 (TX) / GPIO36 (RX).

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| PoE | la prise Ethernet, depuis un switch ou un injecteur PoE | IEEE 802.3af, isolée |
| USB 5 V | le connecteur micro-USB | la voie du premier chargement |
| Batterie Li-Po | le connecteur de batterie | chargée sur la carte |

L'alimentation PoE est **isolée galvaniquement** de la carte : contrairement
à l'ESP32-PoE simple, l'USB vers un PC et le PoE peuvent être branchés en
même temps - le runtime peut être chargé et observé en ligne pendant que la
carte reste sur son switch PoE.

## Brochage

![Olimex ESP32-PoE-ISO - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
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
| 33 | libre - E/S | ADC1 |
| 34 | libre - le bouton de la carte | ⚠ entrée seule, ADC1 |
| 35 | libre - entrée | ⚠ entrée seule, ADC1 |
| 36 | free (UART RX line) | ⚠ entrée seule, ADC1 |

Les broches libres se trouvent sur les barrettes **EXT1 / EXT2** (2,54 mm)
et sur le connecteur **UEXT**. GPIO34 à GPIO39 sont des entrées seules -
l'éditeur y refuse une sortie. Le connecteur UEXT porte l'I2C (GPIO13 /
GPIO16) et le SPI (GPIO14 / GPIO2 / GPIO15, partagé avec le lecteur
microSD).

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme.
- Les broches GPIO sont en 3,3 V. Une entrée 24 V demande un optocoupleur
  ou un adaptateur de niveau ; une bobine de relais demande un driver (un
  module relais en possède un).

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
