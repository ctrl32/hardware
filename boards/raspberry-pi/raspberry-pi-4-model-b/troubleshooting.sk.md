---
title: 'Raspberry Pi 4 Model B: riešenie problémov'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Raspberry Pi 4 Model B
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
- troubleshooting
---

# Riešenie problémov

| Prejav | Príčina | Riešenie |
|---|---|---|
| Look at the device sa nevie pripojiť | SSH je vypnuté, adresa je zlá alebo je PC v inej sieti | Zapni SSH v nastaveniach Imagera a kartu zapíš znova; pingni adresu z PC. |
| Prepare neponúkne inštaláciu | Runtime ctrl32 je už na Pi nainštalovaný | Nainštalovaný runtime sa aktualizuje cez Flash runtime s adresou Pi vo výbere portu. |
| Monitor ostane po nahratí čierny | Monitor bol pripojený až po štarte, alebo projekt nemá obrazovku | Pripoj monitor pred zapnutím Pi; pridaj do projektu obrazovku. |
| WEBview sa neotvorí | Zlý port | Otvor http://<adresa>:8080 - runtime beží na porte 8080. |
| Adaptér USB-RS485 zmizne | Podpätie - zdroj je príliš slabý | Použi oficiálny zdroj 27 W. |
| CAN mlčí | Ovládač HAT-u nie je načítaný, chýba zakončenie alebo je iná prenosová rýchlosť | Zaškrtni HAT v Prepare a Linux device; rezistor 120 ohm na oboch koncoch zbernice; rovnaká rýchlosť na každom uzle. |
| Klient OPC UA nevidí žiadne premenné | Premenná je zo servera vyradená, alebo firewall blokuje port 4840 | Skontroluj zaškrtnutie OPC UA v zozname premenných; otvor port 4840. |

Panel **Messages** v editore a **diagnostický buffer** dosky (Online → Diagnostics) hovoria, čo runtime rozhodol a prečo - prečítaj ich ako prvé.

---

[← Vzorové projekty](examples/README.sk.md) | [Prehľad](README.sk.md)
