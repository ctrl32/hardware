---
title: 'Makerfabs MaTouch ESP32-P4 7": ejemplo Car cockpit'
slug: car-cockpit
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: La página del operador del ejemplo car cockpit para la Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Car cockpit

Un cuadro de instrumentos en un bus de vehículo J1939 - velocímetro y cuentarrevoluciones, marcha, combustible, refrigerante, los testigos de aviso, las unidades de control del bus, el código de fallo activo en palabras y los ajustes del conductor.

**Descarga:** [car-cockpit.prj32](car-cockpit.prj32) - ábrelo en el editor ctrl32 (**File → Open**).

## Qué hace

Cinco pantallas en el cristal de 7":

- **Cockpit** - velocímetro y cuentarrevoluciones, la marcha,
  combustible, refrigerante y batería, el cuentakilómetros y el parcial,
  el reloj, los intermitentes y los testigos de aviso.
- **Engine** - los valores del motor en detalle.
- **Bus** - la red **J1939**: el nodo del panel, el motor, la
  transmisión y los frenos y si responden, los testigos DM1, cada señal
  con su grupo de parámetros.
- **Faults** - la lista de alarmas y el código de fallo activo del
  motor (SPN / FMI / recuento) con su significado en palabras.
- **Settings** - modo demo, unidades, el aviso de velocidad, la zona
  roja, los avisos de refrigerante y combustible, el intervalo de
  mantenimiento.

La comunicación es **SAE J1939** en el CAN de la placa (un transceptor
de 3,3 V en GPIO47 / GPIO48, 250 kbit/s): el motor, la transmisión y
los frenos emiten sus grupos de parámetros y el panel los lee - no hace
falta ningún programa para que llegue un valor. En **modo demo**
(activado por defecto) el programa SIM recorre un ciclo: arranca,
cambia de marcha, circula, frena, se detiene - y de vez en cuando un
fallo.

## Las pantallas

**Cockpit**

![La pantalla Cockpit: velocímetro y cuentarrevoluciones, marcha, combustible, refrigerante y los testigos de aviso](img/cockpit.png)

**Bus**

![La pantalla Bus con la red J1939: las unidades de control y las señales que lee el panel](img/bus.png)

**Fallos**

![La pantalla Faults: la lista de alarmas y el código de fallo activo](img/faults.png)

## Abrirlo y ejecutarlo

1. Abre `car-cockpit.prj32` en el editor.
2. Ejecútalo tal cual en modo demo; en un vehículo conecta el transceptor CAN a GPIO47 / GPIO48 y desactiva el modo demo en la pantalla Settings.
3. Inicia la **simulación** (barra de herramientas) para probarlo en el PC, o descárgalo a la placa - consulta [Instalar el runtime](../../install.es.md).

## Qué deberías ver

El cuadro aparece en modo demo: las agujas recorren el ciclo de
conducción, la marcha cambia, los intermitentes parpadean. Desactiva el
modo demo en la pantalla Settings y conecta el bus - los indicadores
muestran entonces el vehículo.


---

[← Proyectos de ejemplo](../README.es.md) | [Resumen](../../README.es.md)
