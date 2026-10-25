---
title: Configurează Raspberry Pi 3 Model B+ în editorul ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Pagina plăcii Raspberry Pi 3 Model B+ în editor
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Configurează placa

## Pagina plăcii

Fă dublu clic pe placă în arborele de dispozitive. Pagina arată ce are placa și fiecare pin: un pin liber primește o variabilă dintr-un clic - o intrare, o ieșire sau, pe un pin cu capacitate analogică, o intrare analogică.

![Pagina plăcii: pinii liberi și ce poate face fiecare](img/configure-01-board.png)

## Rețea

Pi-ul păstrează setările de rețea ale sistemului său de operare: DHCP de
la router, dacă **Prepare a Linux device** nu a setat o adresă fixă. Îl
găsești după hostname sau cu **Find devices** din editor.


## Intrări, ieșiri și variabile

Fiecare semnal al programului este o **variabilă**. O variabilă pe un pin citește sau comandă pinul; o variabilă analogică spune ce este conectat la ea (o tensiune, 4-20 mA, un termistor) și domeniul ei în unități.

![Variabilele exemplului all-in-one](img/configure-03-variables.png)

## Comunicație

**Modbus TCP.** Un dispozitiv din rețea se adaugă sub **Ethernet → Modbus TCP master**; registrele lui devin variabile.

**Modbus RTU / RS-485.** Un adaptor USB-RS485 (`/dev/ttyUSB0`, direcția se comută singură) sau un HAT RS-485 pe UART-ul Pi-ului. ctrl32 este master sau slave Modbus RTU pe el, pe până la patru linii.

**CAN.** CAN vine de la un HAT CAN pe SPI (MCP2515, MCP251xFD) sau de la un adaptor CAN USB; runtime-ul îl folosește ca interfață SocketCAN (`can0`, până la patru magistrale). Prepare a Linux device adaugă driverul HAT-ului; rata de biți este cea a proiectului.

**MQTT.** Placa publică variabilele alese către un broker; în modul Home Assistant brokerul le găsește singur, iar o variabilă marcată *write* poate fi setată de acolo.

![Pagina MQTT: brokerul și variabilele publicate](img/configure-05-mqtt.png)

## Display

Runtime-ul desenează pe monitorul HDMI conectat (sau pe un display DSI) și
scalează proiectul la el; exemplul este desenat la 1280 x 720. Touch-ul
USB al unui monitor tactil funcționează fără driver. Fără monitor, Pi-ul
își servește ecranele doar browserelor (WEBview).

![Setările HMIview: ecranul pe care desenează proiectul](img/configure-04-display.png)

## OPC UA și EtherCAT

- **OPC UA** - fiecare variabilă a proiectului este un nod al serverului
  propriu al Pi-ului (`opc.tcp://<adresă>:4840`, `ns=1;s=<nume>`); o
  variabilă poate fi ținută în afara lui cu o bifă în lista de variabile.
  Altceva nu se setează.
- **EtherCAT** - un master pe un adaptor Ethernet USB pentru terminale
  I/O; pentru servoacționări cu un ciclu de magistrală scurt, un
  Raspberry Pi 4 sau 5 este alegerea mai bună.

## WEBview

Placa servește pagina operatorului oricărui browser din rețea - deschide adresa plăcii. Pagina se desenează în editor ca un ecran.

![Setările paginii WEBview](img/configure-06-webview.png)

---

[← Instalarea runtime-ului](install.ro.md) | [Prezentare](README.ro.md) | [Proiecte exemplu →](examples/README.ro.md)
