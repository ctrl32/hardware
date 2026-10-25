---
title: 'Makerfabs MaTouch ESP32-P4 7": řešení problémů'
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

# Řešení problémů

| Projev | Příčina | Řešení |
|---|---|---|
| COM port se neobjeví | Kabel jen napájí, nebo chybí ovladač CH340 | Použij datový kabel USB-C; nainstaluj ovladač CH340 (WCH CH341SER); zkus jiný port USB. |
| Deska se restartuje, když se rozsvítí obrazovka | Zdroj neutáhne podsvícení | Použij zdroj 5 V / 2 A nebo USB hub s vlastním napájením. |
| Obrazovka zůstane po nahrání runtime tmavá | Na desce ještě není projekt | Nahraj projekt (F5); deska bez projektu na sklo nic nekreslí. |
| Dotyk nereaguje nebo reaguje na špatném místě | Orientace projektu se liší od toho, jak je deska namontovaná | Nastav orientaci na stránce HMIview a nahraj znovu. |
| Síť nenaběhne | Žádný DHCP server, nebo port nemá linku | Podívej se na LED linky na konektoru; nastav pevnou adresu na stránce desky; u Wi-Fi zkontroluj jméno sítě a heslo. |
| CAN mlčí | Chybí převodník, zakončení 120 ohmů nebo je jiná přenosová rychlost | Zkontroluj převodník na GPIO20 / GPIO21, rezistor 120 ohmů na obou koncích sběrnice a stejnou rychlost na každém uzlu. |
| Hodnota Modbus RTU zůstává 0 | Prohozené A a B, špatný unit nebo rychlost, nebo chybí pin DE | Prohoď A a B; zkontroluj unit, rychlost a paritu; zkontroluj, že DE je zapojený a pojmenovaný. |

Panel **Messages** v editoru a **diagnostický buffer** desky (Online → Diagnostics) říkají, co runtime rozhodl a proč - přečti je jako první.

---

[← Vzorové projekty](examples/README.cs.md) | [Přehled](README.cs.md)
