---
title: 'Olimex ESP32-PoE: depanare'
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

# Depanare

| Simptom | Cauză | Remediere |
|---|---|---|
| Portul COM nu apare, selectorul de port rămâne gol | Cablul transportă doar alimentare sau lipsește driverul CH340 | Folosește un cablu de date; instalează driverul CH340 (WCH CH341SER); încearcă alt port USB. |
| Flash runtime se oprește la conectare | Alt program ține portul ocupat | Închide monitorul serial sau celălalt instrument care ține portul deschis, apoi încearcă din nou. |
| Placa repornește la câteva secunde | Portul USB nu poate furniza curentul cât pornește Ethernet | Folosește un hub USB alimentat sau o sursă de 5 V de cel puțin 1 A ori rulează placa pe PoE (fără USB). |
| Rețeaua nu pornește | Niciun server DHCP sau niciun link pe port | Verifică LED-urile de link de pe mufă; setează o adresă fixă pe pagina Ethernet; încearcă alt port al switch-ului. |
| Placa nu este găsită după numele ei .local | Rețeaua blochează mDNS (multicast) | Folosește adresa IP a plăcii - lista de clienți a routerului și Find devices din editor o arată. |
| USB se deconectează sau PC-ul semnalează o eroare când se conectează cablul PoE | USB și PoE conectate în același timp la o placă neizolată | Deconectează imediat unul dintre ele. Încarcă întâi prin USB, apoi rulează pe PoE - sau folosește ESP32-PoE-ISO. |
| O ieșire pe GPIO34 până la GPIO39 nu face nimic | Acești pini sunt doar intrări | Mută ieșirea pe GPIO33, GPIO4 sau GPIO5. |
| O valoare Modbus rămâne la 0 | Adresa dispozitivului, unit-ul sau registrul sunt greșite ori dispozitivul este în altă subrețea | Verifică IP-ul și unit-ul dispozitivului în arborele de dispozitive și registrul în manualul dispozitivului; dă ping dispozitivului de pe PC. |

Panoul **Messages** al editorului și **bufferul de diagnostic** al plăcii (Online → Diagnostics) spun ce a decis runtime-ul și de ce - citește-le întâi.

---

[← Proiecte exemplu](examples/README.ro.md) | [Prezentare](README.ro.md)
