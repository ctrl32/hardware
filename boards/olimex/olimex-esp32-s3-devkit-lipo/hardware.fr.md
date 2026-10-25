---
title: 'Olimex ESP32-S3-DevKit-Lipo : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-S3-DevKit-Lipo - brochage
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Matériel et câblage

## Ce dont vous avez besoin

- L'Olimex ESP32-S3-DevKit-Lipo.
- Un câble de données USB-C - sur le connecteur marqué UART (le CH340X) pour le chargement.
- Le nom et le mot de passe de votre Wi-Fi 2,4 GHz.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- En option, pour l'exemple all-in-one : le bouton Boot/User (GPIO0) et la LED (GPIO38) sont sur la carte ; un potentiomètre (10 k) entre 3,3 V et GND avec son curseur sur GPIO1 ; un transceiver CAN 3,3 V sur GPIO10 / GPIO17 et un transceiver RS-485 sur GPIO18 / GPIO2 / GPIO4 (DE).

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| USB 5 V | l'un ou l'autre connecteur USB-C | alimentation et programmation |
| Batterie Li-Po | le connecteur de batterie | chargée sur la carte, basculement automatique |

## Brochage

![Olimex ESP32-S3-DevKit-Lipo - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
| 0 | libre - le bouton de la carte | ⚠ broche de strapping |
| 1 | libre - E/S | ADC1 |
| 2 | libre - E/S | ADC1 |
| 4 | libre - E/S | ADC1 |
| 5 | free (PWR SENSE line) | ADC1 |
| 6 | free (BAT SENSE line) | ADC1 |
| 7 | libre - E/S | ADC1 |
| 8 | libre - E/S | ADC1 |
| 9 | libre - E/S | ADC1 |
| 10 | free (SPI CS line) | ADC1 |
| 11 | SPI MOSI |  |
| 12 | SPI SCLK |  |
| 13 | SPI MISO |  |
| 14 | libre - E/S |  |
| 15 | libre - E/S |  |
| 16 | libre - E/S |  |
| 17 | free (UART TX line) |  |
| 18 | free (UART RX line) |  |
| 21 | libre - E/S |  |
| 38 | free (LED0 line) |  |
| 39 | libre - E/S |  |
| 40 | libre - E/S |  |
| 41 | libre - E/S |  |
| 42 | libre - E/S |  |
| 47 | I2C SCL |  |
| 48 | I2C SDA |  |

Les barrettes portent les GPIO libres ; l'ADC1 (les entrées analogiques
qu'utilise ctrl32) est sur GPIO1 à GPIO10. GPIO0 est le bouton Boot/User -
une entrée dans le programme, et maintenu à la mise sous tension il lance
le mode de téléchargement de la puce. Le connecteur pUEXT porte l'I2C
(GPIO48 / GPIO47) et le SPI.

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme.
- Les broches GPIO sont en 3,3 V. Un signal 24 V demande un optocoupleur
  ou un adaptateur de niveau ; une bobine de relais demande un driver (un
  module relais en possède un).

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
