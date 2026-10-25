---
title: 'Makerfabs MaTouch ESP32-P4 7": ejemplo Home dashboard'
slug: home-dashboard
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.jpg
image_alt: La página del operador del ejemplo home dashboard para la Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Home dashboard

Un panel de control para toda la casa en un estilo oscuro de cristal esmerilado - calefacción por habitación, energía con fotovoltaica y batería, luces, el garaje y el tiempo - con una casa simulada detrás.

**Descarga:** [home-dashboard.prj32](home-dashboard.prj32) - ábrelo en el editor ctrl32 (**File → Open**).

## Qué hace

Seis pantallas sobre fotografías de la casa, cada una un conjunto de
tarjetas de cristal esmerilado:

- **Home** - la hora, el tiempo, las habitaciones, la alarma y las
  escenas.
- **Weather** - hoy y los próximos días.
- **Climate** - seis habitaciones, cada una con su temperatura, su
  consigna y la calefacción; la bomba de calor y el depósito de agua
  caliente.
- **Energy** - la producción fotovoltaica, el consumo de la casa, la
  batería y la red, los kWh del día.
- **Lights** - las luces de las habitaciones y sus escenas.
- **Access** - la puerta del garaje, el cargador del coche, la alarma.

El programa **SIM** es la casa: la temperatura exterior sigue el día,
la producción fotovoltaica el sol, el consumo tiene sus picos de mañana
y de tarde, las habitaciones se calientan con histéresis hasta sus
consignas. Sustituye sus variables por tus dispositivos Modbus, MQTT o
CAN para controlar una casa real.

## Las pantallas

**Inicio**

![La pantalla Home del panel: hora, tiempo, habitaciones, alarma y escenas](img/home.jpg)

**Clima**

![La pantalla Climate: seis habitaciones con sus temperaturas y consignas](img/climate.png)

**Energía**

![La pantalla Energy: fotovoltaica, consumo de la casa, batería y red](img/energy.jpg)

## Abrirlo y ejecutarlo

1. Abre `home-dashboard.prj32` en el editor.
2. Ejecútalo tal cual - la casa está simulada; para una casa real sustituye las variables del programa SIM por tus dispositivos.
3. Inicia la **simulación** (barra de herramientas) para probarlo en el PC, o descárgalo a la placa - consulta [Instalar el runtime](../../install.es.md).

## Qué deberías ver

La pantalla Home aparece con la hora, el tiempo y las habitaciones; los
valores se mueven a medida que avanza el día simulado. Un toque en la
consigna de una habitación la cambia, y la habitación se calienta hasta
ella.


---

[← Proyectos de ejemplo](../README.es.md) | [Resumen](../../README.es.md)
