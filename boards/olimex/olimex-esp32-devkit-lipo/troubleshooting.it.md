---
title: 'Olimex ESP32-DevKit-LiPo: risoluzione dei problemi'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-DevKit-LiPo
tags:
- esp32
- wifi
- battery
- olimex
- troubleshooting
---

# Risoluzione dei problemi

| Sintomo | Causa | Rimedio |
|---|---|---|
| La porta COM non compare, il selettore di porta resta vuoto | Il cavo porta solo alimentazione, oppure manca il driver USB | Usa un cavo dati; installa il driver del chip USB della scheda; prova un'altra porta USB. |
| Flash runtime si ferma durante la connessione | Un altro programma occupa la porta | Chiudi il monitor seriale o l'altro strumento che tiene aperta la porta, poi riprova. |
| La scheda si riavvia ogni pochi secondi | La porta USB non riesce a fornire la corrente | Usa un hub USB alimentato o un alimentatore da 5 V di almeno 1 A. |
| La scheda non si collega al Wi-Fi | Nome della rete o password errati, oppure una rete solo a 5 GHz | Controlla nome e password nella pagina WiFi; l'ESP32 si collega solo a reti a 2,4 GHz. |
| La scheda non viene trovata con il suo nome .local | La rete blocca mDNS (multicast) | Usa l'indirizzo IP della scheda - lo mostrano l'elenco dei client del router e Find devices nell'editor. |
| Un'uscita non fa nulla | Il pin è solo un ingresso, oppure è stato indicato il pin sbagliato | Controlla il pin nella pagina della scheda - i pin solo ingresso sono contrassegnati; sposta l'uscita su un pin I/O libero. |
| Un valore Modbus resta a 0 | L'indirizzo del dispositivo, la unit o il registro sono errati | Controlla IP e unit del dispositivo nell'albero dei dispositivi e il registro nel manuale del dispositivo. |

Il riquadro **Messages** dell'editor e il **buffer diagnostico** della scheda (Online → Diagnostics) dicono cosa ha deciso il runtime e perché - leggili per primi.

---

[← Progetti di esempio](examples/README.it.md) | [Panoramica](README.it.md)
