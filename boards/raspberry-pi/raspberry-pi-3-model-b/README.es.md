---
title: Raspberry Pi 3 Model B+
slug: raspberry-pi-3-model-b
sidebar_position: 10
hardware: /hardware/boards/raspberry-pi-3-model-b/
image: img/board-01.jpg
image_alt: Placa Raspberry Pi 3 Model B+ vista desde arriba
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Raspberry Pi 3 Model B+

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: Linux](https://img.shields.io/badge/chip-Linux-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed)

![Placa Raspberry Pi 3 Model B+ vista desde arriba](img/board-01.jpg)

La Raspberry Pi 3 Model B+ ejecuta el runtime Linux de ctrl32: un programa grande, un HMI en el monitor HDMI, un servidor OPC UA para SCADA, CAN y RS-485 mediante HAT o adaptadores USB, Modbus y MQTT. Con 1 GB de memoria y un Cortex-A53 de cuatro núcleos es adecuada para un control de línea o una pasarela; la visión artificial con una cámara pide una Raspberry Pi 4 o 5.

**Ideal para:**

- Un control de línea con un HMI en un monitor HDMI y OPC UA hacia SCADA
- Un maestro EtherCAT para servoaccionamientos
- Una pasarela entre Modbus, CAN, OPC UA y MQTT

Página de la placa en el catálogo: [Raspberry Pi 3 Model B+](https://ctrl32.com/hardware/boards/raspberry-pi-3-model-b/)

![Raspberry Pi 3 Model B+ - mapa de pines: la función de cada GPIO en ctrl32](pinout/pinout.png)

## Qué puede hacer ctrl32 en esta placa

<!-- capabilities:start -->
| Característica | En esta placa | Notas |
|---|---|---|
| Chip | Linux |  |
| Tamaño del programa | 20480 variables, 4096 alarmas, 40960 bloques | el editor lo comprueba antes de una descarga |
| Entradas / salidas digitales | mediante módulos de E/S | Modbus, CANopen, EtherCAT |
| Ethernet | sí |  |
| Wi-Fi | Wi-Fi 5 (2.4 + 5 GHz) |  |
| CAN | mediante un HAT CAN o un adaptador USB | SocketCAN, hasta 4 buses |
| Modbus RTU (RS-485) | sí | un adaptador USB o un HAT |
| Modbus TCP | cliente y servidor |  |
| MQTT | sí (también TLS) | descubrimiento en Home Assistant |
| WEBview | sí | la página del operador en cualquier navegador |
| Servidor OPC UA | sí |  |
| EtherCAT master | sí | en un segundo puerto Ethernet |
| Pantalla (HMI) | HDMI o un panel DSI | o sin pantalla con WEBview |
| USB | Micro-USB |  |
| Alimentación | 5 V USB |  |
<!-- capabilities:end -->

### Qué no está soportado

- La tira GPIO de 40 pines como E/S del programa - las entradas y salidas van por módulos de E/S (Modbus RTU / TCP, CANopen, EtherCAT); la tira lleva los buses de los HAT.
- Bluetooth.
- Un entorno de escritorio - el runtime dibuja la pantalla por sí mismo; Raspberry Pi OS Lite es el sistema que necesita.

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
- [Raspberry Pi 5](../raspberry-pi-5/README.es.md)
- [Raspberry Pi 4 Model B](../raspberry-pi-4-model-b/README.es.md)
- [El runtime Linux](https://ctrl32.com/docs/linux-runtime/) - qué hace y sus límites

