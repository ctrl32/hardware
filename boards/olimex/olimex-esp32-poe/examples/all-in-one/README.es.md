---
title: 'Olimex ESP32-PoE: ejemplo All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/olimex-esp32-poe/
image: img/screen.png
image_alt: La página del operador del ejemplo all-in-one para la Olimex ESP32-PoE
tags:
- esp32
- ethernet
- poe
- olimex
- example
---

# All-in-one

Una bomba controlada desde el botón de la placa, la página del operador y Home Assistant, con una entrada de nivel, un temporizador de marcha, una alarma de nivel y un contador de energía Modbus TCP.

**Descarga:** [all-in-one.prj32](all-in-one.prj32) - ábrelo en el editor ctrl32 (**File → Open**).

## Qué hace

El programa es un pequeño control de bomba - la forma de la mayoría de
las máquinas:

- **Start** llega desde el botón de la placa (BUT1), desde el botón
  **Start** de la página del operador o desde Home Assistant por MQTT.
- **Stop** llega desde el botón **Stop**, desde un nivel bajo o al
  agotarse el tiempo de marcha - el enclavamiento apaga la salida en
  GPIO33.
- El **nivel** es una entrada analógica en GPIO35 (de 0 a 3,3 V
  escalado de 0 a 100 %). Por debajo del 10 % la bomba se detiene y
  salta una alarma; por encima del 15 % puede volver a arrancar
  (histéresis).
- El **tiempo de marcha** se ajusta en la página en minutos y se
  conserva tras un corte de corriente (una variable remanente).
- Un contador de energía **Modbus TCP** en la red da la tensión de red
  (registro 0, registros de entrada, unidad 1 en 192.168.1.60 -
  cámbiala por la de tu contador). Por encima de 253 V salta una
  alarma.
- **CAN** (un transceptor en GPIO4 / GPIO36) envía el nivel y el
  estado de la bomba en la trama 0x181 cada 100 ms y recibe una
  consigna en 0x201.
- **MQTT** publica el nivel, el estado de la bomba y la tensión en un
  broker de Home Assistant, que los encuentra por sí solo (discovery);
  la bomba se puede arrancar desde Home Assistant.
- **WEBview** sirve la página del operador - la bomba, el nivel, su
  tendencia y las alarmas - a cualquier navegador de la red.

## El programa

![El programa en ladder del ejemplo](img/ladder.png)

## La página del operador

![La página del operador en la simulación](img/screen.png)

## Abrirlo y ejecutarlo

1. Abre `all-in-one.prj32` en el editor.
2. Cambia las direcciones (el dispositivo Modbus, el broker MQTT) por las de tu red.
3. Inicia la **simulación** (barra de herramientas) para probarlo en el PC, o descárgalo a la placa - consulta [Instalar el runtime](../../install.es.md).

## Qué deberías ver

Con el potenciómetro subido, pulsa BUT1: el relé en GPIO33 se activa y
el LED de la bomba en la página se ilumina. Baja el potenciómetro por
debajo del 10 %: la bomba se detiene y la alarma aparece en la tabla.
En Home Assistant la placa aparece con su nivel, la bomba y la tensión.


---

[← Proyectos de ejemplo](../README.es.md) | [Resumen](../../README.es.md)
