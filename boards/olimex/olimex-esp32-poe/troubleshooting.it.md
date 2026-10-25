---
title: 'Olimex ESP32-PoE: risoluzione dei problemi'
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

# Risoluzione dei problemi

| Sintomo | Causa | Rimedio |
|---|---|---|
| La porta COM non compare, il selettore di porta resta vuoto | Il cavo porta solo alimentazione, oppure manca il driver CH340 | Usa un cavo dati; installa il driver CH340 (WCH CH341SER); prova un'altra porta USB. |
| Flash runtime si ferma durante la connessione | Un altro programma occupa la porta | Chiudi il monitor seriale o l'altro strumento che tiene aperta la porta, poi riprova. |
| La scheda si riavvia ogni pochi secondi | La porta USB non riesce a fornire la corrente mentre si avvia l'Ethernet | Usa un hub USB alimentato o un alimentatore da 5 V di almeno 1 A, oppure fai funzionare la scheda in PoE (senza USB). |
| La rete non si attiva | Nessun server DHCP, oppure nessun link sulla porta | Controlla i LED di link sul connettore; imposta un indirizzo fisso nella pagina Ethernet; prova un'altra porta dello switch. |
| La scheda non viene trovata con il suo nome .local | La rete blocca mDNS (multicast) | Usa l'indirizzo IP della scheda - lo mostrano l'elenco dei client del router e Find devices nell'editor. |
| L'USB si disconnette o il PC segnala un errore quando si collega il cavo PoE | USB e PoE collegati contemporaneamente su una scheda non isolata | Scollega subito uno dei due. Carica prima tramite USB, poi fai funzionare in PoE - oppure usa la ESP32-PoE-ISO. |
| Un'uscita da GPIO34 a GPIO39 non fa nulla | Questi pin sono solo ingressi | Sposta l'uscita su GPIO33, GPIO4 o GPIO5. |
| Un valore Modbus resta a 0 | L'indirizzo del dispositivo, la unit o il registro sono errati, oppure il dispositivo è in un'altra sottorete | Controlla IP e unit del dispositivo nell'albero dei dispositivi e il registro nel manuale del dispositivo; fai un ping al dispositivo dal PC. |

Il riquadro **Messages** dell'editor e il **buffer diagnostico** della scheda (Online → Diagnostics) dicono cosa ha deciso il runtime e perché - leggili per primi.

---

[← Progetti di esempio](examples/README.it.md) | [Panoramica](README.it.md)
