---
title: Nastavení desky Raspberry Pi 3 Model B+ v editoru ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Stránka desky Raspberry Pi 3 Model B+ v editoru
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Nastavení desky

## Stránka desky

Dvakrát klikni na desku ve stromu zařízení. Stránka ukáže, co deska nese, a každý pin: volný pin dostane proměnnou jedním kliknutím - vstup, výstup, nebo na analogovém pinu analogový vstup.

![Stránka desky: volné piny a co který umí](img/configure-01-board.png)

## Síť

Pi si drží síťové nastavení svého operačního systému: DHCP z routeru,
pokud **Prepare a Linux device** nenastavil pevnou adresu. Najdeš ho
podle hostname nebo přes **Find devices** v editoru.


## Vstupy, výstupy a proměnné

Každý signál programu je **proměnná**. Proměnná na pinu pin čte nebo ovládá; analogová proměnná říká, co je na ni zapojeno (napětí, 4-20 mA, termistor), a její rozsah v jednotkách.

![Proměnné příkladu all-in-one](img/configure-03-variables.png)

## Komunikace

**Modbus TCP.** Zařízení v síti se přidá pod **Ethernet → Modbus TCP master**; jeho registry se stanou proměnnými.

**Modbus RTU / RS-485.** Adaptér USB-RS485 (`/dev/ttyUSB0`, směr se přepíná sám) nebo RS-485 HAT na UART Pi. ctrl32 je na něm master nebo slave Modbus RTU, až na čtyřech linkách.

**CAN.** CAN přijde z CAN HAT na SPI (MCP2515, MCP251xFD) nebo z USB adaptéru CAN; runtime ho používá jako rozhraní SocketCAN (`can0`, až čtyři sběrnice). Prepare a Linux device přidá ovladač HATu; přenosová rychlost je daná projektem.

**MQTT.** Deska posílá vybrané proměnné do brokeru; v režimu Home Assistant si je broker najde sám a proměnnou označenou *write* lze odtud nastavit.

![Stránka MQTT: broker a odesílané proměnné](img/configure-05-mqtt.png)

## Displej

Runtime kreslí na připojený monitor HDMI (nebo displej DSI) a projekt
na něj přepočítá; příklad je nakreslený v 1280 x 720. Dotyk dotykového
monitoru přes USB funguje bez ovladače. Bez monitoru Pi zobrazuje své
obrazovky jen v prohlížečích (WEBview).

![Nastavení HMIview: obrazovka, na kterou projekt kreslí](img/configure-04-display.png)

## OPC UA a EtherCAT

- **OPC UA** - každá proměnná projektu je uzel vlastního serveru Pi
  (`opc.tcp://<adresa>:4840`, `ns=1;s=<jméno>`); proměnnou z něj vyřadíš
  jedním zaškrtnutím v seznamu proměnných. Nic jiného se nenastavuje.
- **EtherCAT** - master na USB adaptéru Ethernet pro I/O terminály; pro
  servoměniče s krátkým cyklem sběrnice je lepší volbou Raspberry Pi 4
  nebo 5.

## WEBview

Deska nabízí svou stránku operátora každému prohlížeči v síti - otevři adresu desky. Stránka se kreslí v editoru jako obrazovka.

![Nastavení stránky WEBview](img/configure-06-webview.png)

---

[← Nahrání runtime](install.cs.md) | [Přehled](README.cs.md) | [Vzorové projekty →](examples/README.cs.md)
