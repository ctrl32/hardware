---
title: 'Olimex ESP32-PoE: exemplul All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/screen.png
image_alt: Pagina operatorului din exemplul all-in-one pentru Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- example
---

# All-in-one

O pompă comandată de butonul plăcii, de pagina operatorului și din Home Assistant, cu o intrare de nivel, un temporizator de funcționare, o alarmă de nivel și un contor de energie Modbus TCP.

**Descărcare:** [all-in-one.prj32](all-in-one.prj32) - deschide-l în editorul ctrl32 (**File → Open**).

## Ce face

Programul este un mic controler de pompă - forma majorității
mașinilor:

- **Start** vine de la butonul plăcii (BUT1), de la butonul **Start**
  de pe pagina operatorului sau din Home Assistant prin MQTT.
- **Stop** vine de la butonul **Stop**, de la un nivel scăzut sau de la
  expirarea timpului de funcționare - automenținerea (latch) oprește
  ieșirea de pe GPIO33.
- **Nivelul** este o intrare analogică pe GPIO35 (0 la 3,3 V scalat la
  0 la 100 %). Sub 10 % pompa se oprește și se declanșează o alarmă;
  peste 15 % poate porni din nou (histerezis).
- **Timpul de funcționare** se setează pe pagină în minute și se
  păstrează la o pană de curent (o variabilă remanentă).
- Un contor de energie **Modbus TCP** din rețea dă tensiunea rețelei
  (registrul 0, registre de intrare, unit 1 la 192.168.1.60 - schimbă-l
  cu contorul tău). Peste 253 V se declanșează o alarmă.
- **CAN** (un transceiver pe GPIO4 / GPIO36) trimite nivelul și starea
  pompei în cadrul 0x181 la fiecare 100 ms și primește o valoare de
  referință în 0x201.
- **MQTT** publică nivelul, starea pompei și tensiunea către un broker
  Home Assistant, care le găsește singur (discovery); pompa poate fi
  pornită din Home Assistant.
- **WEBview** servește pagina operatorului - pompa, nivelul, trendul
  lui și alarmele - oricărui browser din rețea.

## Programul

![Programul ladder al exemplului](img/ladder.png)

## Pagina operatorului

![Pagina operatorului rulând în simulare](img/screen.png)

## Deschide-l și rulează-l

1. Deschide `all-in-one.prj32` în editor.
2. Schimbă adresele (dispozitivul Modbus, brokerul MQTT) cu cele ale rețelei tale.
3. Pornește **simularea** (bara de instrumente) pentru a-l încerca pe PC sau descarcă-l pe placă - vezi [Instalarea runtime-ului](../../install.ro.md).

## Ce ar trebui să vezi

Cu potențiometrul rotit în sus, apasă BUT1: releul de pe GPIO33 se
activează și LED-ul pompei de pe pagină se aprinde. Rotește
potențiometrul sub 10 %: pompa se oprește și alarma apare în tabel. În
Home Assistant placa apare cu nivelul, pompa și tensiunea.


---

[← Proiecte exemplu](../README.ro.md) | [Prezentare](../../README.ro.md)
