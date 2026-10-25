---
title: 'Olimex ESP32-GATEWAY: ejemplo All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-gateway/
image: img/screen.png
image_alt: La página del operador del ejemplo all-in-one para la Olimex ESP32-GATEWAY
tags:
- esp32
- ethernet
- gateway
- olimex
- example
---

# All-in-one

Una salida de motor con marcha / paro, un temporizador de marcha, un contador Modbus TCP, MQTT y la página del operador en un navegador.

**Descarga:** [all-in-one.prj32](all-in-one.prj32) - ábrelo en el editor ctrl32 (**File → Open**).

## Qué hace

El programa es un pequeño control de máquina - la forma de la mayoría de las máquinas:

- **Start** llega desde el botón en GPIO34, desde **Start** en la página del operador o desde Home Assistant por MQTT.
- **Stop** llega desde **Stop**, desde un nivel bajo o al agotarse el tiempo de marcha - el enclavamiento apaga la salida en **GPIO33**.
- El **tiempo de marcha** se ajusta en minutos y se conserva tras un corte de corriente.
- El **nivel** es una variable que se ajusta en la página (a la placa no le queda ningún pin analógico libre).
- Un contador de energía **Modbus TCP** en la red da la potencia demandada (192.168.1.60 - cámbiala por la de tu contador).
- **MQTT** publica los valores en un broker de Home Assistant, que los encuentra por sí solo; la salida también se puede arrancar desde Home Assistant.
- **WEBview** sirve la página del operador a cualquier navegador de la red.

## El programa

![El programa en ladder del ejemplo](img/ladder.png)

## La página del operador

![La página del operador en la simulación](img/screen.png)

## Abrirlo y ejecutarlo

1. Abre `all-in-one.prj32` en el editor.
2. Cambia las direcciones (el dispositivo Modbus, el broker MQTT) por las de tu red.
3. Inicia la **simulación** (barra de herramientas) para probarlo en el PC, o descárgalo a la placa - consulta [Instalar el runtime](../../install.es.md).

## Qué deberías ver

Pulsa el botón en GPIO34: la salida en GPIO33 se enciende y su LED en la página se ilumina. Pasado el tiempo de marcha se apaga sola. En Home Assistant la placa aparece con sus valores.


---

[← Proyectos de ejemplo](../README.es.md) | [Resumen](../../README.es.md)
