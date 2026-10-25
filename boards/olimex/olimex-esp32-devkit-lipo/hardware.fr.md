---
title: 'Olimex ESP32-DevKit-LiPo : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-DevKit-LiPo - brochage
tags:
- esp32
- wifi
- battery
- olimex
---

# Matériel et câblage

## Ce dont vous avez besoin

- L'Olimex ESP32-DevKit-LiPo.
- Un câble de données micro-USB - pour le chargement et pour l'alimentation (5 V).
- Le nom et le mot de passe de votre Wi-Fi 2,4 GHz.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- En option, pour l'exemple all-in-one : un bouton-poussoir de GPIO13 à GND ; un module relais ou une LED avec une résistance sur GPIO4 ; un potentiomètre (10 k) entre 3,3 V et GND avec son curseur sur GPIO32 ; un transceiver CAN 3,3 V sur GPIO14 / GPIO34 et un transceiver RS-485 sur GPIO16 / GPIO36 / GPIO17 (DE) ; un élément Li-Po en secours.

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| USB 5 V | le connecteur micro-USB | alimentation et programmation |
| Batterie Li-Po | le connecteur de batterie | chargée sur la carte, prend le relais quand l'USB fait défaut |

## Brochage

![Olimex ESP32-DevKit-LiPo - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
| 4 | libre - E/S |  |
| 6 | flash SPI du module | ⚠ utilisée par la carte |
| 7 | flash SPI du module | ⚠ utilisée par la carte |
| 8 | flash SPI du module | ⚠ utilisée par la carte |
| 9 | flash SPI du module | ⚠ utilisée par la carte |
| 10 | flash SPI du module | ⚠ utilisée par la carte |
| 11 | flash SPI du module | ⚠ utilisée par la carte |
| 13 | libre - E/S |  |
| 14 | libre - E/S |  |
| 16 | libre - E/S |  |
| 17 | libre - E/S |  |
| 18 | libre - E/S |  |
| 19 | libre - E/S |  |
| 21 | libre - E/S |  |
| 22 | libre - E/S |  |
| 23 | libre - E/S |  |
| 25 | libre - E/S |  |
| 26 | libre - E/S |  |
| 27 | libre - E/S |  |
| 32 | libre - E/S | ADC1 |
| 33 | libre - E/S | ADC1 |
| 34 | libre - entrée | ⚠ entrée seule, ADC1 |
| 35 | free (BAT SENSE line) | ⚠ entrée seule, ADC1 |
| 36 | libre - entrée | ⚠ entrée seule, ADC1 |
| 39 | free (PWR SENSE line) | ⚠ entrée seule, ADC1 |

Les deux barrettes portent les GPIO libres du module. GPIO34 à GPIO39 sont
des entrées seules ; GPIO0, 2, 12 et 15 sont des broches de strapping -
réservez-les aux entrées ou testez-les avant de les utiliser. Un bouton
vers GND n'a pas besoin de résistance : ctrl32 le lit inversé avec le
pull-up de la puce.

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme.
- Les broches GPIO sont en 3,3 V. Un signal 24 V demande un optocoupleur
  ou un adaptateur de niveau ; une bobine de relais demande un driver (un
  module relais en possède un).

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
