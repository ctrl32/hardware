---
title: 'Makerfabs MaTouch ESP32-P4 7": hibaelhárítás'
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

# Hibaelhárítás

| Tünet | Ok | Megoldás |
|---|---|---|
| A COM port nem jelenik meg | A kábel csak tápot visz, vagy hiányzik a CH340 illesztőprogram | Használj USB-C adatkábelt; telepítsd a CH340 illesztőprogramot (WCH CH341SER); próbálj egy másik USB portot. |
| A panel újraindul, amikor a képernyő megjelenik | A tápegység nem bírja a háttérvilágítást | Használj 5 V / 2 A-es tápegységet vagy saját tápos USB hubot. |
| A képernyő sötét marad a runtime megírása után | Még nincs projekt a panelen | Töltsd le a projektet (F5); projekt nélkül a panel semmit sem mutat a kijelzőn. |
| Az érintés nem reagál, vagy rossz helyen reagál | A projekt tájolása eltér attól, ahogy a panel be van építve | Állítsd be a tájolást a HMIview oldalon, és töltsd le újra. |
| A hálózat nem indul el | Nincs DHCP-szerver, vagy nincs link a porton | Ellenőrizd a csatlakozó link LED-jeit; állíts be fix címet a panel oldalán; Wi-Fi esetén ellenőrizd a hálózat nevét és a jelszót. |
| A CAN néma marad | Nincs adó-vevő, nincs 120 ohmos lezárás, vagy eltér a bitsebesség | Ellenőrizd az adó-vevőt a GPIO20 / GPIO21 lábon, a 120 ohmos ellenállást a busz mindkét végén, és hogy minden csomóponton ugyanaz a bitsebesség. |
| Egy Modbus RTU érték 0-n marad | Az A és a B fel van cserélve, rossz a unit vagy az átviteli sebesség, vagy hiányzik a DE láb | Cseréld fel az A-t és a B-t; ellenőrizd a unitot, az átviteli sebességet és a paritást; ellenőrizd, hogy a DE be van-e kötve és meg van-e adva. |

A szerkesztő **Messages** ablaka és a panel **diagnosztikai puffere** (Online → Diagnostics) megmondja, mit döntött a runtime és miért - először ezeket olvasd el.

---

[← Példaprojektek](examples/README.hu.md) | [Áttekintés](README.hu.md)
