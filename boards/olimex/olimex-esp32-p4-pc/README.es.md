---
title: Olimex ESP32-P4-PC
slug: olimex-esp32-p4-pc
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-p4-pc/
image: img/board-01.jpg
image_alt: Placa Olimex ESP32-P4-PC con el conector Ethernet, los puertos USB y el conector HDMI
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Olimex ESP32-P4-PC

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a)

![Placa Olimex ESP32-P4-PC con el conector Ethernet, los puertos USB y el conector HDMI](img/board-01.jpg)

La Olimex ESP32-P4-PC es un pequeño ordenador sobre el ESP32-P4 - doble núcleo a 400 MHz con 32 MB de PSRAM - con Ethernet de 100 Mb, cuatro puertos USB host, HDMI, audio y una batería Li-Po que la mantiene en marcha durante un corte de corriente. Con ctrl32 es un control cableado con el programa más grande que ejecuta un ESP32 - 4096 variables - su página del operador en cualquier navegador (WEBview), Modbus TCP, MQTT con TLS, y CAN o RS-485 en los pines libres de su tira.

**Ideal para:**

- Un PLC cableado que aguanta un corte de corriente con su propia batería
- Una pasarela con mucha lógica entre Modbus TCP, CAN y MQTT
- Un control en una caja, alimentado por PoE (con la extensión)

Página de la placa en el catálogo: [Olimex ESP32-P4-PC](https://ctrl32.com/hardware/boards/olimex-esp32-p4-pc/)

![Olimex ESP32-P4-PC - mapa de pines: la función de cada GPIO en ctrl32](pinout/pinout.png)

## Qué puede hacer ctrl32 en esta placa

<!-- capabilities:start -->
| Característica | En esta placa | Notas |
|---|---|---|
| Chip | ESP32-P4 (ESP32-P4NRW32) |  |
| Memoria | 16 MB flash, 32 MB PSRAM |  |
| Tamaño del programa | 4096 variables, 512 alarmas, 1024 bloques | el editor lo comprueba antes de una descarga |
| Entradas / salidas digitales | 15 GPIO libres | consulta el mapa de pines |
| Entradas analógicas | mediante un ADC I2C (ADS1115) |  |
| Ethernet | sí - IP101GRI |  |
| Wi-Fi | no |  |
| CAN (TWAI) | 1 - en pines libres | necesita un transceptor externo |
| Modbus RTU (RS-485) | sí - en pines libres | necesita un transceptor externo |
| Modbus TCP | cliente y servidor |  |
| MQTT | sí (también TLS) | descubrimiento en Home Assistant |
| WEBview | sí | la página del operador en cualquier navegador |
| Pantalla / táctil (HMI) | no | la página del operador es WEBview |
| USB | USB-C (Native USB) |  |
| Alimentación | 5 V USB, 3.7 V Li-Po / Li-Ion, PoE |  |
<!-- capabilities:end -->

### Qué no está soportado

- La salida HDMI y los conectores MIPI DSI / CSI - esta placa funciona sin pantalla en ctrl32 (la página del operador es WEBview).
- Los puertos USB host y la salida de audio.
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

| Archivo | Qué |
|---|---|
| [pinout/pinout.svg](pinout/pinout.svg) | el mapa de pines, en vectorial (también en [PNG](pinout/pinout.png)) |
| [olimex-esp32-p4-pc-schematic.pdf](schematics/olimex-esp32-p4-pc-schematic.pdf) | ESP32-P4-PC schematic Rev C |
| [esp32-p4-pc-rev-c-kicad.zip](schematics/esp32-p4-pc-rev-c-kicad.zip) | KiCad project |
| [olimex-esp32-p4-pc-user-manual.pdf](datasheets/olimex-esp32-p4-pc-user-manual.pdf) | ESP32-P4-PC user manual |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | de dónde vienen las fotos, los esquemas y los modelos |

## Siguientes pasos

- [Documentación de ctrl32](https://ctrl32.com/docs/) - el editor, los lenguajes, cada bloque
- [Descargar el editor](https://ctrl32.com/download/)
- [Todas las placas probadas](../../README.es.md)
- [Olimex ESP32-P4-DevKit](../olimex-esp32-p4-devkit/README.es.md) - el mismo ESP32-P4 en una placa más pequeña

