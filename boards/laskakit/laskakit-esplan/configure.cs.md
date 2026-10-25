---
title: Nastavení desky LaskaKit ESPlan v editoru ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Stránka desky LaskaKit ESPlan v editoru
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Nastavení desky

## Stránka desky

Dvakrát klikni na desku ve stromu zařízení. Stránka ukáže, co deska nese, a každý pin: volný pin dostane proměnnou jedním kliknutím - vstup, výstup, nebo na analogovém pinu analogový vstup.

![Stránka desky: volné piny a co který umí](img/configure-01-board.png)

## Síť

Port Ethernet naběhne sám a adresu si vezme z routeru (DHCP). Pevnou adresu
nastavíš na stránce desky v sekci **Network**; Wi-Fi na stránce **WiFi**
ve stromu zařízení.


## Vstupy, výstupy a proměnné

Každý signál programu je **proměnná**. Proměnná na pinu pin čte nebo ovládá; analogová proměnná říká, co je na ni zapojeno (napětí, 4-20 mA, termistor), a její rozsah v jednotkách.

![Proměnné příkladu all-in-one](img/configure-03-variables.png)

## Komunikace

**Modbus TCP.** Zařízení v síti se přidá pod **Ethernet → Modbus TCP master**; jeho registry se stanou proměnnými.

**Modbus RTU / RS-485.** Deska má vlastní převodník RS-485 (WS3081, s ochranou). ctrl32 je Modbus RTU master - zařízení a jejich registry se přidávají ve stromu zařízení pod RS485 - nebo Modbus RTU slave, který čtou jiné mastery.

**CAN.** ESP32 má jeden řadič CAN (TWAI). Deska nemá převodník CAN: dej 3,3 V modul převodníku na dva volné piny a urči je na stránce desky (Bus pins) - pak na něm běží zařízení CANopen, surové rámce CAN i sběrnice vozidel (J1939).

**MQTT.** Deska posílá vybrané proměnné do brokeru; v režimu Home Assistant si je broker najde sám a proměnnou označenou *write* lze odtud nastavit.

![Stránka MQTT: broker a odesílané proměnné](img/configure-05-mqtt.png)

## WEBview

Deska nabízí svou stránku operátora každému prohlížeči v síti - otevři adresu desky. Stránka se kreslí v editoru jako obrazovka.

![Nastavení stránky WEBview](img/configure-06-webview.png)

---

[← Nahrání runtime](install.cs.md) | [Přehled](README.cs.md) | [Vzorové projekty →](examples/README.cs.md)
