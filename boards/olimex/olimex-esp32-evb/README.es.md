---
title: Olimex ESP32-EVB
slug: olimex-esp32-evb
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-evb/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-EVB con sus dos relés, el conector Ethernet y el borne CAN
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Olimex ESP32-EVB

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 240x320](https://img.shields.io/badge/HMI-240x320-0891b2)

![Placa Olimex ESP32-EVB con sus dos relés, el conector Ethernet y el borne CAN](img/board-01.jpg)

La Olimex ESP32-EVB es una placa ESP32 hecha para controlar: dos relés (10 A / 250 VAC), un transceptor CAN, Ethernet y Wi-Fi en una sola placa. Con ctrl32 es un PLC listo - los relés y el botón son variables de un programa ladder, CAN habla con variadores y nodos de E/S, y la página del operador funciona en cualquier navegador (WEBview). Una pantalla táctil opcional de 2,8" en el conector UEXT la convierte en un pequeño panel.

**Ideal para:**

- Un control de relés - calefacción, bombas, luces - con Ethernet
- Un maestro CAN para un variador o nodos de E/S CANopen
- Un termostato o un pequeño panel con la pantalla opcional de 2,8"

Página de la placa en el catálogo: [Olimex ESP32-EVB](https://ctrl32.com/hardware/boards/olimex-esp32-evb/)

![Olimex ESP32-EVB - mapa de pines: la función de cada GPIO en ctrl32](pinout/pinout.png)

## Qué puede hacer ctrl32 en esta placa

<!-- capabilities:start -->
| Característica | En esta placa | Notas |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memoria | 4 MB flash |  |
| Tamaño del programa | 128 variables, 32 alarmas, 128 bloques | el editor lo comprueba antes de una descarga |
| Entradas / salidas digitales | 6 GPIO libres | 2 de ellos solo entradas |
| Entradas analógicas | 4 en el chip (ADC1) | GPIO32, GPIO33, GPIO34, GPIO36 |
| Ethernet | sí - LAN8710A |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 |  |
| Modbus RTU (RS-485) | sí - en pines libres | necesita un transceptor externo |
| Modbus TCP | cliente y servidor |  |
| MQTT | sí | descubrimiento en Home Assistant |
| WEBview | sí | la página del operador en cualquier navegador |
| Pantalla / táctil (HMI) | - 240x320, - |  |
| USB | Micro-USB (CH340T USB-UART) |  |
| Alimentación | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Qué no está soportado

- Bluetooth.
- El receptor y el emisor IR - ctrl32 no los usa en esta placa.
- La ranura microSD - ctrl32 guarda el programa y las pantallas en la propia flash del chip.

## La guía

| Paso | Página |
|---|---|
| 1 | [Hardware y cableado](hardware.es.md) - qué necesitas, alimentación, el mapa de pines |
| 2 | [Instalar el runtime](install.es.md) - el editor, la placa, la primera carga |
| 3 | [Configurar](configure.es.md) - red, E/S, comunicación |
| 4 | [Proyectos de ejemplo](examples/README.es.md) - todo lo que hace la placa, listo para abrir |
| - | [Solución de problemas](troubleshooting.es.md) |

## Archivos

-

## Siguientes pasos

- [Documentación de ctrl32](https://ctrl32.com/docs/) - el editor, los lenguajes, cada bloque
- [Descargar el editor](https://ctrl32.com/download/)
- [Todas las placas probadas](../../README.es.md)
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.es.md) - Ethernet y Power over Ethernet

