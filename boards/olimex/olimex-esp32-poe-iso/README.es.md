---
title: Olimex ESP32-PoE-ISO
slug: olimex-esp32-poe-iso
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe-iso/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-PoE-ISO con el conector Ethernet y la alimentación PoE aislada
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Olimex ESP32-PoE-ISO

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32](https://img.shields.io/badge/chip-ESP32-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Placa Olimex ESP32-PoE-ISO con el conector Ethernet y la alimentación PoE aislada](img/board-01.jpg)

La Olimex ESP32-PoE-ISO es la ESP32-PoE con una alimentación Power over Ethernet con aislamiento galvánico: un solo cable de red la alimenta y lleva su enlace, y un PC puede seguir conectado por USB mientras la placa funciona con PoE. Con ctrl32 es un PLC compacto para un armario - un programa ladder en el chip, su página del operador en cualquier navegador (WEBview), Modbus TCP hacia contadores y módulos de E/S, y MQTT hacia Home Assistant.

**Ideal para:**

- Un pequeño PLC en un armario, alimentado desde un switch PoE
- Una pasarela Modbus TCP que lee contadores y los publica por MQTT
- Domótica - una habitación o una sala de calderas con un solo cable

Página de la placa en el catálogo: [Olimex ESP32-PoE-ISO](https://ctrl32.com/hardware/boards/olimex-esp32-poe-iso/)

![Olimex ESP32-PoE-ISO - mapa de pines: la función de cada GPIO en ctrl32](pinout/pinout.png)

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

-

## Siguientes pasos

- [Documentación de ctrl32](https://ctrl32.com/docs/) - el editor, los lenguajes, cada bloque
- [Descargar el editor](https://ctrl32.com/download/)
- [Todas las placas probadas](../../README.es.md)
- [Olimex ESP32-PoE](../olimex-esp32-poe/README.es.md) - la misma placa sin la alimentación aislada
- [Olimex ESP32-POE2](../olimex-esp32-poe2/README.es.md) - la siguiente generación

