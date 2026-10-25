---
title: Nastavení desky Makerfabs MaTouch Lite ESP32-S3 3.95" v editoru ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Stránka desky Makerfabs MaTouch Lite ESP32-S3 3.95" v editoru
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Nastavení desky

## Stránka desky

Dvakrát klikni na desku ve stromu zařízení. Stránka ukáže, co deska nese, a každý pin: volný pin dostane proměnnou jedním kliknutím - vstup, výstup, nebo na analogovém pinu analogový vstup.

![Stránka desky: volné piny a co který umí](img/configure-01-board.png)

## Síť

Deska se připojí k tvé Wi-Fi: ve stromu zařízení otevři stránku **WiFi**
a zadej jméno a heslo sítě (příklad nese zástupné hodnoty). Pevnou adresu
nastavíš na stránce desky v sekci **Network**.


## Vstupy, výstupy a proměnné

Každý signál programu je **proměnná**. Proměnná na pinu pin čte nebo ovládá; analogová proměnná říká, co je na ni zapojeno (napětí, 4-20 mA, termistor), a její rozsah v jednotkách.

![Proměnné příkladu all-in-one](img/configure-03-variables.png)

## Komunikace

**Modbus TCP.** Zařízení v síti se přidá pod **Ethernet → Modbus TCP master**; jeho registry se stanou proměnnými.

**Modbus RTU / RS-485.** Deska nemá převodník RS-485 a vedle I/O příkladu na něj zbývá příliš málo volných pinů; k zařízením Modbus se dostaneš přes Modbus TCP na Wi-Fi.

**CAN.** ESP32-S3 má jeden řadič CAN (TWAI). Deska nemá převodník: dej 3,3 V modul převodníku na dva volné piny a pojmenuj je na stránce desky (**Bus pins**); příklad používá GPIO6 / GPIO7.

**MQTT.** Deska posílá vybrané proměnné do brokeru; v režimu Home Assistant si je broker najde sám a proměnnou označenou *write* lze odtud nastavit.

![Stránka MQTT: broker a odesílané proměnné](img/configure-05-mqtt.png)

## Displej a dotyk

Sklo má 320 x 480, na výšku tak, jak je namontované; stránka HMIview otočí
obraz (dotyk ho následuje) a nastaví úvodní obrazovku při startu. Odporový
dotyk potřebuje pevný stisk - tlačítka kresli aspoň 40 px vysoká.

![Nastavení HMIview: obrazovka, na kterou projekt kreslí](img/configure-04-display.png)

## WEBview

Deska nabízí svou stránku operátora každému prohlížeči v síti - otevři adresu desky. Stránka se kreslí v editoru jako obrazovka.

![Nastavení stránky WEBview](img/configure-06-webview.png)

---

[← Nahrání runtime](install.cs.md) | [Přehled](README.cs.md) | [Vzorové projekty →](examples/README.cs.md)
