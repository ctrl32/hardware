---
title: A(z) Makerfabs MaTouch ESP32-P4 7" beállítása a ctrl32 szerkesztőben
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: A(z) Makerfabs MaTouch ESP32-P4 7" panel oldala a szerkesztőben
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# A panel beállítása

## A panel oldala

Kattints duplán a panelre az eszközfában. Az oldal megmutatja, mi van a panelen, és minden lábat: egy szabad láb egy kattintással kap változót - bemenetet, kimenetet, vagy analógképes lábon analóg bemenetet.

![A panel oldala: a szabad lábak, és mire képes mindegyik](img/configure-01-board.png)

## Hálózat

Az Ethernet port magától elindul, és a routertől kap címet (DHCP). Az
ESP32-C6 Wi-Fi-jét az eszközfa **WiFi** oldalán állítod be - a hálózat
nevét és a jelszót. Fix címet a panel oldalának **Network** szakaszában
adhatsz meg.


## Bemenetek, kimenetek és változók

A program minden jele egy **változó**. Egy lábhoz rendelt változó olvassa vagy vezérli a lábat; egy analóg változó megmondja, mi van rákötve (feszültség, 4-20 mA, termisztor), és mi a tartománya mértékegységben.

![Az all-in-one példa változói](img/configure-03-variables.png)

## Kommunikáció

**Modbus TCP.** A hálózat egy eszközét az **Ethernet → Modbus TCP master** alatt adod hozzá; a regiszterei változókká válnak.

**Modbus RTU / RS-485.** A panelen nincs RS-485 adó-vevő: tegyél egy 3,3 V-os adó-vevő modult szabad lábakra (TX, RX és a DE irányláb), és add meg őket a panel oldalán - a példa a GPIO4 / GPIO5 / GPIO32 lábakat használja. A ctrl32 ezután Modbus RTU master vagy slave azon a vonalon.

**CAN.** Az ESP32-P4-nek egy CAN vezérlője van (TWAI). A panelen nincs CAN adó-vevő: tegyél egy 3,3 V-os adó-vevő modult két szabad lábra, és add meg őket a panel oldalán (**Bus pins**) - a példa a GPIO20 / GPIO21 lábat használja. CANopen eszközök, nyers CAN keretek és a járműbuszok (J1939) mind futnak rajta.

**MQTT.** A panel a kiválasztott változókat egy brókernek teszi közzé; Home Assistant módban a bróker magától megtalálja őket, és egy *write* jelölésű változó onnan is beállítható.

![Az MQTT oldal: a bróker és a közzétett változók](img/configure-05-mqtt.png)

## Kijelző és érintés

A projekt a kijelző saját 1024 x 600-as felbontásában készül. A HMIview
oldal állítja be a tájolást (a beépítés szerint vagy elforgatva - az
érintés követi), a WEBview vászon méretét és az indítóképet. Az érintést
nem kell beállítani: a GT911 vezérlő a panel része.

![A HMIview beállításai: a képernyő, amelyre a projekt rajzol](img/configure-04-display.png)

## WEBview

A panel a kezelőoldalát a hálózat bármely böngészőjének kiszolgálja - nyisd meg a panel címét. Az oldalt a szerkesztőben úgy rajzolod meg, mint egy képernyőt.

![A WEBview oldal beállításai](img/configure-06-webview.png)

---

[← A runtime telepítése](install.hu.md) | [Áttekintés](README.hu.md) | [Példaprojektek →](examples/README.hu.md)
