---
title: 'Olimex ESP32-PoE: řešení problémů'
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

# Řešení problémů

| Projev | Příčina | Řešení |
|---|---|---|
| COM port se neobjeví, výběr portu zůstane prázdný | Kabel jen napájí, nebo chybí ovladač CH340 | Použij datový kabel; nainstaluj ovladač CH340 (WCH CH341SER); zkus jiný port USB. |
| Flash runtime se zastaví při připojování | Port drží jiný program | Zavři sériový monitor nebo jiný nástroj, který má port otevřený, a zkus to znovu. |
| Deska se každých pár sekund restartuje | Port USB nedodá proud, když startuje Ethernet | Použij napájený USB hub nebo zdroj 5 V alespoň 1 A, nebo desku napájej z PoE (bez USB). |
| Síť nenaběhne | Žádný DHCP server, nebo port nemá linku | Zkontroluj LED linky na konektoru; nastav pevnou adresu na stránce desky; zkus jiný port switche. |
| Desku nelze najít podle jména .local | Síť blokuje mDNS (multicast) | Použij IP adresu desky - ukáže ji seznam klientů v routeru a Find devices v editoru. |
| USB se odpojí nebo PC hlásí chybu, když se zapojí kabel PoE | USB a PoE zapojené současně na desce, která není oddělená | Okamžitě jedno odpoj. Nejdřív nahraj přes USB, potom provozuj na PoE - nebo použij ESP32-PoE-ISO. |
| Výstup na GPIO34 až GPIO39 nic nedělá | Tyto piny jsou pouze vstupy | Přesuň výstup na GPIO33, GPIO4 nebo GPIO5. |
| Hodnota Modbus zůstává 0 | Špatná adresa zařízení, unit nebo registr, nebo je zařízení v jiné podsíti | Zkontroluj IP a unit zařízení ve stromu zařízení a registr v manuálu zařízení; zkus zařízení z PC pingnout. |

Panel **Messages** v editoru a **diagnostický buffer** desky (Online → Diagnostics) říkají, co runtime rozhodl a proč - přečti je jako první.

---

[← Vzorové projekty](examples/README.cs.md) | [Přehled](README.cs.md)
