---
title: 'Olimex ESP32-POE2: hibaelhárítás'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-POE2
tags:
- esp32
- ethernet
- poe
- psram
- olimex
- troubleshooting
---

# Hibaelhárítás

| Tünet | Ok | Megoldás |
|---|---|---|
| A COM port nem jelenik meg, a portválasztó üres marad | A kábel csak tápot visz, vagy hiányzik az USB-illesztőprogram | Használj adatkábelt; telepítsd a panel USB-chipjének illesztőprogramját; próbálj egy másik USB portot. |
| A Flash runtime megáll csatlakozás közben | Egy másik program foglalja a portot | Zárd be a soros monitort vagy azt a másik eszközt, amely nyitva tartja a portot, majd próbáld újra. |
| A panel néhány másodpercenként újraindul | Az USB port nem tud elég áramot adni | Használj saját tápos USB hubot vagy legalább 1 A-es 5 V-os tápegységet. |
| A hálózat nem indul el | Nincs DHCP-szerver, vagy nincs link a porton | Ellenőrizd a csatlakozó link LED-jeit; állíts be fix címet a panel oldalán; próbáld a switch egy másik portját. |
| A panel nem található a .local nevén | A hálózat blokkolja az mDNS-t (multicast) | Használd a panel IP-címét - megmutatja a router kliens-listája és a szerkesztő Find devices funkciója. |
| Egy kimenet nem csinál semmit | A láb csak bemenet, vagy rossz lábat adtál meg | Ellenőrizd a lábat a panel oldalán - a csak bemeneti lábak jelölve vannak; tedd át a kimenetet egy szabad I/O lábra. |
| Egy Modbus érték 0-n marad | Rossz az eszköz címe, a unit vagy a regiszter | Ellenőrizd az eszköz IP-címét és unitját az eszközfában, a regisztert pedig az eszköz kézikönyvében. |
| Az USB lekapcsol, vagy a PC hibát jelez, amikor bedugod a PoE kábelt | Az USB és a PoE egyszerre csatlakozik egy nem leválasztott panelen | Azonnal húzd ki az egyiket. Előbb tölts fel USB-n, aztán üzemeltesd PoE-ről. |
| A 24 V-os / 12 V-os kimenet kikapcsolva marad | A panel USB-ről fut - a kimenetek csak PoE-ről jönnek | Tápláld a panelt PoE-ről (802.3at). |

A szerkesztő **Messages** ablaka és a panel **diagnosztikai puffere** (Online → Diagnostics) megmondja, mit döntött a runtime és miért - először ezeket olvasd el.

---

[← Példaprojektek](examples/README.hu.md) | [Áttekintés](README.hu.md)
