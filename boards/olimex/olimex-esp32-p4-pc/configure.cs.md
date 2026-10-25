---
title: Nastavení desky Olimex ESP32-P4-PC v editoru ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Stránka desky Olimex ESP32-P4-PC v editoru
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Nastavení desky

## Stránka desky

Dvakrát klikni na desku ve stromu zařízení. Stránka ukáže, co deska nese, a každý pin: volný pin dostane proměnnou jedním kliknutím - vstup, výstup, nebo na analogovém pinu analogový vstup.

![Stránka desky: volné piny a co který umí](img/configure-01-board.png)

## Síť

Port Ethernet naběhne sám a adresu si vezme z routeru (DHCP). Pevnou adresu
nastavíš na stránce desky v sekci **Network**. Deska nemá Wi-Fi.


## Vstupy, výstupy a proměnné

Každý signál programu je **proměnná**. Proměnná na pinu pin čte nebo ovládá; analogová proměnná říká, co je na ni zapojeno (napětí, 4-20 mA, termistor), a její rozsah v jednotkách.

![Proměnné příkladu all-in-one](img/configure-03-variables.png)

## Komunikace

**Modbus TCP.** Zařízení v síti se přidá pod **Ethernet → Modbus TCP master**; jeho registry se stanou proměnnými.

**Modbus RTU / RS-485.** Deska nemá převodník RS-485: dej 3,3 V modul převodníku na volné piny EXT1 (TX, RX a směrový pin DE) a pojmenuj je na stránce desky - ctrl32 je pak na té lince Modbus RTU master nebo slave.

**CAN.** ESP32-P4 má jeden řadič CAN (TWAI). Deska nemá převodník: dej 3,3 V modul převodníku CAN na dva volné piny EXT1 a pojmenuj je na stránce desky (**Bus pins**).

**MQTT.** Deska posílá vybrané proměnné do brokeru; v režimu Home Assistant si je broker najde sám a proměnnou označenou *write* lze odtud nastavit.

![Stránka MQTT: broker a odesílané proměnné](img/configure-05-mqtt.png)

## WEBview

Deska nabízí svou stránku operátora každému prohlížeči v síti - otevři adresu desky. Stránka se kreslí v editoru jako obrazovka.

![Nastavení stránky WEBview](img/configure-06-webview.png)

---

[← Nahrání runtime](install.cs.md) | [Přehled](README.cs.md) | [Vzorové projekty →](examples/README.cs.md)
