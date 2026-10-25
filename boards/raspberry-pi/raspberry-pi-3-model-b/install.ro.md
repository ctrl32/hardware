---
title: Instalează runtime-ul ctrl32 pe Raspberry Pi 3 Model B+
slug: install
sidebar_position: 30
image: img/install-03-prepare.png
image_alt: Editorul ctrl32 pregătește Raspberry Pi 3 Model B+
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- install
---

# Instalează runtime-ul ctrl32

Runtime-ul Linux ctrl32 este programul de pe placă care rulează proiectul tău - ciclul PLC, ecranul de pe monitor, WEBview, OPC UA și magistralele. Editorul îl instalează prin rețea; nu se tastează nicio comandă Linux.

## 1. Scrie cardul

Scrie **Raspberry Pi OS Lite (64-bit)** pe card cu Raspberry Pi Imager.
*Lite* este intenționat: runtime-ul desenează singur ecranul și nu are
nevoie de desktop. În setările Imager-ului, înainte de scriere, setează:

- un **hostname** pe care îl vei recunoaște în rețea,
- un **utilizator** și **parola** lui,
- **SSH activat**,
- Wi-Fi-ul doar dacă Pi-ul nu va fi pe cablu.

Pune cardul în Pi, conectează Ethernet-ul și monitorul și pornește-l.

![Raspberry Pi 3 Model B+](img/board-01.jpg)

## 2. Creează proiectul

Pornește editorul ctrl32 și alege **New project** (Ctrl+N). Introdu **numele** proiectului, alege **Raspberry Pi** sub **Linux** și apasă **Create project**.

![Asistentul New project cu Raspberry Pi ales](img/install-02-new-project.png)

Pentru a porni în schimb de la exemplul gata făcut, deschide [proiectul all-in-one](examples/all-in-one/README.ro.md) (**File → Open**).

## 3. Pregătește placa

Alege **Online → Prepare a Linux device**. Introdu **adresa** plăcii, **utilizatorul** și **parola** de la pasul 1 și apasă **Look at the device**: editorul se autentifică, citește ce placă este și enumeră ce va face - privitul nu schimbă nimic. Apoi apasă **Prepare it**: editorul copiază runtime-ul, îl instalează ca serviciu, îl pornește și așteaptă până răspunde. De atunci placa pornește runtime-ul la fiecare boot.

![Prepare a Linux device: ce placă este și pașii pe care îi va face editorul](img/install-03-prepare.png)

Lasă bifat **Do not ask for the password again**: editorul pune propria cheie pe placă, iar vizitele ulterioare au nevoie doar de adresă. Parola este folosită o singură dată și nu este stocată niciodată.

Sub plan, **Operating system of this device** conține ce ține de Pi și nu
de proiect: HAT-ul CAN (un rând pentru fiecare cip CAN pe SPI), eliberarea
portului serial pentru un HAT RS-485, I2C, o adresă fixă și kernelul de
timp real pentru EtherCAT. Bifează ce are Pi-ul tău; fiecare rând bifat
este un pas, iar Pi-ul repornește doar când s-a schimbat o setare de boot.

## 4. Descarcă proiectul

Introdu adresa plăcii în selectorul de port din bara de instrumente și apasă butonul de descărcare (F5). Runtime-ul încarcă proiectul, iar ecranul apare pe monitor.

![Bara de instrumente: selectorul de port și butonul Download](img/install-05-download.png)

## 5. Verifică că rulează

- **ONLINE** (pictograma ștecher) arată valorile live în rungs, în variabile și pe ecran.
- **WEBview**: `http://<adresă>:8080` într-un browser din aceeași rețea.
- **OPC UA**: `opc.tcp://<adresă>:4840` - fiecare variabilă este un nod, `ns=1;s=<nume>`.

![Programul ladder în funcțiune - verde înseamnă că trece curentul](img/install-06-running.png)

| Port | Ce rulează acolo |
|---|---|
| 8080 | WEBview, încărcarea programului, găsirea dispozitivului |
| 4840 | serverul OPC UA |
| 3232 | conexiunea online a editorului |

Ceva nu funcționează? Vezi [Depanare](troubleshooting.ro.md).

*Capturi de ecran: editorul ctrl32 1.07.*

---

[← Hardware și cablare](hardware.ro.md) | [Prezentare](README.ro.md) | [Configurare →](configure.ro.md)
