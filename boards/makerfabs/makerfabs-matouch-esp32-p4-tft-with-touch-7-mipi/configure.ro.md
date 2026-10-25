---
title: Configurează Makerfabs MaTouch ESP32-P4 7" în editorul ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: Pagina plăcii Makerfabs MaTouch ESP32-P4 7" în editor
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Configurează placa

## Pagina plăcii

Fă dublu clic pe placă în arborele de dispozitive. Pagina arată ce are placa și fiecare pin: un pin liber primește o variabilă dintr-un clic - o intrare, o ieșire sau, pe un pin cu capacitate analogică, o intrare analogică.

![Pagina plăcii: pinii liberi și ce poate face fiecare](img/configure-01-board.png)

## Rețea

Portul Ethernet pornește singur și își ia adresa de la routerul tău
(DHCP). Wi-Fi-ul lui ESP32-C6 se setează pe pagina **WiFi** din arborele
de dispozitive - numele rețelei și parola. O adresă fixă se setează pe
pagina plăcii, în secțiunea **Network**.


## Intrări, ieșiri și variabile

Fiecare semnal al programului este o **variabilă**. O variabilă pe un pin citește sau comandă pinul; o variabilă analogică spune ce este conectat la ea (o tensiune, 4-20 mA, un termistor) și domeniul ei în unități.

![Variabilele exemplului all-in-one](img/configure-03-variables.png)

## Comunicație

**Modbus TCP.** Un dispozitiv din rețea se adaugă sub **Ethernet → Modbus TCP master**; registrele lui devin variabile.

**Modbus RTU / RS-485.** Placa nu are transceiver RS-485: pune un modul transceiver de 3,3 V pe pini liberi (TX, RX și pinul de direcție DE) și numește-i pe pagina plăcii - exemplul folosește GPIO4 / GPIO5 / GPIO32. ctrl32 este atunci master sau slave Modbus RTU pe acea linie.

**CAN.** ESP32-P4 are un controler CAN (TWAI). Placa nu are transceiver CAN: pune un modul transceiver de 3,3 V pe doi pini liberi și numește-i pe pagina plăcii (**Bus pins**) - exemplul folosește GPIO20 / GPIO21. Dispozitivele CANopen, cadrele CAN brute și magistralele de vehicul (J1939) rulează toate pe el.

**MQTT.** Placa publică variabilele alese către un broker; în modul Home Assistant brokerul le găsește singur, iar o variabilă marcată *write* poate fi setată de acolo.

![Pagina MQTT: brokerul și variabilele publicate](img/configure-05-mqtt.png)

## Display și touch

Proiectul se desenează la rezoluția proprie a sticlei, 1024 x 600. Pagina
HMIview setează orientarea (cum este montată sau rotită - touch-ul o
urmează), dimensiunea suprafeței WEBview și ecranul de pornire. Touch-ul
nu are nevoie de configurare: controlerul GT911 face parte din placă.

![Setările HMIview: ecranul pe care desenează proiectul](img/configure-04-display.png)

## WEBview

Placa servește pagina operatorului oricărui browser din rețea - deschide adresa plăcii. Pagina se desenează în editor ca un ecran.

![Setările paginii WEBview](img/configure-06-webview.png)

---

[← Instalarea runtime-ului](install.ro.md) | [Prezentare](README.ro.md) | [Proiecte exemplu →](examples/README.ro.md)
