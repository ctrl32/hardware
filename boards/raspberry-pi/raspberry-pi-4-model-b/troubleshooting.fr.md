---
title: 'Raspberry Pi 4 Model B : dépannage'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Raspberry Pi 4 Model B
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
- troubleshooting
---

# Dépannage

| Symptôme | Cause | Solution |
|---|---|---|
| Look at the device ne parvient pas à se connecter | SSH est désactivé, l'adresse est erronée, ou le PC est dans un autre réseau | Activez SSH dans les réglages de l'Imager et réécrivez la carte ; faites un ping de l'adresse depuis le PC. |
| Prepare ne propose aucune installation | Le runtime ctrl32 est déjà installé sur le Pi | Un runtime installé se met à jour avec Flash runtime et l'adresse du Pi dans le sélecteur de port. |
| Le moniteur reste noir après le chargement | Le moniteur a été branché après le démarrage, ou le projet n'a pas d'écran | Branchez le moniteur avant de mettre le Pi sous tension ; ajoutez un écran au projet. |
| WEBview ne s'ouvre pas | Le mauvais port | Ouvrez http://<adresse>:8080 - le runtime sert sur le port 8080. |
| L'adaptateur USB-RS485 disparaît | Sous-tension - l'alimentation est trop faible | Utilisez l'alimentation officielle de 27 W. |
| Le CAN reste muet | Le pilote du HAT n'est pas chargé, pas de terminaison, ou un débit différent | Cochez le HAT dans Prepare a Linux device ; une résistance de 120 ohms aux deux extrémités du bus ; le même débit sur chaque nœud. |
| Un client OPC UA ne voit aucune variable | La variable est exclue du serveur, ou un pare-feu bloque le port 4840 | Vérifiez la coche OPC UA dans la liste des variables ; ouvrez le port 4840. |

Le volet **Messages** de l'éditeur et le **tampon de diagnostic** de la carte (Online → Diagnostics) disent ce que le runtime a décidé et pourquoi - lisez-les d'abord.

---

[← Projets d'exemple](examples/README.fr.md) | [Vue d'ensemble](README.fr.md)
