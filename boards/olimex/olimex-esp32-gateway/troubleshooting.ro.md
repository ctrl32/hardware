---
title: 'Olimex ESP32-GATEWAY: depanare'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-GATEWAY
tags:
- esp32
- ethernet
- gateway
- olimex
- troubleshooting
---

# Depanare

| Simptom | Cauză | Remediere |
|---|---|---|
| Portul COM nu apare, selectorul de port rămâne gol | Cablul transportă doar alimentare sau lipsește driverul USB | Folosește un cablu de date; instalează driverul cipului USB al plăcii; încearcă alt port USB. |
| Flash runtime se oprește la conectare | Alt program ține portul ocupat | Închide monitorul serial sau celălalt instrument care ține portul deschis, apoi încearcă din nou. |
| Placa repornește la câteva secunde | Portul USB nu poate furniza curentul | Folosește un hub USB alimentat sau o sursă de 5 V de cel puțin 1 A. |
| Rețeaua nu pornește | Niciun server DHCP sau niciun link pe port | Verifică LED-urile de link de pe mufă; setează o adresă fixă pe pagina plăcii; încearcă alt port al switch-ului. |
| Placa nu este găsită după numele ei .local | Rețeaua blochează mDNS (multicast) | Folosește adresa IP a plăcii - lista de clienți a routerului și Find devices din editor o arată. |
| O ieșire nu face nimic | Pinul este doar de intrare sau a fost indicat pinul greșit | Verifică pinul pe pagina plăcii - pinii doar de intrare sunt marcați; mută ieșirea pe un pin I/O liber. |
| O valoare Modbus rămâne la 0 | Adresa dispozitivului, unit-ul sau registrul sunt greșite | Verifică IP-ul și unit-ul dispozitivului în arborele de dispozitive și registrul în manualul dispozitivului. |

Panoul **Messages** al editorului și **bufferul de diagnostic** al plăcii (Online → Diagnostics) spun ce a decis runtime-ul și de ce - citește-le întâi.

---

[← Proiecte exemplu](examples/README.ro.md) | [Prezentare](README.ro.md)
