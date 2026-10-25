---
title: LaskaKit ESPlan
slug: laskakit-esplan
sidebar_position: 10
hardware: /hardware/boards/laskakit-esplan/
image: img/board-01.jpg
image_alt: Placa LaskaKit ESPlan cu mufa Ethernet, clema RS-485 și clema de alimentare
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# LaskaKit ESPlan

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Placa LaskaKit ESPlan cu mufa Ethernet, clema RS-485 și clema de alimentare](img/board-01.jpg)

LaskaKit ESPlan este o placă industrială cu ESP32: Ethernet 10/100, o interfață RS-485 cu protecție și terminație comutabilă, Wi-Fi și o alimentare largă de 7-40 V pe o clemă cu șurub (sau PoE cu un modul suplimentar). Cu ctrl32 este un master sau slave Modbus RTU într-un dulap - un program ladder pe cip, dispozitive RS-485 citite și scrise, valorile pe Modbus TCP, MQTT și pe pagina sa de operator (WEBview).

**Potrivit pentru:**

- Un master Modbus RTU pentru contoare, senzori și acționări, alimentat la 24 V
- Un gateway Modbus RTU / TCP cu logică proprie
- Automatizarea clădirilor într-un dulap

Pagina plăcii în catalog: [LaskaKit ESPlan](https://ctrl32.com/hardware/boards/laskakit-esplan/)

![LaskaKit ESPlan - harta pinilor: funcția fiecărui GPIO în ctrl32](pinout/pinout.png)

## Ce poate face ctrl32 pe această placă

<!-- capabilities:start -->
| Funcție | Pe această placă | Note |
|---|---|---|
| Cip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memorie | 4 MB flash |  |
| Mărimea programului | 128 variabile, 32 alarme, 128 blocuri | verificat de editor înainte de descărcare |
| Intrări / ieșiri digitale | 5 GPIO libere | 2 dintre ele doar intrări |
| Intrări analogice | 2 pe cip (ADC1) | GPIO35, GPIO39 |
| Ethernet | da - LAN8720A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - pe pini liberi | necesită un transceiver extern |
| Modbus RTU (RS-485) | da |  |
| Modbus TCP | client și server |  |
| MQTT | da | descoperire în Home Assistant |
| WEBview | da | pagina operatorului în orice browser |
| Afișaj / touch (HMI) | nu | pagina operatorului este WEBview |
| USB | USB-C (CH9102 USB-UART) |  |
| Alimentare | 5 V USB, PoE |  |
<!-- capabilities:end -->

### Ce nu este suportat

- Bluetooth - ESP32 îl are, ctrl32 nu îl folosește.
- Slotul microSD - ctrl32 ține programul și ecranele în flash-ul propriu al cipului.

## Ghidul

| Pas | Pagină |
|---|---|
| 1 | [Hardware și cablare](hardware.ro.md) - de ce ai nevoie, alimentarea, harta pinilor |
| 2 | [Instalarea runtime-ului](install.ro.md) - editorul, placa, prima încărcare |
| 3 | [Configurare](configure.ro.md) - rețea, I/O, comunicație |
| 4 | [Proiecte exemplu](examples/README.ro.md) - tot ce face placa, gata de deschis |
| - | [Depanare](troubleshooting.ro.md) |

## Fișiere

-

## Pașii următori

- [Documentația ctrl32](https://ctrl32.com/docs/) - editorul, limbajele, fiecare bloc
- [Descarcă editorul](https://ctrl32.com/download/)
- [Toate plăcile testate](../../README.ro.md)

