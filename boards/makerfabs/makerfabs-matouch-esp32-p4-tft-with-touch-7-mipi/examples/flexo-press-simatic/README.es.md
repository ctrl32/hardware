---
title: 'Makerfabs MaTouch ESP32-P4 7": ejemplo Flexo press on a SIMATIC'
slug: flexo-press-simatic
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/screen.png
image_alt: La página del operador del ejemplo flexo press on a simatic para la Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- example
---

# Flexo press on a SIMATIC

El HMI de una impresora flexográfica de ocho colores controlada por un SIMATIC S7-1200 - la impresora con su banda en movimiento, dieciséis servos de impresión, el registro, los secadores, los trabajos como recetas y el diagnóstico, por el protocolo S7.

**Descarga:** [flexo-press-simatic.prj32](flexo-press-simatic.prj32) - ábrelo en el editor ctrl32 (**File → Open**).

## Qué hace

Seis páginas en un panel industrial claro:

- **Overview** - la impresora como dibujo con la banda moviéndose
  sobre él, los testigos de sincronismo de los grupos, las temperaturas
  de los secadores, las tensiones de banda y las longitudes de las
  bobinas; START (con confirmación), STOP, JOG, RESET.
- **Sections** - los dieciséis servos de impresión: cilindros
  portaclichés y anilox, en sincronismo, fallo, velocidad, habilitado.
- **Register** - el error de registro de cada grupo y la corrección.
- **Heating** - las cámaras de secado y el secador de puente.
- **Jobs** - el trabajo como **receta** guardada en el panel: cargar,
  guardar, borrar.
- **Diagnostics** - las alarmas, el enlace con el PLC y una tendencia
  de velocidad y tensión.

El panel habla con un **SIMATIC S7-1200** por **+7** (el protocolo S7,
ISO-on-TCP): lee el bloque de estado DB100 del PLC cada 100 ms y
escribe sus consignas y órdenes en DB101 - no hace falta nada más en el
PLC. En **modo demo** (activado por defecto) el programa SIM hace
funcionar la impresora en el propio panel.

## Las pantallas

**Resumen**

![La página Overview: el dibujo de la impresora con la banda en movimiento, las tensiones y los secadores](img/overview.png)

**Grupos**

![La página Sections: dieciséis servos de impresión con su estado](img/sections.png)

**Trabajos**

![La página Jobs: el trabajo como receta guardada en el panel](img/jobs.png)

## Abrirlo y ejecutarlo

1. Abre `flexo-press-simatic.prj32` en el editor.
2. Ejecútalo tal cual en modo demo; con un PLC ajusta su dirección en la página +7 y crea los dos bloques de datos DB100 / DB101.
3. Inicia la **simulación** (barra de herramientas) para probarlo en el PC, o descárgalo a la placa - consulta [Instalar el runtime](../../install.es.md).

## Qué deberías ver

El resumen aparece en modo demo. Pulsa START y confirma: la línea
acelera, la banda se mueve sobre el dibujo y las tensiones se
estabilizan. Desactiva el modo demo en la página Diagnostics y ajusta
la dirección del PLC - el panel muestra entonces la impresora real.


---

[← Proyectos de ejemplo](../README.es.md) | [Resumen](../../README.es.md)
