---
title: 'Raspberry Pi 4 Model B: hibaelhárítás'
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

# Hibaelhárítás

| Tünet | Ok | Megoldás |
|---|---|---|
| A Look at the device nem tud csatlakozni | Az SSH ki van kapcsolva, rossz a cím, vagy a PC egy másik hálózaton van | Kapcsold be az SSH-t az Imager beállításaiban, és írd újra a kártyát; pingeld meg a címet a PC-ről. |
| A Prepare nem kínál telepítést | A ctrl32 runtime már telepítve van a Pi-n | A telepített runtime-ot a Flash runtime frissíti, a Pi címével a portválasztóban. |
| A monitor a letöltés után fekete marad | A monitort a rendszerindítás után csatlakoztattad, vagy a projektben nincs képernyő | Csatlakoztasd a monitort, mielőtt bekapcsolod a Pi-t; adj képernyőt a projekthez. |
| A WEBview nem nyílik meg | Rossz port | Nyisd meg a http://<cím>:8080 címet - a runtime a 8080-as porton szolgál ki. |
| Az USB-RS485 adapter eltűnik | Alacsony feszültség - a tápegység túl gyenge | Használd a hivatalos 27 W-os tápegységet. |
| A CAN néma marad | A HAT illesztőprogramja nincs betöltve, nincs lezárás, vagy eltér a bitsebesség | Jelöld be a HAT-ot a Prepare a Linux device-ban; 120 ohmos ellenállás a busz mindkét végén; minden csomóponton ugyanaz a bitsebesség. |
| Egy OPC UA kliens nem lát változókat | A változó távol van tartva a szervertől, vagy egy tűzfal blokkolja a 4840-es portot | Ellenőrizd az OPC UA pipát a változólistában; nyisd meg a 4840-es portot. |

A szerkesztő **Messages** ablaka és a panel **diagnosztikai puffere** (Online → Diagnostics) megmondja, mit döntött a runtime és miért - először ezeket olvasd el.

---

[← Példaprojektek](examples/README.hu.md) | [Áttekintés](README.hu.md)
