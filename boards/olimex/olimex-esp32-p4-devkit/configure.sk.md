---
title: Nastavenie dosky Olimex ESP32-P4-DevKit v editore ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Stránka dosky Olimex ESP32-P4-DevKit v editore
tags:
- esp32-p4
- ethernet
- olimex
---

# Nastavenie dosky

## Stránka dosky

Dvojklikni na dosku v strome zariadení. Stránka ukáže, čo doska má, a každý pin: voľný pin dostane premennú jedným klikom - vstup, výstup alebo na analógovom pine analógový vstup.

![Stránka dosky: voľné piny a čo ktorý dokáže](img/configure-01-board.png)

## Sieť

Port Ethernet sa spustí sám a adresu si vezme z routera (DHCP). Pevnú
adresu nastavíš na stránke dosky v sekcii **Network**. Doska nemá Wi-Fi.


## Vstupy, výstupy a premenné

Každý signál programu je **premenná**. Premenná na pine pin číta alebo ovláda; analógová premenná hovorí, čo je na ňu zapojené (napätie, 4-20 mA, termistor), a jej rozsah v jednotkách.

![Premenné príkladu all-in-one](img/configure-03-variables.png)

## Komunikácia

**Modbus TCP.** Zariadenie v sieti sa pridá pod **Ethernet → Modbus TCP master**; jeho registre sa stanú premennými.

**Modbus RTU / RS-485.** Doska nemá prevodník RS-485: daj 3,3 V modul prevodníka na voľné piny (TX, RX a smerový pin DE) a urči ich na stránke dosky (Bus pins) - ctrl32 je potom na tej linke Modbus RTU master alebo slave. Zariadenia Modbus TCP v sieti nepotrebujú nič.

**CAN.** ESP32-P4 má jeden radič CAN (TWAI). Doska nemá prevodník CAN: daj 3,3 V modul prevodníka na dva voľné piny a urči ich na stránke dosky (Bus pins) - potom na ňom bežia zariadenia CANopen, surové rámce CAN aj zbernice vozidiel (J1939).

**MQTT.** Doska posiela vybrané premenné do brokera; v režime Home Assistant si ich broker nájde sám a premenná označená *write* sa dá odtiaľ nastaviť.

![Stránka MQTT: broker a posielané premenné](img/configure-05-mqtt.png)

## WEBview

Doska ponúka svoju stránku operátora každému prehliadaču v sieti - otvor adresu dosky. Stránka sa kreslí v editore ako obrazovka.

![Nastavenie stránky WEBview](img/configure-06-webview.png)

---

[← Nahratie runtime](install.sk.md) | [Prehľad](README.sk.md) | [Vzorové projekty →](examples/README.sk.md)
