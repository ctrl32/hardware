---
title: Olimex ESP32-S3-DevKit-Lipo
slug: olimex-esp32-s3-devkit-lipo
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-s3-devkit-lipo/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-S3-DevKit-Lipo con sus dos conectores USB-C y las tiras de pines
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Olimex ESP32-S3-DevKit-Lipo

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-S3](https://img.shields.io/badge/chip-ESP32--S3-334155) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a)

![Placa Olimex ESP32-S3-DevKit-Lipo con sus dos conectores USB-C y las tiras de pines](img/board-01.jpg)

La Olimex ESP32-S3-DevKit-Lipo es una placa ESP32-S3 de hardware libre con 8 MB de flash, 8 MB de PSRAM, Wi-Fi, dos puertos USB-C y un cargador Li-Po. El S3 con PSRAM es el chip de referencia de ctrl32: un programa ladder con el tamaño de programa completo, su página del operador en cualquier navegador (WEBview), Modbus TCP y MQTT con TLS - todo por Wi-Fi.

**Ideal para:**

- Un PLC Wi-Fi con margen para crecer - 512 variables, TLS hacia un broker en la nube
- Un control con batería que sigue funcionando durante un corte de corriente
- El desarrollo de una placa propia sobre el ESP32-S3

Página de la placa en el catálogo: [Olimex ESP32-S3-DevKit-Lipo](https://ctrl32.com/hardware/boards/olimex-esp32-s3-devkit-lipo/)

![Olimex ESP32-S3-DevKit-Lipo - mapa de pines: la función de cada GPIO en ctrl32](pinout/pinout.png)

## Qué puede hacer ctrl32 en esta placa

<!-- capabilities:start -->
| Característica | En esta placa | Notas |
|---|---|---|
| Chip | ESP32-S3 (ESP32-S3-WROOM-1-N8R8) |  |
| Memoria | 8 MB flash, 8 MB PSRAM |  |
| Tamaño del programa | 512 variables, 128 alarmas, 1024 bloques | el editor lo comprueba antes de una descarga |
| Entradas / salidas digitales | 21 GPIO libres | consulta el mapa de pines |
| Entradas analógicas | 9 en el chip (ADC1) | GPIO1, GPIO2, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10 |
| Ethernet | no |  |
| Wi-Fi | Wi-Fi 2.4 GHz |  |
| CAN (TWAI) | 1 - en pines libres | necesita un transceptor externo |
| Modbus RTU (RS-485) | sí - en pines libres | necesita un transceptor externo |
| Modbus TCP | cliente y servidor |  |
| MQTT | sí (también TLS) | descubrimiento en Home Assistant |
| WEBview | sí | la página del operador en cualquier navegador |
| Pantalla / táctil (HMI) | no | la página del operador es WEBview |
| USB | USB-C (CH340X USB-UART, Native USB) |  |
| Alimentación | 5 V USB, 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Qué no está soportado

- Bluetooth - el ESP32-S3 lo tiene, ctrl32 no lo usa.
- Las entradas de medida de batería y alimentación (GPIO5 / GPIO6) son pines libres en ctrl32, no un indicador de batería.

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
- [Olimex ESP32-DevKit-LiPo](../olimex-esp32-devkit-lipo/README.es.md) - la versión con el ESP32 clásico

