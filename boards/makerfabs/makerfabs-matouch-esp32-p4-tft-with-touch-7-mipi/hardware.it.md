---
title: 'Makerfabs MaTouch ESP32-P4 7": hardware e cablaggio'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch ESP32-P4 7" - mappa dei pin
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Hardware e cablaggio

## Cosa ti serve

- La Makerfabs MaTouch ESP32-P4 TFT with Touch 7" MIPI.
- Un cavo dati USB-C - per il primo caricamento del runtime e per l'alimentazione.
- Per l'alimentazione: un alimentatore USB-C da 5 V di almeno 2 A (la retroilluminazione del display ne assorbe la maggior parte).
- Un cavo Ethernet, oppure il Wi-Fi della tua rete.
- Un PC con l'[editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opzionale, per l'esempio all-in-one: due pulsanti e un modulo relè sul connettore J6; un modulo ADS1115 sul bus I2C; un transceiver RS-485 a 3,3 V (ad es. MAX3485) e un transceiver CAN a 3,3 V (ad es. SN65HVD230).

## Alimentazione

| Sorgente | Dove | Nota |
|---|---|---|
| USB 5 V | il connettore USB-C | 2 A o più - la retroilluminazione da 7" ne assorbe la maggior parte |
| Batteria Li-Po | il connettore della batteria | 3,7 V, ricaricata sulla scheda |

!!! warning "Un alimentatore debole"
    La porta USB di un PC spesso non regge la scheda con la
    retroilluminazione accesa. Se la scheda si riavvia mentre lo schermo
    si accende, usa un alimentatore da 5 V / 2 A o un hub USB alimentato.

## Mappa dei pin

![Makerfabs MaTouch ESP32-P4 7" - mappa dei pin](pinout/pinout.png)

| GPIO | Funzione in ctrl32 | Nota |
|---|---|---|
| 0 | RTC XTAL P | ⚠  |
| 1 | RTC XTAL N | ⚠  |
| 2 | libero - I/O |  |
| 3 | libero - I/O |  |
| 4 | libero - I/O |  |
| 5 | libero - I/O |  |
| 6 | C6 IO2 | ⚠  |
| 7 | TOUCH SDA |  |
| 8 | TOUCH SCL |  |
| 20 | libero - I/O |  |
| 21 | libero - I/O |  |
| 22 | TOUCH RST |  |
| 23 | TFT BL |  |
| 26 | USB1 PAIR | ⚠  |
| 27 | DSI RST |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 29 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 30 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 31 | Ethernet MDC (IP101GRI) | ⚠ usato dalla scheda |
| 32 | libero - I/O |  |
| 33 | libero - I/O |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 35 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 36 | libero - I/O | ⚠ pin di strapping |
| 37 | CONSOLE RX | ⚠ pin di strapping |
| 38 | CONSOLE TX | ⚠ pin di strapping |
| 45 | MOSFET GATE | ⚠  |
| 46 | libero - I/O |  |
| 47 | libero - I/O |  |
| 48 | libero - I/O |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 50 | Ethernet RMII (IP101GRI) | ⚠ usato dalla scheda |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ usato dalla scheda |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ usato dalla scheda |
| 53 | AMP EN | ⚠  |
| 54 | C6 EN | ⚠  |

I pin liberi si trovano sui connettori **J6** e **J10** e sui due
connettori Grove (**J1**, **J2**). Il bus I2C della scheda (GPIO7 / GPIO8)
porta il controller touch e il codec audio; altri chip I2C (un ADS1115, un
sensore) si collegano allo stesso bus. CAN e RS-485 non hanno transceiver
sulla scheda: l'esempio li mette su pin liberi - **CAN** TX GPIO20 / RX
GPIO21 (Grove J2), **RS-485** TX GPIO4 / RX GPIO5 / DE GPIO32 (J10) -
ciascuno verso un modulo transceiver a 3,3 V.

## Sicurezza

- La scheda non è destinata a funzioni di sicurezza. Un arresto di
  emergenza, un interruttore della porta o una barriera fotoelettrica si
  cablano in hardware, mai tramite un programma o uno schermo touch.
- I pin GPIO sono a 3,3 V. Un segnale a 24 V richiede un optoisolatore;
  la bobina di un relè richiede un driver (un modulo relè ne ha uno).
- Il touch capacitivo può registrare una falsa pressione vicino a una
  forte sorgente di disturbi (un inverter). I comandi critici su una
  schermata chiedono una conferma.

## Foto

![Makerfabs MaTouch ESP32-P4 7" - foto 1](img/board-01.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 2](img/board-02.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 3](img/board-03.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 4](img/board-04.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 5](img/board-05.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 6](img/board-06.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 7](img/board-07.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 8](img/board-08.jpg)

---

[← Panoramica](README.it.md) | [Panoramica](README.it.md) | [Installare il runtime →](install.it.md)
