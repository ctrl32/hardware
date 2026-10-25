---
title: A(z) Makerfabs MaTouch Lite ESP32-S3 3.95" beállítása a ctrl32 szerkesztőben
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: A(z) Makerfabs MaTouch Lite ESP32-S3 3.95" panel oldala a szerkesztőben
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# A panel beállítása

## A panel oldala

Kattints duplán a panelre az eszközfában. Az oldal megmutatja, mi van a panelen, és minden lábat: egy szabad láb egy kattintással kap változót - bemenetet, kimenetet, vagy analógképes lábon analóg bemenetet.

![A panel oldala: a szabad lábak, és mire képes mindegyik](img/configure-01-board.png)

## Hálózat

A panel a Wi-Fi-hálózatodhoz csatlakozik: nyisd meg az eszközfa **WiFi**
oldalát, és írd be a hálózat nevét és jelszavát (a példában helyőrzők
vannak). Fix címet a panel oldalának **Network** szakaszában adhatsz meg.


## Bemenetek, kimenetek és változók

A program minden jele egy **változó**. Egy lábhoz rendelt változó olvassa vagy vezérli a lábat; egy analóg változó megmondja, mi van rákötve (feszültség, 4-20 mA, termisztor), és mi a tartománya mértékegységben.

![Az all-in-one példa változói](img/configure-03-variables.png)

## Kommunikáció

**Modbus TCP.** A hálózat egy eszközét az **Ethernet → Modbus TCP master** alatt adod hozzá; a regiszterei változókká válnak.

**Modbus RTU / RS-485.** A panelen nincs RS-485 adó-vevő, és a példa I/O-ja mellett túl kevés a szabad láb egyhez; a Modbus eszközök Modbus TCP-n, a Wi-Fi-n keresztül érhetők el.

**CAN.** Az ESP32-S3-nak egy CAN vezérlője van (TWAI). A panelen nincs adó-vevő: tegyél egy 3,3 V-os adó-vevő modult két szabad lábra, és add meg őket a panel oldalán (**Bus pins**); a példa a GPIO6 / GPIO7 lábat használja.

**MQTT.** A panel a kiválasztott változókat egy brókernek teszi közzé; Home Assistant módban a bróker magától megtalálja őket, és egy *write* jelölésű változó onnan is beállítható.

![Az MQTT oldal: a bróker és a közzétett változók](img/configure-05-mqtt.png)

## Kijelző és érintés

A kijelző 320 x 480-as, a beépítés szerint álló; a HMIview oldal
elforgatja a képet (az érintés követi), és beállítja az indítóképet. A
rezisztív érintés határozott nyomást igényel - a gombokat legalább 40 px
magasra rajzold.

![A HMIview beállításai: a képernyő, amelyre a projekt rajzol](img/configure-04-display.png)

## WEBview

A panel a kezelőoldalát a hálózat bármely böngészőjének kiszolgálja - nyisd meg a panel címét. Az oldalt a szerkesztőben úgy rajzolod meg, mint egy képernyőt.

![A WEBview oldal beállításai](img/configure-06-webview.png)

---

[← A runtime telepítése](install.hu.md) | [Áttekintés](README.hu.md) | [Példaprojektek →](examples/README.hu.md)
