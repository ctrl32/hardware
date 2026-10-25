---
title: 'Olimex ESP32-P4-DevKit : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-DevKit - brochage
tags:
- esp32-p4
- ethernet
- olimex
---

# Matériel et câblage

## Ce dont vous avez besoin

- L'Olimex ESP32-P4-DevKit.
- Un câble de données USB-C - pour le chargement et pour l'alimentation (5 V).
- Un câble Ethernet et un port libre sur votre réseau.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- En option, pour l'exemple all-in-one : la LED (GPIO2) est sur la carte ; un bouton-poussoir de GPIO20 à GND ; un transceiver CAN 3,3 V sur GPIO5 / GPIO21 et un transceiver RS-485 sur GPIO22 / GPIO23 / GPIO32 (DE).

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| USB 5 V | le connecteur USB-C | alimentation, programmation et débogage |
| PoE | via l'extension PoE | en option |

## Brochage

![Olimex ESP32-P4-DevKit - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 7 | I2C SDA |  |
| 8 | I2C SCL |  |
| 20 | libre - E/S |  |
| 21 | libre - E/S |  |
| 22 | libre - E/S |  |
| 23 | libre - E/S |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 29 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 30 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 31 | Ethernet MDC (IP101GRI) | ⚠ utilisée par la carte |
| 32 | libre - E/S |  |
| 33 | libre - E/S |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 35 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 46 | libre - E/S |  |
| 47 | libre - E/S |  |
| 48 | libre - E/S |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 50 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ utilisée par la carte |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ utilisée par la carte |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Tous les GPIO sont sur les deux barrettes de 20 broches. L'ESP32-P4 n'a
pas d'entrée analogique utilisée par ctrl32 : les signaux analogiques
passent par un ADC I2C (un ADS1115 sur le connecteur pUEXT, I2C GPIO7 /
GPIO8) ou par un module Modbus.

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme.
- Les broches GPIO sont en 3,3 V. Un signal 24 V demande un optocoupleur
  ou un adaptateur de niveau ; une bobine de relais demande un driver (un
  module relais en possède un).

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
