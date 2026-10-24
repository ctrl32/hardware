---
title: 'Makerfabs MaTouch ESP32-P4 7": riešenie problémov'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- troubleshooting
---

# Riešenie problémov

| Prejav | Príčina | Riešenie |
|---|---|---|
| COM port sa neobjaví | Kábel len napája, alebo chýba ovládač CH340 | Použi dátový kábel USB-C; nainštaluj ovládač CH340 (WCH CH341SER); skús iný port USB. |
| Doska sa reštartuje, keď sa rozsvieti obrazovka | Zdroj neutiahne podsvietenie | Použi zdroj 5 V / 2 A alebo napájaný USB hub. |
| Obrazovka ostane po nahratí runtime tmavá | Na doske ešte nie je projekt | Nahraj projekt (F5); doska bez projektu nič na sklo nekreslí. |
| Dotyk nereaguje alebo reaguje na zlom mieste | Orientácia projektu sa líši od toho, ako je doska namontovaná | Nastav orientáciu na stránke HMIview a nahraj znova. |
| Sieť nenabehne | Žiadny DHCP server, alebo port nemá linku | Pozri LED linky na konektore; nastav pevnú adresu na stránke dosky; pri Wi-Fi skontroluj meno siete a heslo. |
| CAN mlčí | Chýba prevodník, zakončenie 120 ohm alebo je iná prenosová rýchlosť | Skontroluj prevodník na GPIO20 / GPIO21, rezistor 120 ohm na oboch koncoch zbernice a rovnakú rýchlosť na každom uzle. |
| Hodnota Modbus RTU ostáva 0 | Prehodené A a B, zlý unit alebo rýchlosť, alebo chýba pin DE | Prehoď A a B; skontroluj unit, rýchlosť a paritu; skontroluj, že DE je zapojený a pomenovaný. |

Panel **Messages** v editore a **diagnostický buffer** dosky (Online → Diagnostics) hovoria, čo runtime rozhodol a prečo - prečítaj ich ako prvé.

---

[← Vzorové projekty](examples/README.sk.md) | [Prehľad](README.sk.md)
