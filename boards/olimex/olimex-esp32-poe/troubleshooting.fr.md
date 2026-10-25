---
title: 'Olimex ESP32-PoE : dépannage'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- troubleshooting
---

# Dépannage

| Symptôme | Cause | Solution |
|---|---|---|
| Le port COM n'apparaît pas, le sélecteur de port reste vide | Le câble ne transporte que l'alimentation, ou le pilote CH340 manque | Utilisez un câble de données ; installez le pilote CH340 (WCH CH341SER) ; essayez un autre port USB. |
| Flash runtime s'arrête pendant la connexion | Un autre programme occupe le port | Fermez le moniteur série ou l'autre outil qui tient le port ouvert, puis réessayez. |
| La carte redémarre toutes les quelques secondes | Le port USB ne peut pas fournir le courant pendant le démarrage d'Ethernet | Utilisez un hub USB alimenté ou une alimentation 5 V d'au moins 1 A, ou faites fonctionner la carte sur PoE (sans USB). |
| Le réseau ne monte pas | Pas de serveur DHCP, ou pas de liaison sur le port | Vérifiez les LED de liaison sur la prise ; définissez une adresse fixe sur la page Ethernet ; essayez un autre port du switch. |
| La carte est introuvable par son nom .local | Le réseau bloque le mDNS (multicast) | Utilisez l'adresse IP de la carte - la liste des clients du routeur et Find devices dans l'éditeur l'indiquent. |
| L'USB se déconnecte ou le PC signale une erreur quand le câble PoE est branché | L'USB et le PoE sont branchés en même temps sur une carte non isolée | Débranchez immédiatement l'un des deux. Chargez d'abord par USB, puis faites fonctionner sur PoE - ou utilisez l'ESP32-PoE-ISO. |
| Une sortie sur GPIO34 à GPIO39 ne fait rien | Ces broches sont des entrées seules | Déplacez la sortie sur GPIO33, GPIO4 ou GPIO5. |
| Une valeur Modbus reste à 0 | L'adresse de l'appareil, l'unité ou le registre est erroné, ou l'appareil est dans un autre sous-réseau | Vérifiez l'IP et l'unité de l'appareil dans l'arbre des appareils et le registre dans le manuel de l'appareil ; faites un ping de l'appareil depuis le PC. |

Le volet **Messages** de l'éditeur et le **tampon de diagnostic** de la carte (Online → Diagnostics) disent ce que le runtime a décidé et pourquoi - lisez-les d'abord.

---

[← Projets d'exemple](examples/README.fr.md) | [Vue d'ensemble](README.fr.md)
