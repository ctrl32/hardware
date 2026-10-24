---
title: Nastavenie dosky Raspberry Pi 4 Model B v editore ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Stránka dosky Raspberry Pi 4 Model B v editore
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
---

# Nastavenie dosky

## Stránka dosky

Dvojklikni na dosku v strome zariadení. Stránka ukáže, čo doska má, a každý pin: voľný pin dostane premennú jedným klikom - vstup, výstup alebo na analógovom pine analógový vstup.

![Stránka dosky: voľné piny a čo ktorý dokáže](img/configure-01-board.png)

## Sieť

Pi si drží sieťové nastavenia svojho operačného systému: DHCP z routera,
ak **Prepare a Linux device** nenastavil pevnú adresu. Nájdeš ho podľa
hostname alebo cez **Find devices** v editore.


## Vstupy, výstupy a premenné

Každý signál programu je **premenná**. Premenná na pine pin číta alebo ovláda; analógová premenná hovorí, čo je na ňu zapojené (napätie, 4-20 mA, termistor), a jej rozsah v jednotkách.

![Premenné príkladu all-in-one](img/configure-03-variables.png)

## Komunikácia

**Modbus TCP.** Zariadenie v sieti sa pridá pod **Ethernet → Modbus TCP master**; jeho registre sa stanú premennými.

**Modbus RTU / RS-485.** Adaptér USB-RS485 (`/dev/ttyUSB0`, smer sa prepína sám) alebo RS-485 HAT na UART Pi. ctrl32 je na ňom master alebo slave Modbus RTU, až na štyroch linkách.

**CAN.** CAN príde z CAN HAT na SPI (MCP2515, MCP251xFD) alebo z USB adaptéra CAN; runtime ho používa ako rozhranie SocketCAN (`can0`, až štyri zbernice). Prepare a Linux device pridá ovládač HAT-u; prenosová rýchlosť je daná projektom.

**MQTT.** Doska posiela vybrané premenné do brokera; v režime Home Assistant si ich broker nájde sám a premenná označená *write* sa dá odtiaľ nastaviť.

![Stránka MQTT: broker a posielané premenné](img/configure-05-mqtt.png)

## Displej

Runtime kreslí na pripojený monitor HDMI (alebo displej DSI) a projekt
naň prepočíta; príklad je nakreslený v 1280 x 720. Dotyk dotykového
monitora cez USB funguje bez ovládača. Bez monitora Pi zobrazuje svoje
obrazovky len v prehliadačoch (WEBview).

![Nastavenie HMIview: obrazovka, na ktorú projekt kreslí](img/configure-04-display.png)

## OPC UA, EtherCAT a videnie

- **OPC UA** - každá premenná projektu je uzol vlastného servera Pi
  (`opc.tcp://<adresa>:4840`, `ns=1;s=<meno>`); premennú z neho vyradíš
  jedným zaškrtnutím v zozname premenných. Nič iné sa nenastavuje.
- **EtherCAT** - master na vlastnom porte Ethernet pre servomeniče a I/O
  terminály; real-time jadro z Prepare a Linux device drží cyklus
  zbernice pod milisekundou.
- **Videnie** - USB kamera a bloky videnia (prítomnosť, meranie, kódy,
  neurónová sieť) - pozri [Vision](https://ctrl32.com/docs/vision/).

## WEBview

Doska ponúka svoju stránku operátora každému prehliadaču v sieti - otvor adresu dosky. Stránka sa kreslí v editore ako obrazovka.

![Nastavenie stránky WEBview](img/configure-06-webview.png)

---

[← Nahratie runtime](install.sk.md) | [Prehľad](README.sk.md) | [Vzorové projekty →](examples/README.sk.md)
