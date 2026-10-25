---
title: 'Makerfabs MaTouch ESP32-P4 7" : matériel et câblage'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch ESP32-P4 7" - brochage
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Matériel et câblage

## Ce dont vous avez besoin

- La Makerfabs MaTouch ESP32-P4 TFT with Touch 7" MIPI.
- Un câble de données USB-C - pour le premier chargement du runtime et pour l'alimentation.
- Pour l'alimentation : une alimentation USB-C 5 V d'au moins 2 A (le rétroéclairage de l'écran en consomme l'essentiel).
- Un câble Ethernet, ou le Wi-Fi de votre réseau.
- Un PC avec l'[éditeur ctrl32](https://ctrl32.com/download/) (Windows).
- En option, pour l'exemple all-in-one : deux boutons-poussoirs et un module relais sur la barrette J6 ; un module ADS1115 sur le bus I2C ; un transceiver RS-485 3,3 V (par ex. MAX3485) et un transceiver CAN 3,3 V (par ex. SN65HVD230).

## Alimentation

| Source | Où | Remarque |
|---|---|---|
| USB 5 V | le connecteur USB-C | 2 A ou plus - le rétroéclairage 7" en consomme l'essentiel |
| Batterie Li-Po | le connecteur de batterie | 3,7 V, chargée sur la carte |

!!! warning "Une alimentation trop faible"
    Le port USB d'un PC ne peut souvent pas porter la carte avec le
    rétroéclairage allumé. Si la carte redémarre au moment où l'écran
    s'allume, utilisez une alimentation 5 V / 2 A ou un hub USB alimenté.

## Brochage

![Makerfabs MaTouch ESP32-P4 7" - brochage](pinout/pinout.png)

| GPIO | Fonction dans ctrl32 | Remarque |
|---|---|---|
| 0 | RTC XTAL P | ⚠  |
| 1 | RTC XTAL N | ⚠  |
| 2 | libre - E/S |  |
| 3 | libre - E/S |  |
| 4 | libre - E/S |  |
| 5 | libre - E/S |  |
| 6 | C6 IO2 | ⚠  |
| 7 | TOUCH SDA |  |
| 8 | TOUCH SCL |  |
| 20 | libre - E/S |  |
| 21 | libre - E/S |  |
| 22 | TOUCH RST |  |
| 23 | TFT BL |  |
| 26 | USB1 PAIR | ⚠  |
| 27 | DSI RST |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 29 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 30 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 31 | Ethernet MDC (IP101GRI) | ⚠ utilisée par la carte |
| 32 | libre - E/S |  |
| 33 | libre - E/S |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 35 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 36 | libre - E/S | ⚠ broche de strapping |
| 37 | CONSOLE RX | ⚠ broche de strapping |
| 38 | CONSOLE TX | ⚠ broche de strapping |
| 45 | MOSFET GATE | ⚠  |
| 46 | libre - E/S |  |
| 47 | libre - E/S |  |
| 48 | libre - E/S |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 50 | Ethernet RMII (IP101GRI) | ⚠ utilisée par la carte |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ utilisée par la carte |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ utilisée par la carte |
| 53 | AMP EN | ⚠  |
| 54 | C6 EN | ⚠  |

Les broches libres se trouvent sur les barrettes **J6** et **J10** et sur
les deux connecteurs Grove (**J1**, **J2**). Le bus I2C de la carte (GPIO7
/ GPIO8) porte le contrôleur tactile et le codec audio ; d'autres puces I2C
(un ADS1115, un capteur) rejoignent le même bus. Le CAN et le RS-485 n'ont
pas de transceiver sur la carte : l'exemple les place sur des broches
libres - **CAN** TX GPIO20 / RX GPIO21 (Grove J2), **RS-485** TX GPIO4 / RX
GPIO5 / DE GPIO32 (J10) - chacun vers un module transceiver 3,3 V.

## Sécurité

- La carte n'est pas destinée aux fonctions de sécurité. Un arrêt
  d'urgence, un contact de porte ou un rideau lumineux se câble en
  matériel, jamais à travers un programme ou un écran tactile.
- Les broches GPIO sont en 3,3 V. Un signal 24 V demande un optocoupleur ;
  une bobine de relais demande un driver (un module relais en possède un).
- Le tactile capacitif peut enregistrer un faux appui à côté d'une forte
  source de perturbations (un variateur). Les commandes critiques d'un
  écran demandent une confirmation.

## Photos

![Makerfabs MaTouch ESP32-P4 7" - photo 1](img/board-01.jpg)
![Makerfabs MaTouch ESP32-P4 7" - photo 2](img/board-02.jpg)
![Makerfabs MaTouch ESP32-P4 7" - photo 3](img/board-03.jpg)
![Makerfabs MaTouch ESP32-P4 7" - photo 4](img/board-04.jpg)
![Makerfabs MaTouch ESP32-P4 7" - photo 5](img/board-05.jpg)
![Makerfabs MaTouch ESP32-P4 7" - photo 6](img/board-06.jpg)
![Makerfabs MaTouch ESP32-P4 7" - photo 7](img/board-07.jpg)
![Makerfabs MaTouch ESP32-P4 7" - photo 8](img/board-08.jpg)

---

[← Vue d'ensemble](README.fr.md) | [Vue d'ensemble](README.fr.md) | [Installer le runtime →](install.fr.md)
