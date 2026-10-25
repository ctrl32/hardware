---
title: Installer le runtime ctrl32 sur la Raspberry Pi 3 Model B+
slug: install
sidebar_position: 30
image: img/install-03-prepare.png
image_alt: L'éditeur ctrl32 prépare la Raspberry Pi 3 Model B+
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- install
---

# Installer le runtime ctrl32

Le runtime Linux ctrl32 est le programme de la carte qui exécute votre projet - le cycle de l'automate, l'écran sur le moniteur, WEBview, OPC UA et les bus. L'éditeur l'installe par le réseau ; aucune commande Linux n'est tapée.

## 1. Écrire la carte SD

Écrivez **Raspberry Pi OS Lite (64-bit)** sur la carte avec le Raspberry
Pi Imager. *Lite* est voulu : le runtime dessine l'écran lui-même et n'a
pas besoin de bureau. Dans les réglages de l'Imager, avant l'écriture,
définissez :

- un **nom d'hôte** que vous reconnaîtrez sur le réseau,
- un **utilisateur** et son **mot de passe**,
- **SSH activé**,
- le Wi-Fi uniquement si le Pi ne sera pas sur un câble.

Insérez la carte dans le Pi, branchez l'Ethernet et le moniteur, et mettez
sous tension.

![Raspberry Pi 3 Model B+](img/board-01.jpg)

## 2. Créer le projet

Lancez l'éditeur ctrl32 et choisissez **New project** (Ctrl+N). Saisissez le **nom** du projet, choisissez **Raspberry Pi** sous **Linux** et appuyez sur **Create project**.

![L'assistant New project avec le Raspberry Pi choisi](img/install-02-new-project.png)

Pour partir plutôt de l'exemple prêt, ouvrez le [projet tout-en-un](examples/all-in-one/README.fr.md) (**File → Open**).

## 3. Préparer la carte

Choisissez **Online → Prepare a Linux device**. Saisissez l'**adresse** de la carte, l'**utilisateur** et le **mot de passe** de l'étape 1 et appuyez sur **Look at the device** : l'éditeur se connecte, lit ce qu'est la carte et liste ce qu'il va faire - regarder ne change rien. Appuyez ensuite sur **Prepare it** : l'éditeur copie le runtime, l'installe comme service, le démarre et attend qu'il réponde. Dès lors, la carte démarre le runtime à chaque démarrage.

![Prepare a Linux device : ce qu'est la carte et les étapes que l'éditeur va suivre](img/install-03-prepare.png)

Laissez **Do not ask for the password again** coché : l'éditeur dépose sa propre clé sur la carte, et les visites suivantes ne demandent que l'adresse. Le mot de passe sert une fois et n'est jamais enregistré.

Sous le plan, **Operating system of this device** regroupe ce qui
appartient au Pi plutôt qu'au projet : le HAT CAN (une ligne par puce CAN
sur SPI), la libération du port série pour un HAT RS-485, l'I2C, une
adresse fixe et le noyau temps réel pour EtherCAT. Cochez ce que porte
votre Pi ; chaque ligne cochée est une étape, et le Pi ne redémarre que si
un réglage de démarrage a changé.

## 4. Charger le projet

Saisissez l'adresse de la carte dans le sélecteur de port de la barre d'outils et appuyez sur le bouton de chargement (F5). Le runtime charge le projet et l'écran apparaît sur le moniteur.

![La barre d'outils : le sélecteur de port et le bouton Download](img/install-05-download.png)

## 5. Vérifier que cela fonctionne

- **ONLINE** (l'icône de prise) affiche les valeurs en direct dans les réseaux, les variables et l'écran.
- **WEBview** : `http://<adresse>:8080` dans un navigateur du même réseau.
- **OPC UA** : `opc.tcp://<adresse>:4840` - chaque variable est un nœud, `ns=1;s=<nom>`.

![Le programme ladder en marche - le vert indique le courant qui passe](img/install-06-running.png)

| Port | Ce qui s'y trouve |
|---|---|
| 8080 | WEBview, le chargement du programme, la recherche de l'appareil |
| 4840 | le serveur OPC UA |
| 3232 | la connexion en ligne de l'éditeur |

Quelque chose ne fonctionne pas ? Voir [Dépannage](troubleshooting.fr.md).

*Captures d'écran : éditeur ctrl32 1.07.*

---

[← Matériel et câblage](hardware.fr.md) | [Vue d'ensemble](README.fr.md) | [Configurer →](configure.fr.md)
