---
title: 'Raspberry Pi 3 Model B+: depanare'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Raspberry Pi 3 Model B+
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- troubleshooting
---

# Depanare

| Simptom | Cauză | Remediere |
|---|---|---|
| Look at the device nu se poate conecta | SSH este oprit, adresa este greșită sau PC-ul este în altă rețea | Activează SSH în setările Imager-ului și scrie din nou cardul; dă ping adresei de pe PC. |
| Prepare nu oferă nicio instalare | Runtime-ul ctrl32 este deja instalat pe Pi | Un runtime instalat se actualizează cu Flash runtime și adresa Pi-ului în selectorul de port. |
| Monitorul rămâne negru după descărcare | Monitorul a fost conectat după boot sau proiectul nu are ecran | Conectează monitorul înainte de a porni Pi-ul; adaugă un ecran în proiect. |
| WEBview nu se deschide | Portul greșit | Deschide http://<adresă>:8080 - runtime-ul servește pe 8080. |
| Adaptorul USB-RS485 dispare | Subtensiune - sursa este prea slabă | Folosește sursa oficială de 27 W. |
| CAN rămâne mut | Driverul HAT-ului nu este încărcat, lipsește terminația sau rata de biți diferă | Bifează HAT-ul în Prepare a Linux device; un rezistor de 120 ohm la ambele capete ale magistralei; aceeași rată de biți pe fiecare nod. |
| Un client OPC UA nu vede nicio variabilă | Variabila este ținută în afara serverului sau un firewall blochează portul 4840 | Verifică bifa OPC UA din lista de variabile; deschide portul 4840. |

Panoul **Messages** al editorului și **bufferul de diagnostic** al plăcii (Online → Diagnostics) spun ce a decis runtime-ul și de ce - citește-le întâi.

---

[← Proiecte exemplu](examples/README.ro.md) | [Prezentare](README.ro.md)
