---
title: 'Olimex ESP32-P4-DevKit: hardware y cableado'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-DevKit - mapa de pines
tags:
- esp32-p4
- ethernet
- olimex
---

# Hardware y cableado

## Qué necesitas

- La Olimex ESP32-P4-DevKit.
- Un cable de datos USB-C - para la carga y para la alimentación (5 V).
- Un cable Ethernet y un puerto libre en tu red.
- Un PC con el [editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opcional, para el ejemplo all-in-one: el LED (GPIO2) está en la placa; un pulsador de GPIO20 a GND; un transceptor CAN de 3,3 V en GPIO5 / GPIO21 y un transceptor RS-485 en GPIO22 / GPIO23 / GPIO32 (DE).

## Alimentación

| Fuente | Dónde | Nota |
|---|---|---|
| USB 5 V | el conector USB-C | alimentación, programación y depuración |
| PoE | mediante la extensión PoE | opcional |

## Mapa de pines

![Olimex ESP32-P4-DevKit - mapa de pines](pinout/pinout.png)

| GPIO | Función en ctrl32 | Nota |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 7 | I2C SDA |  |
| 8 | I2C SCL |  |
| 20 | libre - E/S |  |
| 21 | libre - E/S |  |
| 22 | libre - E/S |  |
| 23 | libre - E/S |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 29 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 30 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 31 | Ethernet MDC (IP101GRI) | ⚠ usado por la placa |
| 32 | libre - E/S |  |
| 33 | libre - E/S |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 35 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 46 | libre - E/S |  |
| 47 | libre - E/S |  |
| 48 | libre - E/S |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 50 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ usado por la placa |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ usado por la placa |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Todos los GPIO están en las dos tiras de 20 pines. El ESP32-P4 no tiene
ninguna entrada analógica que use ctrl32: las señales analógicas van por
un ADC I2C (un ADS1115 en el conector pUEXT, I2C GPIO7 / GPIO8) o por un
módulo Modbus.

## Seguridad

- La placa no está pensada para funciones de seguridad. Una parada de
  emergencia, un interruptor de puerta o una cortina de luz se cablean en
  hardware, nunca a través de un programa.
- Los pines GPIO son de 3,3 V. Una señal de 24 V necesita un optoacoplador
  o un adaptador de nivel; la bobina de un relé necesita un driver (un
  módulo de relés ya lo lleva).

---

[← Resumen](README.es.md) | [Resumen](README.es.md) | [Instalar el runtime →](install.es.md)
