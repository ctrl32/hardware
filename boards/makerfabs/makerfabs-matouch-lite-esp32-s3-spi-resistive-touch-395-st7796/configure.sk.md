---
title: Nastavenie dosky Makerfabs MaTouch Lite ESP32-S3 3.95" v editore ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Stránka dosky Makerfabs MaTouch Lite ESP32-S3 3.95" v editore
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Nastavenie dosky

## Stránka dosky

Dvojklikni na dosku v strome zariadení. Stránka ukáže, čo doska má, a každý pin: voľný pin dostane premennú jedným klikom - vstup, výstup alebo na analógovom pine analógový vstup.

![Stránka dosky: voľné piny a čo ktorý dokáže](img/configure-01-board.png)

## Sieť

Doska sa pripojí k tvojej Wi-Fi: v strome zariadení otvor stránku **WiFi**
a zadaj meno a heslo siete (príklad nesie zástupné hodnoty). Pevnú adresu
nastavíš na stránke dosky v sekcii **Network**.


## Vstupy, výstupy a premenné

Každý signál programu je **premenná**. Premenná na pine pin číta alebo ovláda; analógová premenná hovorí, čo je na ňu zapojené (napätie, 4-20 mA, termistor), a jej rozsah v jednotkách.

![Premenné príkladu all-in-one](img/configure-03-variables.png)

## Komunikácia

**Modbus TCP.** Zariadenie v sieti sa pridá pod **Ethernet → Modbus TCP master**; jeho registre sa stanú premennými.

**Modbus RTU / RS-485.** Doska nemá prevodník RS-485 a popri I/O príkladu má na neho príliš málo voľných pinov; zariadenia Modbus sa dosiahnu cez Modbus TCP na Wi-Fi.

**CAN.** ESP32-S3 má jeden radič CAN (TWAI). Doska nemá prevodník: daj 3,3 V modul prevodníka na dva voľné piny a pomenuj ich na stránke dosky (**Bus pins**); príklad používa GPIO6 / GPIO7.

**MQTT.** Doska posiela vybrané premenné do brokera; v režime Home Assistant si ich broker nájde sám a premenná označená *write* sa dá odtiaľ nastaviť.

![Stránka MQTT: broker a posielané premenné](img/configure-05-mqtt.png)

## Displej a dotyk

Sklo má 320 x 480, na výšku tak, ako je namontované; stránka HMIview otočí
obraz (dotyk ho nasleduje) a nastaví úvodnú obrazovku pri štarte. Odporový
dotyk potrebuje pevné stlačenie - tlačidlá kresli aspoň 40 px vysoké.

![Nastavenie HMIview: obrazovka, na ktorú projekt kreslí](img/configure-04-display.png)

## WEBview

Doska ponúka svoju stránku operátora každému prehliadaču v sieti - otvor adresu dosky. Stránka sa kreslí v editore ako obrazovka.

![Nastavenie stránky WEBview](img/configure-06-webview.png)

---

[← Nahratie runtime](install.sk.md) | [Prehľad](README.sk.md) | [Vzorové projekty →](examples/README.sk.md)
