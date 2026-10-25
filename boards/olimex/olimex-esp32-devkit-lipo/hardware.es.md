---
title: 'Olimex ESP32-DevKit-LiPo: hardware y cableado'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-DevKit-LiPo - mapa de pines
tags:
- esp32
- wifi
- battery
- olimex
---

# Hardware y cableado

## Qué necesitas

- La Olimex ESP32-DevKit-LiPo.
- Un cable de datos micro-USB - para la carga y para la alimentación (5 V).
- El nombre y la contraseña de tu Wi-Fi de 2,4 GHz.
- Un PC con el [editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opcional, para el ejemplo all-in-one: un pulsador de GPIO13 a GND; un módulo de relés o un LED con resistencia en GPIO4; un potenciómetro (10 k) entre 3,3 V y GND con el cursor en GPIO32; un transceptor CAN de 3,3 V en GPIO14 / GPIO34 y un transceptor RS-485 en GPIO16 / GPIO36 / GPIO17 (DE); una celda Li-Po como respaldo.

## Alimentación

| Fuente | Dónde | Nota |
|---|---|---|
| USB 5 V | el conector micro-USB | alimentación y programación |
| Batería Li-Po | el conector de batería | se carga en la placa, toma el relevo cuando falla el USB |

## Mapa de pines

![Olimex ESP32-DevKit-LiPo - mapa de pines](pinout/pinout.png)

| GPIO | Función en ctrl32 | Nota |
|---|---|---|
| 4 | libre - E/S |  |
| 6 | flash SPI del módulo | ⚠ usado por la placa |
| 7 | flash SPI del módulo | ⚠ usado por la placa |
| 8 | flash SPI del módulo | ⚠ usado por la placa |
| 9 | flash SPI del módulo | ⚠ usado por la placa |
| 10 | flash SPI del módulo | ⚠ usado por la placa |
| 11 | flash SPI del módulo | ⚠ usado por la placa |
| 13 | libre - E/S |  |
| 14 | libre - E/S |  |
| 16 | libre - E/S |  |
| 17 | libre - E/S |  |
| 18 | libre - E/S |  |
| 19 | libre - E/S |  |
| 21 | libre - E/S |  |
| 22 | libre - E/S |  |
| 23 | libre - E/S |  |
| 25 | libre - E/S |  |
| 26 | libre - E/S |  |
| 27 | libre - E/S |  |
| 32 | libre - E/S | ADC1 |
| 33 | libre - E/S | ADC1 |
| 34 | libre - entrada | ⚠ solo entrada, ADC1 |
| 35 | free (BAT SENSE line) | ⚠ solo entrada, ADC1 |
| 36 | libre - entrada | ⚠ solo entrada, ADC1 |
| 39 | free (PWR SENSE line) | ⚠ solo entrada, ADC1 |

Las dos tiras de pines llevan los GPIO libres del módulo. GPIO34 a GPIO39
son solo entradas; GPIO0, 2, 12 y 15 son pines de strapping - déjalos
para entradas o pruébalos antes de usarlos. Un pulsador a GND no necesita
resistencia: ctrl32 lo lee invertido con el pull-up del chip.

## Seguridad

- La placa no está pensada para funciones de seguridad. Una parada de
  emergencia, un interruptor de puerta o una cortina de luz se cablean en
  hardware, nunca a través de un programa.
- Los pines GPIO son de 3,3 V. Una señal de 24 V necesita un optoacoplador
  o un adaptador de nivel; la bobina de un relé necesita un driver (un
  módulo de relés ya lo lleva).

---

[← Resumen](README.es.md) | [Resumen](README.es.md) | [Instalar el runtime →](install.es.md)
