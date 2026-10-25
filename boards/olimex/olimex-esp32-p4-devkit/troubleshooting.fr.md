---
title: 'Olimex ESP32-P4-DevKit : dépannage'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-P4-DevKit
tags:
- esp32-p4
- ethernet
- olimex
- troubleshooting
---

# Dépannage

| Symptôme | Cause | Solution |
|---|---|---|
| Le port COM n'apparaît pas, le sélecteur de port reste vide | Le câble ne transporte que l'alimentation, ou le pilote USB manque | Utilisez un câble de données ; installez le pilote de la puce USB de la carte ; essayez un autre port USB. |
| Flash runtime s'arrête pendant la connexion | Un autre programme occupe le port | Fermez le moniteur série ou l'autre outil qui tient le port ouvert, puis réessayez. |
| La carte redémarre toutes les quelques secondes | Le port USB ne peut pas fournir le courant | Utilisez un hub USB alimenté ou une alimentation 5 V d'au moins 1 A. |
| Le réseau ne monte pas | Pas de serveur DHCP, ou pas de liaison sur le port | Vérifiez les LED de liaison sur la prise ; définissez une adresse fixe sur la page de la carte ; essayez un autre port du switch. |
| La carte est introuvable par son nom .local | Le réseau bloque le mDNS (multicast) | Utilisez l'adresse IP de la carte - la liste des clients du routeur et Find devices dans l'éditeur l'indiquent. |
| Une sortie ne fait rien | La broche est une entrée seule, ou la mauvaise broche a été indiquée | Vérifiez la broche sur la page de la carte - les broches d'entrée seule sont signalées ; déplacez la sortie sur une broche E/S libre. |
| Une valeur Modbus reste à 0 | L'adresse de l'appareil, l'unité ou le registre est erroné | Vérifiez l'IP et l'unité de l'appareil dans l'arbre des appareils, et le registre dans le manuel de l'appareil. |

Le volet **Messages** de l'éditeur et le **tampon de diagnostic** de la carte (Online → Diagnostics) disent ce que le runtime a décidé et pourquoi - lisez-les d'abord.

---

[← Projets d'exemple](examples/README.fr.md) | [Vue d'ensemble](README.fr.md)
