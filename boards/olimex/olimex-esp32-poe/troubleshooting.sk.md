---
title: 'Olimex ESP32-PoE: riešenie problémov'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- troubleshooting
---

# Riešenie problémov

| Prejav | Príčina | Riešenie |
|---|---|---|
| COM port sa neobjaví, výber portu ostane prázdny | Kábel len napája, alebo chýba ovládač CH340 | Použi dátový kábel; nainštaluj ovládač CH340 (WCH CH341SER); skús iný port USB. |
| Flash runtime sa zastaví pri pripájaní | Port drží iný program | Zavri sériový monitor alebo iný nástroj, ktorý má port otvorený, a skús znova. |
| Doska sa každých pár sekúnd reštartuje | Port USB nedodá prúd, keď štartuje Ethernet | Použi napájaný USB hub alebo zdroj 5 V aspoň 1 A, alebo dosku napájaj cez PoE (bez USB). |
| Sieť nenabehne | Žiadny DHCP server, alebo port nemá linku | Pozri LED linky na konektore; nastav pevnú adresu na stránke dosky; skús iný port switchu. |
| Doska sa nedá nájsť podľa mena .local | Sieť blokuje mDNS (multicast) | Použi IP adresu dosky - ukáže ju zoznam klientov v routeri a Find devices v editore. |
| USB sa odpojí alebo PC hlási chybu, keď sa zapojí kábel PoE | USB a PoE zapojené naraz na doske, ktorá nie je oddelená | Okamžite jedno odpoj. Najprv nahraj cez USB, potom prevádzkuj na PoE - alebo použi ESP32-PoE-ISO. |
| Výstup na GPIO34 až GPIO39 nič nerobí | Tieto piny sú len vstupy | Presuň výstup na GPIO33, GPIO4 alebo GPIO5. |
| Hodnota Modbus ostáva 0 | Zlá adresa zariadenia, unit alebo register, alebo je zariadenie v inej podsieti | Skontroluj IP a unit zariadenia v strome zariadení a register v manuáli zariadenia; pingni zariadenie z PC. |

Panel **Messages** v editore a **diagnostický buffer** dosky (Online → Diagnostics) hovoria, čo runtime rozhodol a prečo - prečítaj ich ako prvé.

---

[← Vzorové projekty](examples/README.sk.md) | [Prehľad](README.sk.md)
