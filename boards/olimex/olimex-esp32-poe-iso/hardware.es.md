---
title: 'Olimex ESP32-PoE-ISO: hardware y cableado'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-PoE-ISO - mapa de pines
tags:
- esp32
- ethernet
- poe
- isolated
- olimex
---

# Hardware y cableado

## Qué necesitas

- La Olimex ESP32-PoE-ISO (la variante WROOM-32E, sin PSRAM).
- Un cable de datos micro-USB - para la primera carga del runtime.
- Alimentación: un switch / inyector PoE (IEEE 802.3af), o una fuente USB de 5 V.
- Un cable Ethernet y un puerto libre en tu red.
- Un PC con el [editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opcional, para el ejemplo all-in-one: el botón BUT1 está en la placa; un módulo de relés o un LED con resistencia en GPIO4 (UEXT); un potenciómetro (10 k) entre 3,3 V y GND con el cursor en GPIO33 (EXT2); un transceptor CAN de 3,3 V en GPIO5 (TX) / GPIO36 (RX).

## Alimentación

| Fuente | Dónde | Nota |
|---|---|---|
| PoE | el conector Ethernet, desde un switch o inyector PoE | IEEE 802.3af, aislada |
| USB 5 V | el conector micro-USB | el camino para la primera carga |
| Batería Li-Po | el conector de batería | se carga en la placa |

La alimentación PoE está **aislada galvánicamente** de la placa: a
diferencia de la ESP32-PoE sencilla, USB hacia un PC y PoE pueden estar
conectados a la vez - el runtime se puede cargar y observar online
mientras la placa sigue en su switch PoE.

## Mapa de pines

![Olimex ESP32-PoE-ISO - mapa de pines](pinout/pinout.png)

| GPIO | Función en ctrl32 | Nota |
|---|---|---|
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
| 33 | libre - E/S | ADC1 |
| 34 | libre - el botón de la placa | ⚠ solo entrada, ADC1 |
| 35 | libre - entrada | ⚠ solo entrada, ADC1 |
| 36 | free (UART RX line) | ⚠ solo entrada, ADC1 |

Los pines libres están en las tiras **EXT1 / EXT2** (2,54 mm) y en el
conector **UEXT**. GPIO34 a GPIO39 son solo entradas - el editor rechaza
una salida en ellos. El conector UEXT lleva I2C (GPIO13 / GPIO16) y SPI
(GPIO14 / GPIO2 / GPIO15, compartido con la ranura microSD).

## Seguridad

- La placa no está pensada para funciones de seguridad. Una parada de
  emergencia, un interruptor de puerta o una cortina de luz se cablean en
  hardware, nunca a través de un programa.
- Los pines GPIO son de 3,3 V. Una entrada de 24 V necesita un
  optoacoplador o un adaptador de nivel; la bobina de un relé necesita un
  driver (un módulo de relés ya lo lleva).

---

[← Resumen](README.es.md) | [Resumen](README.es.md) | [Instalar el runtime →](install.es.md)
