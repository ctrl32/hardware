---
title: 'Olimex ESP32-PoE: hibaelhárítás'
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

# Hibaelhárítás

| Tünet | Ok | Megoldás |
|---|---|---|
| A COM port nem jelenik meg, a portválasztó üres marad | A kábel csak tápot visz, vagy hiányzik a CH340 illesztőprogram | Használj adatkábelt; telepítsd a CH340 illesztőprogramot (WCH CH341SER); próbálj egy másik USB portot. |
| A Flash runtime megáll csatlakozás közben | Egy másik program foglalja a portot | Zárd be a soros monitort vagy azt a másik eszközt, amely nyitva tartja a portot, majd próbáld újra. |
| A panel néhány másodpercenként újraindul | Az USB port nem tud elég áramot adni, amíg az Ethernet elindul | Használj saját tápos USB hubot vagy legalább 1 A-es 5 V-os tápegységet, vagy üzemeltesd a panelt PoE-ről (USB nélkül). |
| A hálózat nem indul el | Nincs DHCP-szerver, vagy nincs link a porton | Ellenőrizd a csatlakozó link LED-jeit; állíts be fix címet az Ethernet oldalon; próbáld a switch egy másik portját. |
| A panel nem található a .local nevén | A hálózat blokkolja az mDNS-t (multicast) | Használd a panel IP-címét - megmutatja a router kliens-listája és a szerkesztő Find devices funkciója. |
| Az USB lekapcsol, vagy a PC hibát jelez, amikor bedugod a PoE kábelt | Az USB és a PoE egyszerre csatlakozik egy nem leválasztott panelen | Azonnal húzd ki az egyiket. Előbb tölts fel USB-n, aztán üzemeltesd PoE-ről - vagy használd az ESP32-PoE-ISO panelt. |
| Egy kimenet a GPIO34-GPIO39 lábon nem csinál semmit | Ezek a lábak csak bemenetek | Tedd át a kimenetet a GPIO33, GPIO4 vagy GPIO5 lábra. |
| Egy Modbus érték 0-n marad | Rossz az eszköz címe, a unit vagy a regiszter, vagy az eszköz egy másik alhálózatban van | Ellenőrizd az eszköz IP-címét és unitját az eszközfában, a regisztert pedig az eszköz kézikönyvében; pingeld meg az eszközt a PC-ről. |

A szerkesztő **Messages** ablaka és a panel **diagnosztikai puffere** (Online → Diagnostics) megmondja, mit döntött a runtime és miért - először ezeket olvasd el.

---

[← Példaprojektek](examples/README.hu.md) | [Áttekintés](README.hu.md)
