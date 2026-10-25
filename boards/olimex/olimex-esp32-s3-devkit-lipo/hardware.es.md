---
title: 'Olimex ESP32-S3-DevKit-Lipo: hardware y cableado'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-S3-DevKit-Lipo - mapa de pines
tags:
- esp32-s3
- wifi
- psram
- battery
- olimex
---

# Hardware y cableado

## Qué necesitas

- La Olimex ESP32-S3-DevKit-Lipo.
- Un cable de datos USB-C - en el conector marcado UART (el CH340X) para la carga.
- El nombre y la contraseña de tu Wi-Fi de 2,4 GHz.
- Un PC con el [editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opcional, para el ejemplo all-in-one: el botón Boot/User (GPIO0) y el LED (GPIO38) están en la placa; un potenciómetro (10 k) entre 3,3 V y GND con el cursor en GPIO1; un transceptor CAN de 3,3 V en GPIO10 / GPIO17 y un transceptor RS-485 en GPIO18 / GPIO2 / GPIO4 (DE).

## Alimentación

| Fuente | Dónde | Nota |
|---|---|---|
| USB 5 V | cualquiera de los dos conectores USB-C | alimentación y programación |
| Batería Li-Po | el conector de batería | se carga en la placa, conmutación automática |

## Mapa de pines

![Olimex ESP32-S3-DevKit-Lipo - mapa de pines](pinout/pinout.png)

| GPIO | Función en ctrl32 | Nota |
|---|---|---|
| 0 | libre - el botón de la placa | ⚠ pin de strapping |
| 1 | libre - E/S | ADC1 |
| 2 | libre - E/S | ADC1 |
| 4 | libre - E/S | ADC1 |
| 5 | free (PWR SENSE line) | ADC1 |
| 6 | free (BAT SENSE line) | ADC1 |
| 7 | libre - E/S | ADC1 |
| 8 | libre - E/S | ADC1 |
| 9 | libre - E/S | ADC1 |
| 10 | free (SPI CS line) | ADC1 |
| 11 | SPI MOSI |  |
| 12 | SPI SCLK |  |
| 13 | SPI MISO |  |
| 14 | libre - E/S |  |
| 15 | libre - E/S |  |
| 16 | libre - E/S |  |
| 17 | free (UART TX line) |  |
| 18 | free (UART RX line) |  |
| 21 | libre - E/S |  |
| 38 | free (LED0 line) |  |
| 39 | libre - E/S |  |
| 40 | libre - E/S |  |
| 41 | libre - E/S |  |
| 42 | libre - E/S |  |
| 47 | I2C SCL |  |
| 48 | I2C SDA |  |

Las tiras llevan los GPIO libres; ADC1 (las entradas analógicas que usa
ctrl32) está en GPIO1 a GPIO10. GPIO0 es el botón Boot/User - una entrada
en el programa, y mantenido pulsado al encender arranca el modo de
descarga del chip. El conector pUEXT lleva I2C (GPIO48 / GPIO47) y SPI.

## Seguridad

- La placa no está pensada para funciones de seguridad. Una parada de
  emergencia, un interruptor de puerta o una cortina de luz se cablean en
  hardware, nunca a través de un programa.
- Los pines GPIO son de 3,3 V. Una señal de 24 V necesita un optoacoplador
  o un adaptador de nivel; la bobina de un relé necesita un driver (un
  módulo de relés ya lo lleva).

---

[← Resumen](README.es.md) | [Resumen](README.es.md) | [Instalar el runtime →](install.es.md)
