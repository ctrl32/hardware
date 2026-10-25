---
title: A(z) Olimex ESP32-P4-PC beállítása a ctrl32 szerkesztőben
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: A(z) Olimex ESP32-P4-PC panel oldala a szerkesztőben
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# A panel beállítása

## A panel oldala

Kattints duplán a panelre az eszközfában. Az oldal megmutatja, mi van a panelen, és minden lábat: egy szabad láb egy kattintással kap változót - bemenetet, kimenetet, vagy analógképes lábon analóg bemenetet.

![A panel oldala: a szabad lábak, és mire képes mindegyik](img/configure-01-board.png)

## Hálózat

Az Ethernet port magától elindul, és a routertől kap címet (DHCP). Fix
címet a panel oldalának **Network** szakaszában adhatsz meg. A panelnek
nincs Wi-Fi-je.


## Bemenetek, kimenetek és változók

A program minden jele egy **változó**. Egy lábhoz rendelt változó olvassa vagy vezérli a lábat; egy analóg változó megmondja, mi van rákötve (feszültség, 4-20 mA, termisztor), és mi a tartománya mértékegységben.

![Az all-in-one példa változói](img/configure-03-variables.png)

## Kommunikáció

**Modbus TCP.** A hálózat egy eszközét az **Ethernet → Modbus TCP master** alatt adod hozzá; a regiszterei változókká válnak.

**Modbus RTU / RS-485.** A panelen nincs RS-485 adó-vevő: tegyél egy 3,3 V-os adó-vevő modult szabad EXT1 lábakra (TX, RX és a DE irányláb), és add meg őket a panel oldalán - a ctrl32 ezután Modbus RTU master vagy slave azon a vonalon.

**CAN.** Az ESP32-P4-nek egy CAN vezérlője van (TWAI). A panelen nincs adó-vevő: tegyél egy 3,3 V-os CAN adó-vevő modult két szabad EXT1 lábra, és add meg őket a panel oldalán (**Bus pins**).

**MQTT.** A panel a kiválasztott változókat egy brókernek teszi közzé; Home Assistant módban a bróker magától megtalálja őket, és egy *write* jelölésű változó onnan is beállítható.

![Az MQTT oldal: a bróker és a közzétett változók](img/configure-05-mqtt.png)

## WEBview

A panel a kezelőoldalát a hálózat bármely böngészőjének kiszolgálja - nyisd meg a panel címét. Az oldalt a szerkesztőben úgy rajzolod meg, mint egy képernyőt.

![A WEBview oldal beállításai](img/configure-06-webview.png)

---

[← A runtime telepítése](install.hu.md) | [Áttekintés](README.hu.md) | [Példaprojektek →](examples/README.hu.md)
