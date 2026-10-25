---
title: 'Makerfabs MaTouch ESP32-P4 7": risoluzione dei problemi'
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

# Risoluzione dei problemi

| Sintomo | Causa | Rimedio |
|---|---|---|
| La porta COM non compare | Il cavo porta solo alimentazione, oppure manca il driver CH340 | Usa un cavo dati USB-C; installa il driver CH340 (WCH CH341SER); prova un'altra porta USB. |
| La scheda si riavvia quando lo schermo si accende | L'alimentatore non regge la retroilluminazione | Usa un alimentatore da 5 V / 2 A o un hub USB alimentato. |
| Lo schermo resta scuro dopo la scrittura del runtime | Nessun progetto ancora sulla scheda | Scarica il progetto (F5); una scheda senza progetto non mostra nulla sul vetro. |
| Il touch non risponde, oppure risponde nel punto sbagliato | L'orientamento del progetto differisce da come è montata la scheda | Imposta l'orientamento nella pagina HMIview e scarica di nuovo. |
| La rete non si attiva | Nessun server DHCP, oppure nessun link sulla porta | Controlla i LED di link sul connettore; imposta un indirizzo fisso nella pagina della scheda; per il Wi-Fi controlla il nome della rete e la password. |
| Il CAN resta muto | Nessun transceiver, nessuna terminazione da 120 ohm, oppure un bit rate diverso | Controlla il transceiver su GPIO20 / GPIO21, una resistenza da 120 ohm a entrambe le estremità del bus e lo stesso bit rate su ogni nodo. |
| Un valore Modbus RTU resta a 0 | A e B invertiti, unit o baud rate errati, oppure manca il pin DE | Inverti A e B; controlla unit, baud rate e parità; verifica che DE sia cablato e indicato. |

Il riquadro **Messages** dell'editor e il **buffer diagnostico** della scheda (Online → Diagnostics) dicono cosa ha deciso il runtime e perché - leggili per primi.

---

[← Progetti di esempio](examples/README.it.md) | [Panoramica](README.it.md)
