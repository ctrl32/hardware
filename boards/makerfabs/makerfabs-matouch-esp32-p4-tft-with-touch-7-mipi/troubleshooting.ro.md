---
title: 'Makerfabs MaTouch ESP32-P4 7": depanare'
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

# Depanare

| Simptom | Cauză | Remediere |
|---|---|---|
| Portul COM nu apare | Cablul transportă doar alimentare sau lipsește driverul CH340 | Folosește un cablu de date USB-C; instalează driverul CH340 (WCH CH341SER); încearcă alt port USB. |
| Placa repornește când apare ecranul | Sursa nu poate duce iluminarea de fundal | Folosește o sursă de 5 V / 2 A sau un hub USB alimentat. |
| Ecranul rămâne negru după ce runtime-ul a fost scris | Încă niciun proiect pe placă | Descarcă proiectul (F5); o placă fără proiect nu arată nimic pe sticlă. |
| Touch-ul nu răspunde sau răspunde în locul greșit | Orientarea proiectului diferă de felul în care este montată placa | Setează orientarea pe pagina HMIview și descarcă din nou. |
| Rețeaua nu pornește | Niciun server DHCP sau niciun link pe port | Verifică LED-urile de link de pe mufă; setează o adresă fixă pe pagina plăcii; pentru Wi-Fi verifică numele rețelei și parola. |
| CAN rămâne mut | Niciun transceiver, nicio terminație de 120 ohm sau o altă rată de biți | Verifică transceiverul de pe GPIO20 / GPIO21, un rezistor de 120 ohm la ambele capete ale magistralei și aceeași rată de biți pe fiecare nod. |
| O valoare Modbus RTU rămâne la 0 | A și B inversate, unit sau viteză (baud) greșite ori lipsește pinul DE | Inversează A și B; verifică unit-ul, viteza (baud) și paritatea; verifică faptul că DE este cablat și numit. |

Panoul **Messages** al editorului și **bufferul de diagnostic** al plăcii (Online → Diagnostics) spun ce a decis runtime-ul și de ce - citește-le întâi.

---

[← Proiecte exemplu](examples/README.ro.md) | [Prezentare](README.ro.md)
