---
title: Nahrání runtime ctrl32 do desky Makerfabs MaTouch ESP32-P4 7"
slug: install
sidebar_position: 30
image: img/install-04-flash-runtime.png
image_alt: Editor ctrl32 zapisuje runtime do desky Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- install
---

# Nahrání runtime ctrl32

Runtime je program v desce, který vykonává tvůj projekt - cyklus PLC, obrazovky, komunikaci. Do desky se nahraje jednou; potom je každá změna projektu nahráním, které přepíše jen projekt.

## 1. Připoj desku

Připoj desku k PC kabelem USB. Na konektoru USB-C je převodník USB-UART CH340K. Windows 10 a 11 si jeho
ovladač nainstalují samy; pokud se port neobjeví, nainstaluj ovladač CH340
od výrobce čipu (WCH) a kabel připoj znovu.

![Makerfabs MaTouch ESP32-P4 7"](img/board-01.jpg)

## 2. Vytvoř projekt

Spusť editor ctrl32 a zvol **New project** (Ctrl+N). Zadej **název** projektu, v seznamu desek vyber **MaTouch ESP32-P4 7"** (pod **Makerfabs**) a stiskni **Create project**.

![Průvodce New project s vybranou deskou Makerfabs MaTouch ESP32-P4 7"](img/install-02-new-project.png)

Chceš-li začít hotovým příkladem, otevři [projekt all-in-one](examples/all-in-one/README.cs.md) (**File → Open**).

## 3. Zapiš runtime

Vyber COM port desky ve výběru portu na panelu nástrojů, klikni na desku ve stromu zařízení a stiskni **Flash runtime**. Editor runtime zapíše, přečte zpět a ověří; trvá to asi minutu a deska se restartuje. Dělá se to jednou - a znovu až tehdy, když editor přinese novou řadu runtime.

![Dialog Flash runtime s runtime pro desku Makerfabs MaTouch ESP32-P4 7"](img/install-04-flash-runtime.png)

## 4. Nahraj projekt

Stiskni tlačítko nahrání na panelu nástrojů (F5). Editor projekt sestaví, zapíše ho do neaktivního slotu programu v desce, ověří ho a až pak přepne - nepovedené nahrání nechá běžící program nedotčený.

![Panel nástrojů: výběr portu a tlačítko nahrání](img/install-05-download.png)

## 5. Ověř, že běží

Stiskni **ONLINE** (ikona zástrčky vedle výběru portu) a sleduj program v desce: co vede, je zelené, každá proměnná nese živou hodnotu. Bez desky ukáže totéž **simulace** (tlačítko na panelu vedle ONLINE).

![Běžící ladder program - zelená znamená, že proud teče](img/install-06-running.png)

Něco nejde? Viz [Řešení problémů](troubleshooting.cs.md).

*Snímky obrazovky: editor ctrl32 1.07.*

---

[← Hardware a zapojení](hardware.cs.md) | [Přehled](README.cs.md) | [Nastavení →](configure.cs.md)
