---
title: Configurează Olimex ESP32-DevKit-LiPo în editorul ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Pagina plăcii Olimex ESP32-DevKit-LiPo în editor
tags:
- esp32
- wifi
- battery
- olimex
---

# Configurează placa

## Pagina plăcii

Fă dublu clic pe placă în arborele de dispozitive. Pagina arată ce are placa și fiecare pin: un pin liber primește o variabilă dintr-un clic - o intrare, o ieșire sau, pe un pin cu capacitate analogică, o intrare analogică.

![Pagina plăcii: pinii liberi și ce poate face fiecare](img/configure-01-board.png)

## Rețea

Placa se conectează la Wi-Fi-ul tău: deschide pagina **WiFi** din arborele
de dispozitive și introdu numele și parola rețelei (exemplul are valori de
substituție). Își ia adresa de la router (DHCP); o adresă fixă se setează
pe pagina plăcii, în secțiunea **Network**.


## Intrări, ieșiri și variabile

Fiecare semnal al programului este o **variabilă**. O variabilă pe un pin citește sau comandă pinul; o variabilă analogică spune ce este conectat la ea (o tensiune, 4-20 mA, un termistor) și domeniul ei în unități.

![Variabilele exemplului all-in-one](img/configure-03-variables.png)

## Comunicație

**Modbus TCP.** Un dispozitiv din rețea se adaugă sub **Ethernet → Modbus TCP master**; registrele lui devin variabile.

**Modbus RTU / RS-485.** Placa nu are transceiver RS-485: pune un modul transceiver de 3,3 V pe pini liberi (TX, RX și pinul de direcție DE) și numește-i pe pagina plăcii (Bus pins) - ctrl32 este atunci master sau slave Modbus RTU pe acea linie. Dispozitivele Modbus TCP din rețea nu au nevoie de nimic.

**CAN.** ESP32 are un controler CAN (TWAI). Placa nu are transceiver CAN: pune un modul transceiver de 3,3 V pe doi pini liberi și numește-i pe pagina plăcii (Bus pins) - dispozitivele CANopen, cadrele CAN brute și magistralele de vehicul (J1939) rulează apoi pe el.

**MQTT.** Placa publică variabilele alese către un broker; în modul Home Assistant brokerul le găsește singur, iar o variabilă marcată *write* poate fi setată de acolo.

![Pagina MQTT: brokerul și variabilele publicate](img/configure-05-mqtt.png)

## WEBview

Placa servește pagina operatorului oricărui browser din rețea - deschide adresa plăcii. Pagina se desenează în editor ca un ecran.

![Setările paginii WEBview](img/configure-06-webview.png)

---

[← Instalarea runtime-ului](install.ro.md) | [Prezentare](README.ro.md) | [Proiecte exemplu →](examples/README.ro.md)
