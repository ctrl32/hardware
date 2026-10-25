---
title: 'LaskaKit ESPlan: hardware y cableado'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: LaskaKit ESPlan - mapa de pines
tags:
- esp32
- ethernet
- rs485
- modbus
- laskakit
---

# Hardware y cableado

## Qué necesitas

- La LaskaKit ESPlan.
- Un cable de datos USB-C - para la primera carga del runtime.
- Alimentación: 12 o 24 V DC en el borne de tornillo (7-40 V), o 5 V por USB-C.
- Un cable Ethernet y un puerto libre en tu red.
- Un PC con el [editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opcional, para el ejemplo all-in-one: un sensor de temperatura Modbus RTU (unidad 1) en el borne RS-485; un pulsador de GPIO16 a GND; un potenciómetro (10 k) entre 3,3 V y GND con el cursor en GPIO35; un transceptor CAN de 3,3 V en GPIO14 (TX) / GPIO39 (RX).

## Alimentación

| Fuente | Dónde | Nota |
|---|---|---|
| 7-40 V DC | el borne de tornillo | se recomiendan 12 o 24 V |
| USB 5 V | el conector USB-C | el camino para la primera carga |
| PoE | mediante el módulo PoE opcional (802.3af) | módulo adicional |

## Mapa de pines

![LaskaKit ESPlan - mapa de pines](pinout/pinout.png)

| GPIO | Función en ctrl32 | Nota |
|---|---|---|
| 0 | free (LED0 line) | ⚠ pin de strapping |
| 4 | RS485 TX |  |
| 5 | Ethernet PHY power (LAN8720A) | ⚠ usado por la placa |
| 6 | flash SPI del módulo | ⚠ usado por la placa |
| 7 | flash SPI del módulo | ⚠ usado por la placa |
| 8 | flash SPI del módulo | ⚠ usado por la placa |
| 9 | flash SPI del módulo | ⚠ usado por la placa |
| 10 | flash SPI del módulo | ⚠ usado por la placa |
| 11 | flash SPI del módulo | ⚠ usado por la placa |
| 12 | SPI MISO | ⚠ pin de strapping |
| 13 | SPI MOSI |  |
| 14 | free (SPI SCLK line) |  |
| 15 | SPI CS | ⚠ pin de strapping |
| 16 | libre - E/S |  |
| 17 | Ethernet 50 MHz clock (LAN8720A) | ⚠ usado por la placa |
| 18 | Ethernet MDIO (LAN8720A) | ⚠ usado por la placa |
| 19 | Ethernet RMII TXD0 (LAN8720A) | ⚠ usado por la placa |
| 21 | Ethernet RMII TX_EN (LAN8720A) | ⚠ usado por la placa |
| 22 | Ethernet RMII TXD1 (LAN8720A) | ⚠ usado por la placa |
| 23 | Ethernet MDC (LAN8720A) | ⚠ usado por la placa |
| 25 | Ethernet RMII RXD0 (LAN8720A) | ⚠ usado por la placa |
| 26 | Ethernet RMII RXD1 (LAN8720A) | ⚠ usado por la placa |
| 27 | Ethernet RMII CRS_DV (LAN8720A) | ⚠ usado por la placa |
| 32 | TOUCH SCL |  |
| 33 | TOUCH SDA |  |
| 35 | libre - entrada | ⚠ solo entrada, ADC1 |
| 36 | RS485 RX |  |
| 39 | libre - entrada | ⚠ solo entrada, ADC1 |

**RS-485:** A y B en el borne, el transceptor WS3081 en GPIO4 (TX) /
GPIO36 (RX); un puente activa la terminación de 120 ohmios - ponla solo en
los dos extremos de la línea. Los conectores **uSup** llevan I2C (GPIO33 /
GPIO32) y SPI. El LED de la placa está en GPIO0 (un pin de strapping -
déjalo como salida accionada por el programa).

## Seguridad

- La placa no está pensada para funciones de seguridad. Una parada de
  emergencia, un interruptor de puerta o una cortina de luz se cablean en
  hardware, nunca a través de un programa.
- Los pines GPIO son de 3,3 V. Una señal de 24 V necesita un optoacoplador
  o un adaptador de nivel; la bobina de un relé necesita un driver (un
  módulo de relés ya lo lleva).

---

[← Resumen](README.es.md) | [Resumen](README.es.md) | [Instalar el runtime →](install.es.md)
