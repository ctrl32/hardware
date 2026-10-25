---
title: 'Olimex ESP32-EVB: hardware y cableado'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Olimex ESP32-EVB - mapa de pines
tags:
- esp32
- ethernet
- can
- relay
- olimex
---

# Hardware y cableado

## Qué necesitas

- La Olimex ESP32-EVB.
- Un cable de datos micro-USB - para la primera carga del runtime.
- Alimentación: una fuente USB de 5 V, o 5 V en el borne de tornillo.
- Un cable Ethernet y un puerto libre en tu red.
- Un PC con el [editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opcional, para el ejemplo all-in-one: un potenciómetro (10 k) entre 3,3 V y GND con el cursor en GPIO36 (UEXT); un nodo CAN o un adaptador CAN y dos terminaciones de 120 ohmios.
- Opcional: la pantalla Olimex MOD-LCD2.8RTP (2,8 pulgadas, 240 x 320, táctil resistivo) en el conector UEXT.

## Alimentación

| Fuente | Dónde | Nota |
|---|---|---|
| USB 5 V | el conector micro-USB | el camino para la primera carga |
| 5 V DC | el borne de tornillo | para un armario |
| Batería Li-Po | el conector de batería | se carga en la placa |

!!! warning "Los relés conmutan tensión de red"
    Cablea los contactos de los relés solo con la placa sin alimentación,
    dentro de una caja, y solo una persona autorizada para trabajar en
    instalaciones de red. Los contactos admiten 10 A / 250 VAC; un motor o
    un calefactor por encima de eso necesita un contactor accionado por el
    relé.

## Mapa de pines

![Olimex ESP32-EVB - mapa de pines](pinout/pinout.png)

| GPIO | Función en ctrl32 | Nota |
|---|---|---|
| 0 | Ethernet 50 MHz clock (LAN8710A) | ⚠ usado por la placa |
| 2 | TFT MOSI | ⚠ pin de strapping |
| 2 | SPI MOSI | ⚠ pin de strapping |
| 4 | free (UART TX line) |  |
| 5 | CAN TX |  |
| 6 | flash SPI del módulo | ⚠ usado por la placa |
| 7 | flash SPI del módulo | ⚠ usado por la placa |
| 8 | flash SPI del módulo | ⚠ usado por la placa |
| 9 | flash SPI del módulo | ⚠ usado por la placa |
| 10 | flash SPI del módulo | ⚠ usado por la placa |
| 11 | flash SPI del módulo | ⚠ usado por la placa |
| 13 | I2C SDA |  |
| 14 | TFT SCLK |  |
| 14 | SPI SCLK |  |
| 15 | TFT DC | ⚠ pin de strapping |
| 15 | SPI MISO | ⚠ pin de strapping |
| 16 | I2C SCL |  |
| 17 | TFT CS |  |
| 17 | free (SPI CS line) |  |
| 18 | Ethernet MDIO (LAN8710A) | ⚠ usado por la placa |
| 19 | Ethernet RMII TXD0 (LAN8710A) | ⚠ usado por la placa |
| 21 | Ethernet RMII TX_EN (LAN8710A) | ⚠ usado por la placa |
| 22 | Ethernet RMII TXD1 (LAN8710A) | ⚠ usado por la placa |
| 23 | Ethernet MDC (LAN8710A) | ⚠ usado por la placa |
| 25 | Ethernet RMII RXD0 (LAN8710A) | ⚠ usado por la placa |
| 26 | Ethernet RMII RXD1 (LAN8710A) | ⚠ usado por la placa |
| 27 | Ethernet RMII CRS_DV (LAN8710A) | ⚠ usado por la placa |
| 32 | free (REL1 line) | ADC1 |
| 33 | free (REL2 line) | ADC1 |
| 34 | libre - el botón de la placa | ⚠ solo entrada, ADC1 |
| 35 | CAN RX |  |
| 36 | free (UART RX line) | ⚠ solo entrada, ADC1 |

**Relés:** REL1 en GPIO32, REL2 en GPIO33. **Botón:** BUT1 en GPIO34
(solo entrada). **CAN:** el transceptor de la placa en GPIO5 (TX) /
GPIO35 (RX), CAN_H / CAN_L en el borne - termina el bus con 120 ohmios en
ambos extremos. El conector **UEXT** lleva I2C (GPIO13 / GPIO16), SPI y
una UART libre (GPIO4 / GPIO36); la pantalla opcional usa sus líneas SPI.

## Seguridad

- La placa no está pensada para funciones de seguridad. Una parada de
  emergencia, un interruptor de puerta o una cortina de luz se cablean en
  hardware, nunca a través de un programa.
- Los pines GPIO son de 3,3 V. Una señal de 24 V necesita un optoacoplador
  o un adaptador de nivel; la bobina de un relé necesita un driver (un
  módulo de relés ya lo lleva).

---

[← Resumen](README.es.md) | [Resumen](README.es.md) | [Instalar el runtime →](install.es.md)
