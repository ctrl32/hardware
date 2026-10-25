---
title: 'Makerfabs MaTouch ESP32-P4 7": ejemplo All-in-one'
slug: all-in-one
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: La página del operador del ejemplo all-in-one para la Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# All-in-one

Un motor controlado desde la pantalla táctil, dos pulsadores y Home Assistant, con un manómetro, un ventilador según una temperatura Modbus RTU, un contador de potencia Modbus TCP, tramas CAN, una tendencia y las alarmas.

**Descarga:** [all-in-one.prj32](all-in-one.prj32) - ábrelo en el editor ctrl32 (**File → Open**).

## Qué hace

El programa es un pequeño control de máquina:

- **Start** llega desde un pulsador en GPIO47, desde **Start** en la
  pantalla o desde Home Assistant por MQTT; **Stop** desde un pulsador
  en GPIO48, desde **Stop** en la pantalla o cuando la presión sube por
  encima de la consigna que llega por **CAN** (trama 0x201).
- El enclavamiento acciona la salida del motor en **GPIO33**; un
  contador conserva el número de arranques tras un corte de corriente.
- La **presión** es una entrada analógica a través de un **ADS1115** en
  el bus I2C (0-10 V a través de un divisor 1:4, 0-10 bar) y sale por
  CAN cada 100 ms (trama 0x181).
- La **temperatura** llega de un sensor **Modbus RTU** (unidad 1,
  registro de entrada 1, 0,1 °C); un ventilador la sigue con histéresis.
- Un contador **Modbus TCP** da la potencia demandada.
- Tres **pantallas** en el cristal: el resumen, una tendencia y las
  alarmas; una página más sencilla en cualquier navegador (WEBview).

## El programa

![El programa en ladder del ejemplo](img/ladder.png)

## La página del operador

![La página del operador en la simulación](img/screen.png)

## Abrirlo y ejecutarlo

1. Abre `all-in-one.prj32` en el editor.
2. Cambia las direcciones (el dispositivo Modbus, el broker MQTT) por las de tu red.
3. Inicia la **simulación** (barra de herramientas) para probarlo en el PC, o descárgalo a la placa - consulta [Instalar el runtime](../../install.es.md).

## Qué deberías ver

El resumen aparece en el cristal. Pulsa **Start**: el LED del motor se
enciende y el contador de arranques sube. El indicador muestra la
presión, la pantalla Trend la dibuja junto con la temperatura, y en la
pantalla Alarms aparece una alarma cuando la presión pasa de 8 bar.


---

[← Proyectos de ejemplo](../README.es.md) | [Resumen](../../README.es.md)
