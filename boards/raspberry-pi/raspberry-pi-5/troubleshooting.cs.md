---
title: 'Raspberry Pi 5: řešení problémů'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Raspberry Pi 5
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- ethercat
- troubleshooting
---

# Řešení problémů

| Projev | Příčina | Řešení |
|---|---|---|
| Look at the device se nemůže připojit | SSH je vypnuté, adresa je špatně nebo je PC v jiné síti | Zapni SSH v nastavení Imageru a kartu zapiš znovu; pingni adresu z PC. |
| Prepare nenabídne instalaci | Runtime ctrl32 už je na Pi nainstalovaný | Nainstalovaný runtime se aktualizuje přes Flash runtime s adresou Pi ve výběru portu. |
| Monitor zůstane po nahrání černý | Monitor byl připojen až po startu, nebo projekt nemá obrazovku | Připoj monitor před zapnutím Pi; přidej do projektu obrazovku. |
| WEBview se neotevře | Špatný port | Otevři http://<adresa>:8080 - runtime běží na portu 8080. |
| Adaptér USB-RS485 zmizí | Podpětí - zdroj je příliš slabý | Použij oficiální zdroj 27 W. |
| CAN mlčí | Ovladač HATu není načtený, chybí zakončení nebo je jiná přenosová rychlost | Zaškrtni HAT v Prepare a Linux device; rezistor 120 ohmů na obou koncích sběrnice; stejná rychlost na každém uzlu. |
| Klient OPC UA nevidí žádné proměnné | Proměnná je ze serveru vyřazená, nebo firewall blokuje port 4840 | Zkontroluj zaškrtnutí OPC UA v seznamu proměnných; otevři port 4840. |

Panel **Messages** v editoru a **diagnostický buffer** desky (Online → Diagnostics) říkají, co runtime rozhodl a proč - přečti je jako první.

---

[← Vzorové projekty](examples/README.cs.md) | [Přehled](README.cs.md)
