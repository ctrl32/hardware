---
title: 'Olimex ESP32-GATEWAY: hardware y cableado'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-GATEWAY - mapa de pines
tags:
- esp32
- ethernet
- gateway
- olimex
---

# Hardware y cableado

## Qué necesitas

- La Olimex ESP32-GATEWAY.
- Un cable de datos USB-C - para la carga y para la alimentación (5 V).
- Un cable Ethernet y un puerto libre en tu red.
- Un PC con el [editor ctrl32](https://ctrl32.com/download/) (Windows).
- El ejemplo all-in-one usa el propio botón (GPIO34) y el LED (GPIO33) de la placa - no hay que cablear nada más.

## Alimentación

| Fuente | Dónde | Nota |
|---|---|---|
| USB 5 V | el conector USB-C | alimentación y programación |

## Mapa de pines

![Olimex ESP32-GATEWAY - mapa de pines](pinout/pinout.png)

| GPIO | Función en ctrl32 | Nota |
|---|---|---|
| 2 | SPI MOSI | ⚠ pin de strapping |
| 5 | Ethernet PHY power (LAN8710A) | ⚠ usado por la placa |
| 6 | flash SPI del módulo | ⚠ usado por la placa |
| 7 | flash SPI del módulo | ⚠ usado por la placa |
| 8 | flash SPI del módulo | ⚠ usado por la placa |
| 9 | flash SPI del módulo | ⚠ usado por la placa |
| 10 | flash SPI del módulo | ⚠ usado por la placa |
| 11 | flash SPI del módulo | ⚠ usado por la placa |
| 13 | free (SPI CS line) |  |
| 14 | SPI SCLK |  |
| 15 | SPI MISO | ⚠ pin de strapping |
| 16 | I2C SCL |  |
| 17 | Ethernet 50 MHz clock (LAN8710A) | ⚠ usado por la placa |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ usado por la placa |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ usado por la placa |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ usado por la placa |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ usado por la placa |
| 23 | Ethernet MDC (LAN8710A) | ⚠ usado por la placa |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ usado por la placa |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ usado por la placa |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ usado por la placa |
| 32 | I2C SDA |  |
| 33 | free (LED0 line) | ADC1 |
| 34 | libre - el botón de la placa | ⚠ solo entrada, ADC1 |

La tira **EXT** de 20 pines lleva los pines libres y las líneas I2C /
SPI. El LED de la placa está en GPIO33 y su botón en GPIO34 (solo
entrada). Quedan pocos pines libres: más E/S van por Modbus TCP o por
chips I2C.

## Seguridad

- La placa no está pensada para funciones de seguridad. Una parada de
  emergencia, un interruptor de puerta o una cortina de luz se cablean en
  hardware, nunca a través de un programa.
- Los pines GPIO son de 3,3 V. Una señal de 24 V necesita un optoacoplador
  o un adaptador de nivel; la bobina de un relé necesita un driver (un
  módulo de relés ya lo lleva).

---

[← Resumen](README.es.md) | [Resumen](README.es.md) | [Instalar el runtime →](install.es.md)
