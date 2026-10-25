---
title: Makerfabs MaTouch Lite ESP32-S3 3.95"
slug: makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/
image: img/board-01.jpg
image_alt: Placa Makerfabs MaTouch Lite ESP32-S3 con su pantalla táctil de 3,95 pulgadas
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Makerfabs MaTouch Lite ESP32-S3 3.95"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 320x480](https://img.shields.io/badge/HMI-320x480-0891b2)

![Placa Makerfabs MaTouch Lite ESP32-S3 con su pantalla táctil de 3,95 pulgadas](img/board-01.jpg)

La Makerfabs MaTouch Lite es un panel táctil económico: una pantalla de 3,95" de 320 x 480 con táctil resistivo sobre un ESP32-S3 con PSRAM y Wi-Fi. Con ctrl32 es HMI y PLC en uno - pantallas dibujadas en el editor en el cristal, un programa ladder a su lado, los mismos valores en cualquier navegador (WEBview), Modbus TCP, CAN y MQTT. El táctil resistivo funciona con guantes.

**Ideal para:**

- Un pequeño panel de operador en una máquina, manejado con guantes
- Un termostato de pared o un controlador de habitación
- Una pantalla CAN para un vehículo o un variador

Página de la placa en el catálogo: [Makerfabs MaTouch Lite ESP32-S3 3.95"](https://ctrl32.com/hardware/boards/makerfabs-matouch-lite-esp32-s3-spi-resistive-touch-395-st7796/)

![Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa de pines: la función de cada GPIO en ctrl32](pinout/pinout.png)

## Qué puede hacer ctrl32 en esta placa

<!-- capabilities:start -->
| Característica | En esta placa | Notas |
|---|---|---|
| Chip | ESP32-S3 (esp32s3_wroom_1_n16r8) |  |
| Memoria | 16 MB flash, 8 MB PSRAM |  |
| Tamaño del programa | 512 variables, 128 alarmas, 512 bloques | el editor lo comprueba antes de una descarga |
| Entradas / salidas digitales | 4 GPIO libres | consulta el mapa de pines |
| Entradas analógicas | 4 en el chip (ADC1) | GPIO4, GPIO5, GPIO6, GPIO7 |
| Ethernet | no |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 | necesita un transceptor externo |
| Modbus RTU (RS-485) | sí | en pines libres, necesita un transceptor externo |
| Modbus TCP | cliente y servidor |  |
| MQTT | sí (también TLS) | descubrimiento en Home Assistant |
| WEBview | sí | la página del operador en cualquier navegador |
| Pantalla / táctil (HMI) | 3.95" 320x480, NS2009 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Alimentación | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Qué no está soportado

- Bluetooth.
- La ranura microSD - ctrl32 guarda el programa y las pantallas en la flash de la placa.

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
- [Makerfabs MaTouch ESP32-P4 7"](../makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/README.es.md) - la hermana grande

