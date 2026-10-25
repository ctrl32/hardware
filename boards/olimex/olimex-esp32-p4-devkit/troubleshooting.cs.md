---
title: 'Olimex ESP32-P4-DevKit: řešení problémů'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-P4-DevKit
tags:
- esp32-p4
- ethernet
- olimex
- troubleshooting
---

# Řešení problémů

| Projev | Příčina | Řešení |
|---|---|---|
| COM port se neobjeví, výběr portu zůstane prázdný | Kabel jen napájí, nebo chybí ovladač USB | Použij datový kabel; nainstaluj ovladač USB čipu desky; zkus jiný port USB. |
| Flash runtime se zastaví při připojování | Port drží jiný program | Zavři sériový monitor nebo jiný nástroj, který má port otevřený, a zkus to znovu. |
| Deska se každých pár sekund restartuje | Port USB nedodá dost proudu | Použij napájený USB hub nebo zdroj 5 V alespoň 1 A. |
| Síť nenaběhne | Žádný DHCP server, nebo port nemá linku | Podívej se na LED linky na konektoru; nastav pevnou adresu na stránce desky; zkus jiný port switche. |
| Deska nejde najít podle jména .local | Síť blokuje mDNS (multicast) | Použij IP adresu desky - ukáže ji seznam klientů v routeru a Find devices v editoru. |
| Výstup nic nedělá | Pin je jen vstup, nebo byl zadán špatný pin | Podívej se na pin na stránce desky - piny jen pro vstup jsou označené; přesuň výstup na volný I/O pin. |
| Hodnota Modbus zůstává 0 | Špatná adresa zařízení, unit nebo registr | Zkontroluj IP a unit zařízení ve stromu zařízení a registr v manuálu zařízení. |

Panel **Messages** v editoru a **diagnostický buffer** desky (Online → Diagnostics) říkají, co runtime rozhodl a proč - přečti je jako první.

---

[← Vzorové projekty](examples/README.cs.md) | [Přehled](README.cs.md)
