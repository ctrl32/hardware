---
title: 'Makerfabs MaTouch ESP32-P4 7": hardware y cableado'
slug: hardware
sidebar_position: 20
image: pinout/pinout.png
image_alt: Makerfabs MaTouch ESP32-P4 7" - mapa de pines
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Hardware y cableado

## Qué necesitas

- La Makerfabs MaTouch ESP32-P4 TFT with Touch 7" MIPI.
- Un cable de datos USB-C - para la primera carga del runtime y para la alimentación.
- Alimentación: una fuente USB-C de 5 V de al menos 2 A (la retroiluminación de la pantalla consume la mayor parte).
- Un cable Ethernet, o la Wi-Fi de tu red.
- Un PC con el [editor ctrl32](https://ctrl32.com/download/) (Windows).
- Opcional, para el ejemplo all-in-one: dos pulsadores y un módulo de relés en la tira J6; un módulo ADS1115 en el bus I2C; un transceptor RS-485 de 3,3 V (p. ej. MAX3485) y un transceptor CAN de 3,3 V (p. ej. SN65HVD230).

## Alimentación

| Fuente | Dónde | Nota |
|---|---|---|
| USB 5 V | el conector USB-C | 2 A o más - la retroiluminación de 7" consume la mayor parte |
| Batería Li-Po | el conector de batería | 3,7 V, se carga en la placa |

!!! warning "Una fuente débil"
    El puerto USB de un PC a menudo no puede con la placa con la
    retroiluminación encendida. Si la placa se reinicia cuando se enciende
    la pantalla, usa una fuente de 5 V / 2 A o un hub USB con alimentación
    propia.

## Mapa de pines

![Makerfabs MaTouch ESP32-P4 7" - mapa de pines](pinout/pinout.png)

| GPIO | Función en ctrl32 | Nota |
|---|---|---|
| 0 | RTC XTAL P | ⚠  |
| 1 | RTC XTAL N | ⚠  |
| 2 | libre - E/S |  |
| 3 | libre - E/S |  |
| 4 | libre - E/S |  |
| 5 | libre - E/S |  |
| 6 | C6 IO2 | ⚠  |
| 7 | TOUCH SDA |  |
| 8 | TOUCH SCL |  |
| 20 | libre - E/S |  |
| 21 | libre - E/S |  |
| 22 | TOUCH RST |  |
| 23 | TFT BL |  |
| 26 | USB1 PAIR | ⚠  |
| 27 | DSI RST |  |
| 28 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 29 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 30 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 31 | Ethernet MDC (IP101GRI) | ⚠ usado por la placa |
| 32 | libre - E/S |  |
| 33 | libre - E/S |  |
| 34 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 35 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 36 | libre - E/S | ⚠ pin de strapping |
| 37 | CONSOLE RX | ⚠ pin de strapping |
| 38 | CONSOLE TX | ⚠ pin de strapping |
| 45 | MOSFET GATE | ⚠  |
| 46 | libre - E/S |  |
| 47 | libre - E/S |  |
| 48 | libre - E/S |  |
| 49 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 50 | Ethernet RMII (IP101GRI) | ⚠ usado por la placa |
| 51 | Ethernet PHY reset (IP101GRI) | ⚠ usado por la placa |
| 52 | Ethernet MDIO (IP101GRI) | ⚠ usado por la placa |
| 53 | AMP EN | ⚠  |
| 54 | C6 EN | ⚠  |

Los pines libres están en las tiras **J6** y **J10** y en los dos
conectores Grove (**J1**, **J2**). El bus I2C de la placa (GPIO7 / GPIO8)
lleva el controlador táctil y el códec de audio; otros chips I2C (un
ADS1115, un sensor) se conectan al mismo bus. CAN y RS-485 no tienen
transceptor en la placa: el ejemplo los pone en pines libres - **CAN** TX
GPIO20 / RX GPIO21 (Grove J2), **RS-485** TX GPIO4 / RX GPIO5 / DE GPIO32
(J10) - cada uno a un módulo transceptor de 3,3 V.

## Seguridad

- La placa no está pensada para funciones de seguridad. Una parada de
  emergencia, un interruptor de puerta o una cortina de luz se cablean en
  hardware, nunca a través de un programa ni de una pantalla táctil.
- Los pines GPIO son de 3,3 V. Una señal de 24 V necesita un
  optoacoplador; la bobina de un relé necesita un driver (un módulo de
  relés ya lo lleva).
- El táctil capacitivo puede registrar una pulsación falsa junto a una
  fuente de interferencias fuerte (un variador). Las órdenes críticas en
  una pantalla piden una confirmación.

## Fotos

![Makerfabs MaTouch ESP32-P4 7" - foto 1](img/board-01.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 2](img/board-02.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 3](img/board-03.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 4](img/board-04.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 5](img/board-05.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 6](img/board-06.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 7](img/board-07.jpg)
![Makerfabs MaTouch ESP32-P4 7" - foto 8](img/board-08.jpg)

---

[← Resumen](README.es.md) | [Resumen](README.es.md) | [Instalar el runtime →](install.es.md)
