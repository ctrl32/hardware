---
title: Configurează Olimex ESP32-P4-PC în editorul ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Pagina plăcii Olimex ESP32-P4-PC în editor
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Configurează placa

## Pagina plăcii

Fă dublu clic pe placă în arborele de dispozitive. Pagina arată ce are placa și fiecare pin: un pin liber primește o variabilă dintr-un clic - o intrare, o ieșire sau, pe un pin cu capacitate analogică, o intrare analogică.

![Pagina plăcii: pinii liberi și ce poate face fiecare](img/configure-01-board.png)

## Rețea

Portul Ethernet pornește singur și își ia adresa de la routerul tău
(DHCP). O adresă fixă se setează pe pagina plăcii, în secțiunea
**Network**. Placa nu are Wi-Fi.


## Intrări, ieșiri și variabile

Fiecare semnal al programului este o **variabilă**. O variabilă pe un pin citește sau comandă pinul; o variabilă analogică spune ce este conectat la ea (o tensiune, 4-20 mA, un termistor) și domeniul ei în unități.

![Variabilele exemplului all-in-one](img/configure-03-variables.png)

## Comunicație

**Modbus TCP.** Un dispozitiv din rețea se adaugă sub **Ethernet → Modbus TCP master**; registrele lui devin variabile.

**Modbus RTU / RS-485.** Placa nu are transceiver RS-485: pune un modul transceiver de 3,3 V pe pini EXT1 liberi (TX, RX și pinul de direcție DE) și numește-i pe pagina plăcii - ctrl32 este atunci master sau slave Modbus RTU pe acea linie.

**CAN.** ESP32-P4 are un controler CAN (TWAI). Placa nu are transceiver: pune un modul transceiver CAN de 3,3 V pe doi pini EXT1 liberi și numește-i pe pagina plăcii (**Bus pins**).

**MQTT.** Placa publică variabilele alese către un broker; în modul Home Assistant brokerul le găsește singur, iar o variabilă marcată *write* poate fi setată de acolo.

![Pagina MQTT: brokerul și variabilele publicate](img/configure-05-mqtt.png)

## WEBview

Placa servește pagina operatorului oricărui browser din rețea - deschide adresa plăcii. Pagina se desenează în editor ca un ecran.

![Setările paginii WEBview](img/configure-06-webview.png)

---

[← Instalarea runtime-ului](install.ro.md) | [Prezentare](README.ro.md) | [Proiecte exemplu →](examples/README.ro.md)
