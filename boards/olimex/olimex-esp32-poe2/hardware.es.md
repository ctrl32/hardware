---
title: 'Olimex ESP32-POE2: hardware y cableado'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-POE2 - mapa de pines
tags:
- esp32
- ethernet
- poe
- psram
- olimex
---

# Hardware y cableado

## Qué necesitas

- La Olimex ESP32-POE2.
- Un cable de datos USB-C - para la primera carga del runtime.
- Alimentación: un switch / inyector PoE (IEEE 802.3at, clase 4 para los 25 W completos), o una fuente USB de 5 V.
- Un cable Ethernet y un puerto libre en tu red.
- Un PC con el [editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opcional, para el ejemplo all-in-one: el botón BUT1 está en la placa; un módulo de relés o un LED en GPIO4 (UEXT); un potenciómetro (10 k) entre 3,3 V y GND con el cursor en GPIO36; un transceptor CAN de 3,3 V en GPIO5 (TX) / GPIO39 (RX).

## Alimentación

| Fuente | Dónde | Nota |
|---|---|---|
| PoE | el conector Ethernet | IEEE 802.3at clase 4, hasta 25 W |
| USB 5 V | el conector USB-C | el camino para la primera carga |
| Batería Li-Po | el conector de batería | se carga en la placa |

Alimentada por Ethernet, la placa da corriente a circuitos externos:
**24 V / 0,75 A o 12 V / 1,5 A** (un puente elige), **5 V / 1,5 A** y
**3,3 V / 1 A**, 25 W en total.

!!! danger "Nunca conectes USB y PoE a la vez"
    La ESP32-POE2 **no tiene aislamiento galvánico** respecto a la
    alimentación Ethernet. Carga el runtime por USB con el cable Ethernet
    desenchufado (o desde un puerto sin PoE) y después haz funcionar la
    placa con PoE.

## Mapa de pines

![Olimex ESP32-POE2 - mapa de pines](pinout/pinout.png)

| GPIO | Función en ctrl32 | Nota |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ usado por la placa |
| 2 | SPI MOSI | ⚠ pin de strapping |
| 4 | free (UART TX line) |  |
| 5 | free (SPI CS line) |  |
| 6 | flash SPI del módulo | ⚠ usado por la placa |
| 7 | flash SPI del módulo | ⚠ usado por la placa |
| 8 | flash SPI del módulo | ⚠ usado por la placa |
| 9 | flash SPI del módulo | ⚠ usado por la placa |
| 10 | flash SPI del módulo | ⚠ usado por la placa |
| 11 | flash SPI del módulo | ⚠ usado por la placa |
| 12 | Ethernet PHY power (LAN8710A) | ⚠ usado por la placa |
| 13 | I2C SDA |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ pin de strapping |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ usado por la placa |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ usado por la placa |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ usado por la placa |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ usado por la placa |
| 23 | Ethernet MDC (LAN8710A) | ⚠ usado por la placa |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ usado por la placa |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ usado por la placa |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ usado por la placa |
| 33 | I2C SCL |  |
| 34 | libre - el botón de la placa | ⚠ solo entrada, ADC1 |
| 36 | free (UART RX line) | ⚠ solo entrada, ADC1 |
| 39 | libre - entrada | ⚠ solo entrada, ADC1 |

Los pines libres están en las tiras **EXT** y en el conector **UEXT**.
GPIO34 a GPIO39 son solo entradas. La PSRAM del módulo ocupa GPIO16 /
GPIO17, así que el reloj de Ethernet va por GPIO0 e I2C usa GPIO13 /
GPIO33.

## Seguridad

- La placa no está pensada para funciones de seguridad. Una parada de
  emergencia, un interruptor de puerta o una cortina de luz se cablean en
  hardware, nunca a través de un programa.
- Los pines GPIO son de 3,3 V. Una entrada de 24 V necesita un
  optoacoplador o un adaptador de nivel; la bobina de un relé necesita un
  driver (un módulo de relés ya lo lleva).

---

[← Resumen](README.es.md) | [Resumen](README.es.md) | [Instalar el runtime →](install.es.md)
