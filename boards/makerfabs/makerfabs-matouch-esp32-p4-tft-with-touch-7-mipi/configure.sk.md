---
title: Nastavenie dosky Makerfabs MaTouch ESP32-P4 7" v editore ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Stránka dosky Makerfabs MaTouch ESP32-P4 7" v editore
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Nastavenie dosky

## Stránka dosky

Dvojklikni na dosku v strome zariadení. Stránka ukáže, čo doska má, a každý pin: voľný pin dostane premennú jedným klikom - vstup, výstup alebo na analógovom pine analógový vstup.

![Stránka dosky: voľné piny a čo ktorý dokáže](img/configure-01-board.png)

## Sieť

Port Ethernet sa spustí sám a adresu si vezme z routera (DHCP). Wi-Fi
čipu ESP32-C6 sa nastavuje na stránke **WiFi** v strome zariadení - meno
siete a heslo. Pevnú adresu nastavíš na stránke dosky v sekcii
**Network**.


## Vstupy, výstupy a premenné

Každý signál programu je **premenná**. Premenná na pine pin číta alebo ovláda; analógová premenná hovorí, čo je na ňu zapojené (napätie, 4-20 mA, termistor), a jej rozsah v jednotkách.

![Premenné príkladu all-in-one](img/configure-03-variables.png)

## Komunikácia

**Modbus TCP.** Zariadenie v sieti sa pridá pod **Ethernet → Modbus TCP master**; jeho registre sa stanú premennými.

**Modbus RTU / RS-485.** Doska nemá prevodník RS-485: daj 3,3 V modul prevodníka na voľné piny (TX, RX a smerový pin DE) a pomenuj ich na stránke dosky - príklad používa GPIO4 / GPIO5 / GPIO32. ctrl32 je potom na tejto linke master alebo slave Modbus RTU.

**CAN.** ESP32-P4 má jeden radič CAN (TWAI). Doska nemá prevodník CAN: daj 3,3 V modul prevodníka na dva voľné piny a pomenuj ich na stránke dosky (Bus pins) - príklad používa GPIO20 / GPIO21. Bežia na ňom zariadenia CANopen, surové rámce CAN aj vozidlové zbernice (J1939).

**MQTT.** Doska posiela vybrané premenné do brokera; v režime Home Assistant si ich broker nájde sám a premenná označená *write* sa dá odtiaľ nastaviť.

![Stránka MQTT: broker a posielané premenné](img/configure-05-mqtt.png)

## Displej a dotyk

Projekt sa kreslí vo vlastnom rozlíšení skla 1024 x 600. Stránka HMIview
nastavuje orientáciu (ako je namontované, alebo otočené - dotyk sa
prispôsobí), veľkosť plátna WEBview a úvodnú obrazovku. Dotyk netreba
nastavovať: radič GT911 je súčasťou dosky.

![Nastavenie HMIview: obrazovka, na ktorú projekt kreslí](img/configure-04-display.png)

## WEBview

Doska ponúka svoju stránku operátora každému prehliadaču v sieti - otvor adresu dosky. Stránka sa kreslí v editore ako obrazovka.

![Nastavenie stránky WEBview](img/configure-06-webview.png)

---

[← Nahratie runtime](install.sk.md) | [Prehľad](README.sk.md) | [Vzorové projekty →](examples/README.sk.md)
