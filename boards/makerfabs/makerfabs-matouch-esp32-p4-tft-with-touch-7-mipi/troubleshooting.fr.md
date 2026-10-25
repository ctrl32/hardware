---
title: 'Makerfabs MaTouch ESP32-P4 7" : dépannage'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- troubleshooting
---

# Dépannage

| Symptôme | Cause | Solution |
|---|---|---|
| Le port COM n'apparaît pas | Le câble ne transporte que l'alimentation, ou le pilote CH340 manque | Utilisez un câble de données USB-C ; installez le pilote CH340 (WCH CH341SER) ; essayez un autre port USB. |
| La carte redémarre quand l'écran s'allume | L'alimentation ne peut pas porter le rétroéclairage | Utilisez une alimentation 5 V / 2 A ou un hub USB alimenté. |
| L'écran reste noir après l'écriture du runtime | Pas encore de projet sur la carte | Chargez le projet (F5) ; une carte sans projet n'affiche rien sur la dalle. |
| Le tactile ne répond pas, ou répond au mauvais endroit | L'orientation du projet diffère de la façon dont la carte est montée | Réglez l'orientation sur la page HMIview et chargez à nouveau. |
| Le réseau ne monte pas | Pas de serveur DHCP, ou pas de liaison sur le port | Vérifiez les LED de liaison sur la prise ; définissez une adresse fixe sur la page de la carte ; pour le Wi-Fi, vérifiez le nom du réseau et le mot de passe. |
| Le CAN reste muet | Pas de transceiver, pas de terminaison de 120 ohms, ou un débit différent | Vérifiez le transceiver sur GPIO20 / GPIO21, une résistance de 120 ohms aux deux extrémités du bus et le même débit sur chaque nœud. |
| Une valeur Modbus RTU reste à 0 | A et B inversés, une unité ou un débit erronés, ou la broche DE manquante | Inversez A et B ; vérifiez l'unité, le débit et la parité ; vérifiez que DE est câblée et indiquée. |

Le volet **Messages** de l'éditeur et le **tampon de diagnostic** de la carte (Online → Diagnostics) disent ce que le runtime a décidé et pourquoi - lisez-les d'abord.

---

[← Projets d'exemple](examples/README.fr.md) | [Vue d'ensemble](README.fr.md)
