---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": hibaelhárítás'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95"
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
- troubleshooting
---

# Hibaelhárítás

| Tünet | Ok | Megoldás |
|---|---|---|
| A COM port nem jelenik meg, a portválasztó üres marad | A kábel csak tápot visz, vagy hiányzik az USB-illesztőprogram | Használj adatkábelt; telepítsd a panel USB-chipjének illesztőprogramját; próbálj egy másik USB portot. |
| A Flash runtime megáll csatlakozás közben | Egy másik program foglalja a portot | Zárd be a soros monitort vagy azt a másik eszközt, amely nyitva tartja a portot, majd próbáld újra. |
| A panel néhány másodpercenként újraindul | Az USB port nem tud elég áramot adni | Használj saját tápos USB hubot vagy legalább 1 A-es 5 V-os tápegységet. |
| A panel nem csatlakozik a Wi-Fi-hez | Rossz hálózatnév vagy jelszó, vagy csak 5 GHz-es hálózat | Ellenőrizd a nevet és a jelszót a WiFi oldalon; az ESP32 csak 2,4 GHz-es hálózatokhoz csatlakozik. |
| A panel nem található a .local nevén | A hálózat blokkolja az mDNS-t (multicast) | Használd a panel IP-címét - megmutatja a router kliens-listája és a szerkesztő Find devices funkciója. |
| Egy kimenet nem csinál semmit | A láb csak bemenet, vagy rossz lábat adtál meg | Ellenőrizd a lábat a panel oldalán - a csak bemeneti lábak jelölve vannak; tedd át a kimenetet egy szabad I/O lábra. |
| Egy Modbus érték 0-n marad | Rossz az eszköz címe, a unit vagy a regiszter | Ellenőrizd az eszköz IP-címét és unitját az eszközfában, a regisztert pedig az eszköz kézikönyvében. |
| A CAN néma marad | Nincs 120 ohmos lezárás, vagy eltér a bitsebesség | Tegyél 120 ohmos ellenállást a busz mindkét végére; minden csomóponton ugyanazt a bitsebességet állítsd be. |
| Egy Modbus RTU érték 0-n marad | Az A és a B fel van cserélve, vagy rossz a unit, az átviteli sebesség vagy a paritás | Cseréld fel az A-t és a B-t; ellenőrizd az eszköz unitját, átviteli sebességét és paritását. |

A szerkesztő **Messages** ablaka és a panel **diagnosztikai puffere** (Online → Diagnostics) megmondja, mit döntött a runtime és miért - először ezeket olvasd el.

---

[← Példaprojektek](examples/README.hu.md) | [Áttekintés](README.hu.md)
