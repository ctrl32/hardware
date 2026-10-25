---
title: 'Raspberry Pi 4 Model B: risoluzione dei problemi'
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

# Risoluzione dei problemi

| Sintomo | Causa | Rimedio |
|---|---|---|
| Look at the device non riesce a connettersi | SSH è disattivato, l'indirizzo è errato, oppure il PC è in un'altra rete | Abilita SSH nelle impostazioni dell'Imager e riscrivi la scheda; fai un ping all'indirizzo dal PC. |
| Prepare non offre alcuna installazione | Il runtime ctrl32 è già installato sul Pi | Un runtime installato si aggiorna con Flash runtime e l'indirizzo del Pi nel selettore di porta. |
| Il monitor resta nero dopo il download | Il monitor è stato collegato dopo il boot, oppure il progetto non ha schermate | Collega il monitor prima di accendere il Pi; aggiungi una schermata al progetto. |
| WEBview non si apre | La porta sbagliata | Apri http://<indirizzo>:8080 - il runtime serve sulla porta 8080. |
| L'adattatore USB-RS485 scompare | Sottotensione - l'alimentatore è troppo debole | Usa l'alimentatore ufficiale da 27 W. |
| Il CAN resta muto | Il driver dell'HAT non è caricato, manca la terminazione, oppure il bit rate è diverso | Spunta l'HAT in Prepare a Linux device; una resistenza da 120 ohm a entrambe le estremità del bus; lo stesso bit rate su ogni nodo. |
| Un client OPC UA non vede alcuna variabile | La variabile è esclusa dal server, oppure un firewall blocca la porta 4840 | Controlla la spunta OPC UA nell'elenco delle variabili; apri la porta 4840. |

Il riquadro **Messages** dell'editor e il **buffer diagnostico** della scheda (Online → Diagnostics) dicono cosa ha deciso il runtime e perché - leggili per primi.

---

[← Progetti di esempio](examples/README.it.md) | [Panoramica](README.it.md)
