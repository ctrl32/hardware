---
title: 'Olimex ESP32-P4-PC : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-PC - brochage
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Matériel et câblage

## Ce dont vous avez besoin

- L'Olimex ESP32-P4-PC.
- Un câble de données USB-C - pour le chargement et pour l'alimentation (5 V).
- Un câble Ethernet et un port libre sur votre réseau.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- En option : un élément Li-Po pour le secours par batterie ; pour l'exemple all-in-one, la LED utilisateur (GPIO2) est sur la carte et un bouton-poussoir va de GPIO14 à GND (EXT1) ; un transceiver CAN 3,3 V sur GPIO5 / GPIO15 et un transceiver RS-485 sur GPIO16 / GPIO17 / GPIO18 (DE).

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| USB 5 V | le connecteur USB-C | alimentation, programmation et débogage |
| Batterie Li-Po | le connecteur de batterie | chargée sur la carte ; prend le relais quand l'alimentation fait défaut (onduleur) |
| PoE | via l'extension PoE | en option |

## Brochage

![Olimex ESP32-P4-PC - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 14 | libre - E/S |  |
| 15 | libre - E/S |  |
| 16 | libre - E/S |  |
| 17 | libre - E/S |  |
| 18 | libre - E/S |  |
| 19 | libre - E/S |  |
| 20 | libre - E/S |  |
| 21 | USB HUB RST | ⚠  |
| 22 | I2C SDA |  |
| 23 | I2C SCL |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 29 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 30 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 31 | Ethernet MDC (IP101GRI) | ⚠ utilisée par la carte |
| 32 | libre - E/S |  |
| 33 | libre - E/S |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 35 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 36 | libre - E/S | ⚠ broche de strapping |
| 46 | libre - E/S |  |
| 47 | libre - E/S |  |
| 48 | libre - E/S |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 50 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ utilisée par la carte |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ utilisée par la carte |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Les broches libres sont sur la barrette **EXT1** de 20 broches : GPIO14 à
GPIO20, 32, 33, 36, 46, 47, 48 et la LED utilisateur sur GPIO2. Le
connecteur **UEXT** porte l'I2C (GPIO22 / GPIO23 - partagé avec le pont
HDMI), le SPI (GPIO4 / 53 / 54, CS GPIO5) et l'UART de la console.
L'ESP32-P4 n'a pas d'entrée analogique utilisée par ctrl32 : les signaux
analogiques passent par un ADC I2C (un ADS1115 sur UEXT) ou par un module
Modbus. Le CAN et le RS-485 se placent sur des broches EXT1 libres avec un
module transceiver 3,3 V.

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme.
- Les broches GPIO sont en 3,3 V. Un signal 24 V demande un optocoupleur
  ou un adaptateur de niveau ; une bobine de relais demande un driver (un
  module relais en possède un).

## Photos

![Olimex ESP32-P4-PC - photo 1](img/board-01.jpg)
![Olimex ESP32-P4-PC - photo 2](img/board-02.jpg)
![Olimex ESP32-P4-PC - photo 3](img/board-03.jpg)
![Olimex ESP32-P4-PC - photo 4](img/board-04.jpg)

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
