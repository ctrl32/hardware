---
title: 'Olimex ESP32-P4-PC: hardware y cableado'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-P4-PC - mapa de pines
tags:
- esp32-p4
- ethernet
- ups
- olimex
---

# Hardware y cableado

## Qué necesitas

- La Olimex ESP32-P4-PC.
- Un cable de datos USB-C - para la carga y para la alimentación (5 V).
- Un cable Ethernet y un puerto libre en tu red.
- Un PC con el [editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opcional: una celda Li-Po para el respaldo por batería; para el ejemplo all-in-one el LED de usuario (GPIO2) está en la placa y un pulsador va de GPIO14 a GND (EXT1); un transceptor CAN de 3,3 V en GPIO5 / GPIO15 y un transceptor RS-485 en GPIO16 / GPIO17 / GPIO18 (DE).

## Alimentación

| Fuente | Dónde | Nota |
|---|---|---|
| USB 5 V | el conector USB-C | alimentación, programación y depuración |
| Batería Li-Po | el conector de batería | se carga en la placa; toma el relevo cuando falla la alimentación (SAI) |
| PoE | mediante la extensión PoE | opcional |

## Mapa de pines

![Olimex ESP32-P4-PC - mapa de pines](pinout/pinout.png)

| GPIO | Función en ctrl32 | Nota |
|---|---|---|
| 2 | free (LED0 line) |  |
| 4 | SPI SCLK |  |
| 5 | free (SPI CS line) |  |
| 14 | libre - E/S |  |
| 15 | libre - E/S |  |
| 16 | libre - E/S |  |
| 17 | libre - E/S |  |
| 18 | libre - E/S |  |
| 19 | libre - E/S |  |
| 20 | libre - E/S |  |
| 21 | USB HUB RST | ⚠  |
| 22 | I2C SDA |  |
| 23 | I2C SCL |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 29 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 30 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 31 | Ethernet MDC (IP101GRI) | ⚠ usado por la placa |
| 32 | libre - E/S |  |
| 33 | libre - E/S |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 35 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 36 | libre - E/S | ⚠ pin de strapping |
| 46 | libre - E/S |  |
| 47 | libre - E/S |  |
| 48 | libre - E/S |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 50 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ usado por la placa |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ usado por la placa |
| 53 | SPI MOSI |  |
| 54 | SPI MISO |  |

Los pines libres están en la tira **EXT1** de 20 pines: GPIO14 a GPIO20,
32, 33, 36, 46, 47, 48 y el LED de usuario en GPIO2. El conector **UEXT**
lleva I2C (GPIO22 / GPIO23 - compartido con el puente HDMI), SPI (GPIO4 /
53 / 54, CS GPIO5) y la UART de consola. El ESP32-P4 no tiene ninguna
entrada analógica que use ctrl32: las señales analógicas van por un ADC
I2C (un ADS1115 en UEXT) o por un módulo Modbus. CAN y RS-485 van en
pines libres de EXT1 con un módulo transceptor de 3,3 V.

## Seguridad

- La placa no está pensada para funciones de seguridad. Una parada de
  emergencia, un interruptor de puerta o una cortina de luz se cablean en
  hardware, nunca a través de un programa.
- Los pines GPIO son de 3,3 V. Una señal de 24 V necesita un optoacoplador
  o un adaptador de nivel; la bobina de un relé necesita un driver (un
  módulo de relés ya lo lleva).

## Fotos

![Olimex ESP32-P4-PC - foto 1](img/board-01.jpg)
![Olimex ESP32-P4-PC - foto 2](img/board-02.jpg)
![Olimex ESP32-P4-PC - foto 3](img/board-03.jpg)
![Olimex ESP32-P4-PC - foto 4](img/board-04.jpg)

---

[← Resumen](README.es.md) | [Resumen](README.es.md) | [Instalar el runtime →](install.es.md)
