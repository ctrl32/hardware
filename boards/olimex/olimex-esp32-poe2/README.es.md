---
title: Olimex ESP32-POE2
slug: olimex-esp32-poe2
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe2/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-POE2 con el conector Ethernet y las salidas de alimentación
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Olimex ESP32-POE2

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Placa Olimex ESP32-POE2 con el conector Ethernet y las salidas de alimentación](img/board-01.jpg)

La Olimex ESP32-POE2 es la siguiente generación de la ESP32-PoE: un ESP32 con 8 MB de PSRAM, Ethernet y Power over Ethernet IEEE 802.3at que también alimenta tus dispositivos de campo - salidas de 24 V o 12 V, 5 V y 3,3 V, hasta 25 W desde el cable de red. Con ctrl32 es un PLC en un armario alimentado con un solo cable: lógica ladder, WEBview, Modbus TCP y MQTT, con el tamaño de programa completo de un ESP32 clásico con PSRAM.

**Ideal para:**

- Un PLC de armario que alimenta sus sensores y un pequeño módulo de relés desde PoE
- Una pasarela Modbus TCP con MQTT hacia Home Assistant
- Automatización de edificios con un cable por habitación

Página de la placa en el catálogo: [Olimex ESP32-POE2](https://ctrl32.com/hardware/boards/olimex-esp32-poe2/)

![Olimex ESP32-POE2 - mapa de pines: la función de cada GPIO en ctrl32](pinout/pinout.png)

## Qué puede hacer ctrl32 en esta placa

<!-- capabilities:start -->
| Característica | En esta placa | Notas |
|---|---|---|
| Chip | ESP32 (ESP32-WROVER-E-N4R8) |  |
| Memoria | 4 MB flash, 8 MB PSRAM |  |
| Tamaño del programa | 512 variables, 128 alarmas, 1024 bloques | el editor lo comprueba antes de una descarga |
| Entradas / salidas digitales | 5 GPIO libres | 3 de ellos solo entradas |
| Entradas analógicas | 3 en el chip (ADC1) | GPIO34, GPIO36, GPIO39 |
| Ethernet | sí - LAN8710A |  |
| Power over Ethernet | IEEE 802.3at |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - en pines libres | necesita un transceptor externo |
| Modbus RTU (RS-485) | sí - en pines libres | necesita un transceptor externo |
| Modbus TCP | cliente y servidor |  |
| MQTT | sí | descubrimiento en Home Assistant |
| WEBview | sí | la página del operador en cualquier navegador |
| Pantalla / táctil (HMI) | no | la página del operador es WEBview |
| USB | USB-C |  |
| Alimentación | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Qué no está soportado

- Bluetooth - el ESP32 lo tiene, ctrl32 no lo usa.
- La ranura microSD - ctrl32 guarda el programa y las pantallas en la propia flash del chip.
- La entrada de batería funciona como característica propia de la placa; ctrl32 no lee el nivel de la batería.

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
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.es.md) - la primera generación
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.es.md) - con una alimentación PoE aislada

