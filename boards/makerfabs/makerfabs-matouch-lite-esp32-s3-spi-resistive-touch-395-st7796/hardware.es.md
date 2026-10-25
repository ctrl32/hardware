---
title: 'Makerfabs MaTouch Lite ESP32-S3 3.95": hardware y cableado'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa de pines
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Hardware y cableado

## Qué necesitas

- La Makerfabs MaTouch Lite ESP32-S3 3,95" (ST7796).
- Un cable de datos USB-C - para la carga y para la alimentación.
- El nombre y la contraseña de tu Wi-Fi de 2,4 GHz.
- Un PC con el [editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opcional, para el ejemplo all-in-one: un módulo de relés o un LED en GPIO4, un potenciómetro (10 k) entre 3,3 V y GND con el cursor en GPIO5 (los conectores JST) y un transceptor CAN de 3,3 V (p. ej. SN65HVD230) en GPIO6 / GPIO7.

## Alimentación

| Fuente | Dónde | Nota |
|---|---|---|
| USB 5 V | el conector USB-C | alimentación y programación |
| Batería Li-Po | el conector de batería | 3,7 V |

## Mapa de pines

![Makerfabs MaTouch Lite ESP32-S3 3.95" - mapa de pines](pinout/pinout.png)

| GPIO | Función en ctrl32 | Nota |
|---|---|---|
| 0 | BOOT BTN | ⚠ pin de strapping |
| 1 | TFT RST |  |
| 2 | SD CMD | ⚠  |
| 4 | libre - E/S | ADC1 |
| 5 | libre - E/S | ADC1 |
| 6 | libre - E/S | ADC1 |
| 7 | libre - E/S | ADC1 |
| 13 | TFT MOSI |  |
| 14 | TFT SCLK |  |
| 15 | TFT CS |  |
| 21 | TFT DC |  |
| 38 | TOUCH SDA |  |
| 39 | TOUCH SCL |  |
| 40 | TOUCH INT |  |
| 41 | SD DO | ⚠  |
| 42 | SD SCLK | ⚠  |
| 48 | TFT BL |  |

Los dos conectores **JST** llevan los cuatro pines libres (GPIO4 a GPIO7)
- pocos, así que el ejemplo pone en ellos la salida, la entrada analógica
y CAN; más E/S van por Modbus TCP o por chips I2C. La pantalla, el
controlador táctil y la ranura microSD ocupan el resto de los pines.

## Seguridad

- La placa no está pensada para funciones de seguridad. Una parada de
  emergencia, un interruptor de puerta o una cortina de luz se cablean en
  hardware, nunca a través de un programa ni de una pantalla táctil.
- Los pines GPIO son de 3,3 V. La bobina de un relé necesita un driver (un módulo de relés ya lo lleva).

---

[← Resumen](README.es.md) | [Resumen](README.es.md) | [Instalar el runtime →](install.es.md)
