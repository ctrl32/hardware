---
title: Nastavení desky Makerfabs MaTouch ESP32-P4 7" v editoru ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Stránka desky Makerfabs MaTouch ESP32-P4 7" v editoru
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Nastavení desky

## Stránka desky

Dvakrát klikni na desku ve stromu zařízení. Stránka ukáže, co deska nese, a každý pin: volný pin dostane proměnnou jedním kliknutím - vstup, výstup, nebo na analogovém pinu analogový vstup.

![Stránka desky: volné piny a co který umí](img/configure-01-board.png)

## Síť

Port Ethernet se spustí sám a adresu si vezme z routeru (DHCP). Wi-Fi
čipu ESP32-C6 se nastavuje na stránce **WiFi** ve stromu zařízení - jméno
sítě a heslo. Pevnou adresu nastavíš na stránce desky v sekci
**Network**.


## Vstupy, výstupy a proměnné

Každý signál programu je **proměnná**. Proměnná na pinu pin čte nebo ovládá; analogová proměnná říká, co je na ni zapojeno (napětí, 4-20 mA, termistor), a její rozsah v jednotkách.

![Proměnné příkladu all-in-one](img/configure-03-variables.png)

## Komunikace

**Modbus TCP.** Zařízení v síti se přidá pod **Ethernet → Modbus TCP master**; jeho registry se stanou proměnnými.

**Modbus RTU / RS-485.** Deska nemá převodník RS-485: dej 3,3V modul převodníku na volné piny (TX, RX a směrový pin DE) a pojmenuj je na stránce desky - příklad používá GPIO4 / GPIO5 / GPIO32. ctrl32 je pak na této lince master nebo slave Modbus RTU.

**CAN.** ESP32-P4 má jeden řadič CAN (TWAI). Deska nemá převodník CAN: dej 3,3V modul převodníku na dva volné piny a pojmenuj je na stránce desky (Bus pins) - příklad používá GPIO20 / GPIO21. Běží na něm zařízení CANopen, surové rámce CAN i vozidlové sběrnice (J1939).

**MQTT.** Deska posílá vybrané proměnné do brokeru; v režimu Home Assistant si je broker najde sám a proměnnou označenou *write* lze odtud nastavit.

![Stránka MQTT: broker a odesílané proměnné](img/configure-05-mqtt.png)

## Displej a dotyk

Projekt se kreslí ve vlastním rozlišení skla 1024 x 600. Stránka HMIview
nastavuje orientaci (jak je deska namontovaná, nebo otočeně - dotyk se
přizpůsobí), velikost plátna WEBview a úvodní obrazovku. Dotyk není třeba
nastavovat: řadič GT911 je součástí desky.

![Nastavení HMIview: obrazovka, na kterou projekt kreslí](img/configure-04-display.png)

## WEBview

Deska nabízí svou stránku operátora každému prohlížeči v síti - otevři adresu desky. Stránka se kreslí v editoru jako obrazovka.

![Nastavení stránky WEBview](img/configure-06-webview.png)

---

[← Nahrání runtime](install.cs.md) | [Přehled](README.cs.md) | [Vzorové projekty →](examples/README.cs.md)
