---
title: 'Olimex ESP32-DevKit-LiPo: riešenie problémov'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-DevKit-LiPo
tags:
- esp32
- wifi
- battery
- olimex
- troubleshooting
---

# Riešenie problémov

| Prejav | Príčina | Riešenie |
|---|---|---|
| COM port sa neobjaví, výber portu ostane prázdny | Kábel len napája, alebo chýba ovládač USB | Použi dátový kábel; nainštaluj ovládač USB čipu dosky; skús iný port USB. |
| Flash runtime sa zastaví pri pripájaní | Port drží iný program | Zavri sériový monitor alebo iný nástroj, ktorý má port otvorený, a skús znova. |
| Doska sa každých pár sekúnd reštartuje | Port USB nedodá dosť prúdu | Použi napájaný USB hub alebo zdroj 5 V aspoň 1 A. |
| Doska sa nepripojí k Wi-Fi | Zlý názov siete alebo heslo, alebo sieť len na 5 GHz | Skontroluj názov a heslo na stránke WiFi; ESP32 sa pripája len do sietí 2,4 GHz. |
| Doska sa nedá nájsť podľa mena .local | Sieť blokuje mDNS (multicast) | Použi IP adresu dosky - ukáže ju zoznam klientov v routeri a Find devices v editore. |
| Výstup nič nerobí | Pin je len vstup, alebo bol zadaný zlý pin | Pozri pin na stránke dosky - piny len na vstup sú označené; presuň výstup na voľný I/O pin. |
| Hodnota Modbus ostáva 0 | Zlá adresa zariadenia, unit alebo register | Skontroluj IP a unit zariadenia v strome zariadení a register v manuáli zariadenia. |

Panel **Messages** v editore a **diagnostický buffer** dosky (Online → Diagnostics) hovoria, čo runtime rozhodol a prečo - prečítaj ich ako prvé.

---

[← Vzorové projekty](examples/README.sk.md) | [Prehľad](README.sk.md)
