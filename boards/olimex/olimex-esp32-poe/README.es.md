---
title: Olimex ESP32-PoE
slug: olimex-esp32-poe
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-PoE vista desde arriba, con el conector Ethernet y el conector USB
tags:
- esp32
- ethernet
- poe
- olimex
---

# Olimex ESP32-PoE

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Placa Olimex ESP32-PoE vista desde arriba, con el conector Ethernet y el conector USB](img/board-01.jpg)

La Olimex ESP32-PoE es una placa ESP32 de hardware libre con Ethernet y Power over Ethernet: un solo cable de red la alimenta y lleva su enlace. Con ctrl32 se convierte en un PLC compacto para un armario o una caja de pared - un programa ladder en el chip, su página del operador servida a cualquier navegador de la red (WEBview), Modbus TCP hacia contadores y módulos de E/S, y MQTT hacia Home Assistant o cualquier broker.

**Ideal para:**

- Un pequeño PLC en un armario, alimentado desde un switch PoE
- Una pasarela Modbus TCP que lee contadores y los publica por MQTT
- Domótica - una habitación o una sala de calderas con un solo cable

Página de la placa en el catálogo: [Olimex ESP32-PoE](https://ctrl32.com/hardware/boards/olimex-esp32-poe/)

![Olimex ESP32-PoE - mapa de pines: la función de cada GPIO en ctrl32](pinout/pinout.png)

## Qué puede hacer ctrl32 en esta placa

<!-- capabilities:start -->
| Característica | En esta placa | Notas |
|---|---|---|
| Chip | ESP32 (ESP32-WROOM-32E-N4) |  |
| Memoria | 4 MB flash |  |
| Tamaño del programa | 128 variables, 32 alarmas, 128 bloques | el editor lo comprueba antes de una descarga |
| Entradas / salidas digitales | 6 GPIO libres | 3 de ellos solo entradas |
| Entradas analógicas | 4 en el chip (ADC1) | GPIO33, GPIO34, GPIO35, GPIO36 |
| Ethernet | sí - LAN8710A |  |
| Power over Ethernet | IEEE 802.3af |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - en pines libres | necesita un transceptor externo |
| Modbus RTU (RS-485) | sí - en pines libres | necesita un transceptor externo |
| Modbus TCP | cliente y servidor |  |
| MQTT | sí | descubrimiento en Home Assistant |
| WEBview | sí | la página del operador en cualquier navegador |
| Pantalla / táctil (HMI) | no | la página del operador es WEBview |
| USB | Micro-USB (CH340T USB-UART) |  |
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

| Archivo | Qué |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | el mapa de pines, en vectorial (también en [PNG](pinout/pinout.png)) |
| [olimex-esp32-poe-schematic.pdf](schematics/olimex-esp32-poe-schematic.pdf) | ESP32-PoE schematic Rev M2 |
| [esp32-poe-revm2.zip](schematics/esp32-poe-revm2.zip) | KiCad project |
| [olimex-esp32-poe-user-manual.pdf](datasheets/olimex-esp32-poe-user-manual.pdf) | ESP32-PoE user manual |
| [olimex-esp32-poe.zip](3d/olimex-esp32-poe.zip) | Modelo 3D (STEP, comprimido en zip) |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | de dónde vienen las fotos, los esquemas y los modelos |

## Siguientes pasos

- [Documentación de ctrl32](https://ctrl32.com/docs/) - el editor, los lenguajes, cada bloque
- [Descargar el editor](https://ctrl32.com/download/)
- [Todas las placas probadas](../../README.es.md)
- [Olimex ESP32-PoE-ISO](../olimex-esp32-poe-iso/README.es.md) - la misma placa con una alimentación PoE aislada
- [Olimex ESP32-POE2](../olimex-esp32-poe2/README.es.md) - la siguiente generación

