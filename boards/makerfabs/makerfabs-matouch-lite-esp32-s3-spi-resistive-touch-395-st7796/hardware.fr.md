---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95" : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95" - brochage
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Matériel et câblage

## Ce dont vous avez besoin

- La Makerfabs MaTouch Lite ESP32-S3 3,95" (ST7796).
- Un câble de données USB-C - pour le chargement et pour l'alimentation.
- Le nom et le mot de passe de votre Wi-Fi 2,4 GHz.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- En option, pour l'exemple all-in-one : un module relais ou une LED sur GPIO4, un potentiomètre (10 k) entre 3,3 V et GND avec son curseur sur GPIO5 (les connecteurs JST), et un transceiver CAN 3,3 V (par ex. SN65HVD230) sur GPIO6 / GPIO7.

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| USB 5 V | le connecteur USB-C | alimentation et programmation |
| Batterie Li-Po | le connecteur de batterie | 3,7 V |

## Brochage

![Makerfabs MaTouch Lite ESP32-S3 3.95" - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
| 0 | BOOT BTN | ⚠ broche de strapping |
| 1 | TFT RST |  |
| 2 | SD CMD | ⚠  |
| 4 | libre - E/S | ADC1 |
| 5 | libre - E/S | ADC1 |
| 6 | libre - E/S | ADC1 |
| 7 | libre - E/S | ADC1 |
| 13 | TFT MOSI |  |
| 14 | TFT SCLK |  |
| 15 | TFT CS |  |
| 21 | TFT DC |  |
| 38 | TOUCH SDA |  |
| 39 | TOUCH SCL |  |
| 40 | TOUCH INT |  |
| 41 | SD DO | ⚠  |
| 42 | SD SCLK | ⚠  |
| 48 | TFT BL |  |

Les deux connecteurs **JST** portent les quatre broches libres (GPIO4 à
GPIO7) - peu nombreuses, si bien que l'exemple y place la sortie, l'entrée
analogique et le CAN ; davantage d'E/S passent par Modbus TCP ou par des
puces I2C. L'écran, le contrôleur tactile et le lecteur microSD occupent
le reste des broches.

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme ou un écran tactile.
- Les broches GPIO sont en 3,3 V. Une bobine de relais demande un driver (un module relais en possède un).

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
