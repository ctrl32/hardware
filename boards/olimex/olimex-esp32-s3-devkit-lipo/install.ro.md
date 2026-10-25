---
title: Instalează runtime-ul ctrl32 pe Olimex ESP32-S3-DevKit-Lipo
slug: install
sidebar_position: 30
image: img/install-04-flash-runtime.png
image_alt: Editorul ctrl32 scrie runtime-ul pe Olimex ESP32-S3-DevKit-Lipo
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
- install
---

# Instalează runtime-ul ctrl32

Runtime-ul este programul de pe placă care rulează proiectul tău - ciclul PLC, ecranele, comunicația. Ajunge pe placă o singură dată; după aceea fiecare modificare a proiectului este o descărcare care nu rescrie nimic în afară de proiect.

## 1. Conectează placa

Conectează placa la PC cu cablul USB. Folosește pentru încărcare conectorul USB-C al convertorului **CH340X**.
Windows 10 și 11 îi instalează driverul singure; dacă portul nu apare,
instalează driverul CH340 de la producătorul cipului (WCH). Celălalt
conector este USB-ul nativ al cipului - și el alimentează placa.

![Olimex ESP32-S3-DevKit-Lipo](img/board-01.jpg)

## 2. Creează proiectul

Pornește editorul ctrl32 și alege **New project** (Ctrl+N). Introdu **numele** proiectului, alege **Olimex ESP32-S3-DevKit-LiPo** în lista de plăci (sub **Olimex**) și apasă **Create project**.

![Asistentul New project cu Olimex ESP32-S3-DevKit-Lipo ales](img/install-02-new-project.png)

Pentru a porni în schimb de la exemplul gata făcut, deschide [proiectul all-in-one](examples/all-in-one/README.ro.md) (**File → Open**).

## 3. Scrie runtime-ul

Alege portul COM al plăcii în selectorul de port din bara de instrumente, fă clic pe placă în arborele de dispozitive și apasă **Flash runtime**. Editorul scrie runtime-ul, îl citește înapoi și îl verifică; durează cam un minut, iar placa repornește. Acest lucru se face o dată - și din nou doar când editorul aduce o nouă linie de runtime.

![Dialogul Flash runtime cu runtime-ul pentru Olimex ESP32-S3-DevKit-Lipo](img/install-04-flash-runtime.png)

## 4. Descarcă proiectul

Apasă butonul de descărcare din bara de instrumente (F5). Editorul construiește proiectul, îl scrie în slotul de program inactiv al plăcii, îl verifică și abia apoi comută - o descărcare eșuată lasă neatins programul care rulează.

![Bara de instrumente: selectorul de port și butonul Download](img/install-05-download.png)

## 5. Verifică că rulează

Apasă **ONLINE** (pictograma ștecher de lângă selectorul de port) pentru a urmări programul pe placă: ce conduce este verde, fiecare variabilă își poartă valoarea live. Fără o placă la îndemână, aceeași vedere o oferă **simularea** (butonul din bara de instrumente de lângă ONLINE).

![Programul ladder în funcțiune - verde înseamnă că trece curentul](img/install-06-running.png)

Ceva nu funcționează? Vezi [Depanare](troubleshooting.ro.md).

*Capturi de ecran: editorul ctrl32 1.07.*

---

[← Hardware și cablare](hardware.ro.md) | [Prezentare](README.ro.md) | [Configurare →](configure.ro.md)
