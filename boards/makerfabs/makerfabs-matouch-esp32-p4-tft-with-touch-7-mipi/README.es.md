---
title: Makerfabs MaTouch ESP32-P4 7"
slug: makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi
sidebar_position: 10
hardware: /hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/
image: img/board-01.jpg
image_alt: Placa Makerfabs MaTouch ESP32-P4 de 7 pulgadas con su pantalla táctil de 1024x600
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Makerfabs MaTouch ESP32-P4 7"

![tested with: ctrl32](https://img.shields.io/badge/tested%20with-ctrl32-0ea5e9) ![chip: ESP32-P4](https://img.shields.io/badge/chip-ESP32--P4-334155) ![Ethernet: yes](https://img.shields.io/badge/Ethernet-yes-16a34a) ![Wi-Fi: yes](https://img.shields.io/badge/Wi--Fi-yes-16a34a) ![CAN: 1](https://img.shields.io/badge/CAN-1-7c3aed) ![HMI: 1024x600](https://img.shields.io/badge/HMI-1024x600-0891b2)

![Placa Makerfabs MaTouch ESP32-P4 de 7 pulgadas con su pantalla táctil de 1024x600](img/board-01.jpg)

La Makerfabs MaTouch ESP32-P4 7" es un panel táctil completo en una sola placa: una pantalla MIPI de 1024 x 600 con táctil capacitivo, el ESP32-P4 de doble núcleo con 32 MB de PSRAM, Ethernet y Wi-Fi 6 a través de un ESP32-C6. Con ctrl32 es HMI y PLC en uno - las pantallas dibujadas en el editor funcionan en el cristal, un programa ladder corre a su lado y los mismos valores llegan a cualquier navegador (WEBview), a dispositivos Modbus, a CAN y a MQTT.

**Ideal para:**

- Un panel de operador en una máquina, con su propia lógica
- Un panel de control de casa inteligente o de edificio en la pared
- Una pasarela Modbus / CAN con pantalla

Página de la placa en el catálogo: [Makerfabs MaTouch ESP32-P4 7"](https://ctrl32.com/hardware/boards/makerfabs-matouch-esp32-p4-tft-with-touch-7-mipi/)

![Makerfabs MaTouch ESP32-P4 7" - mapa de pines: la función de cada GPIO en ctrl32](pinout/pinout.png)

## Qué puede hacer ctrl32 en esta placa

<!-- capabilities:start -->
| Característica | En esta placa | Notas |
|---|---|---|
| Chip | ESP32-P4 (ESP32-P4NRW32) |  |
| Memoria | 16 MB flash, 32 MB PSRAM |  |
| Tamaño del programa | 4096 variables, 512 alarmas, 512 bloques | el editor lo comprueba antes de una descarga |
| Entradas / salidas digitales | 12 GPIO libres | consulta el mapa de pines |
| Entradas analógicas | mediante un ADC I2C (ADS1115) |  |
| Ethernet | sí - IP101GRI |  |
| Wi-Fi | Wi-Fi 6 (2.4 GHz) |  |
| CAN (TWAI) | 1 | necesita un transceptor externo |
| Modbus RTU (RS-485) | sí | en pines libres, necesita un transceptor externo |
| Modbus TCP | cliente y servidor |  |
| MQTT | sí (también TLS) | descubrimiento en Home Assistant |
| WEBview | sí | la página del operador en cualquier navegador |
| Pantalla / táctil (HMI) | 7" 1024x600, GT911 |  |
| USB | USB-C (CH340K USB-UART, Native USB) |  |
| Alimentación | 5 V USB (4.0–5.25 V), 3.7 V Li-Po / Li-Ion |  |
<!-- capabilities:end -->

### Qué no está soportado

- La cámara (SC2336 en MIPI CSI) - ctrl32 ejecuta la visión artificial solo en el runtime Linux de 64 bits.
- El códec de audio, el micrófono y la salida de altavoz.
- El Bluetooth del ESP32-C6.
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
| [makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf](schematics/makerfabs-matouch_esp32-p4_tft_with_touch_7_v1.2.pdf) | MaTouch ESP32-P4 TFT with Touch 7“ V1.2 |
| [makerfabs-matouch-p4-7-display-datasheet.pdf](datasheets/makerfabs-matouch-p4-7-display-datasheet.pdf) | 7" 1024x600 MIPI display AML070JGI50 datasheet |
| [makerfabs-matouch-p4-es8311-datasheet.pdf](datasheets/makerfabs-matouch-p4-es8311-datasheet.pdf) | ES8311 audio codec datasheet |
| [esp32-p4-datasheet.pdf](datasheets/esp32-p4-datasheet.pdf) | ESP32-P4 datasheet (pre-release) |
| [makerfabs-matouch-p4-sc2336-camera-datasheet.pdf](datasheets/makerfabs-matouch-p4-sc2336-camera-datasheet.pdf) | SC2336 2 MP MIPI camera module datasheet |
| [NOTICE](https://github.com/ctrl32/hardware/blob/main/NOTICE.md) | de dónde vienen las fotos, los esquemas y los modelos |

## Siguientes pasos

- [Documentación de ctrl32](https://ctrl32.com/docs/) - el editor, los lenguajes, cada bloque
- [Descargar el editor](https://ctrl32.com/download/)
- [Todas las placas probadas](../../README.es.md)
- Makerfabs MaTouch Lite ESP32-S3 3.95" - la hermana pequeña
- [Panel de control de casa inteligente en la MaTouch ESP32-P4](https://ctrl32.com/examples/smart-home-control-panel-on-an-esp32-p4-7-touch-display/) - un ejemplo completo en la web

