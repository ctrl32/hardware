---
title: Configurar la Makerfabs MaTouch Lite ESP32-S3 3.95" en el editor ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: La página de la placa Makerfabs MaTouch Lite ESP32-S3 3.95" en el editor
tags:
- esp32-s3
- display
- touch
- hmi
- wifi
- makerfabs
---

# Configurar la placa

## La página de la placa

Haz doble clic en la placa en el árbol de dispositivos. La página muestra lo que lleva la placa y cada pin: un pin libre recibe una variable con un clic - una entrada, una salida o, en un pin con capacidad analógica, una entrada analógica.

![La página de la placa: los pines libres y lo que puede hacer cada uno](img/configure-01-board.png)

## Red

La placa se conecta a tu Wi-Fi: abre la página **WiFi** del árbol de
dispositivos y escribe el nombre y la contraseña de la red (el ejemplo
lleva valores de relleno). Una dirección fija se ajusta en la página de la
placa, en su sección **Network**.


## Entradas, salidas y variables

Cada señal del programa es una **variable**. Una variable en un pin lee o acciona el pin; una variable analógica indica qué hay conectado (una tensión, 4-20 mA, un termistor) y su rango en unidades.

![Las variables del ejemplo all-in-one](img/configure-03-variables.png)

## Comunicación

**Modbus TCP.** Un dispositivo de la red se añade en **Ethernet → Modbus TCP master**; sus registros se convierten en variables.

**Modbus RTU / RS-485.** La placa no tiene transceptor RS-485 y le quedan demasiado pocos pines libres para uno junto a las E/S del ejemplo; a los dispositivos Modbus se llega por Modbus TCP en la Wi-Fi.

**CAN.** El ESP32-S3 tiene un controlador CAN (TWAI). La placa no tiene transceptor: pon un módulo transceptor de 3,3 V en dos pines libres e indícalos en la página de la placa (**Bus pins**); el ejemplo usa GPIO6 / GPIO7.

**MQTT.** La placa publica las variables elegidas en un broker; en el modo Home Assistant el broker las encuentra por sí solo, y una variable marcada como *write* se puede ajustar desde allí.

![La página MQTT: el broker y las variables publicadas](img/configure-05-mqtt.png)

## Pantalla y táctil

El cristal es de 320 x 480, en vertical tal como está montado; la página
HMIview gira la imagen (el táctil la sigue) y ajusta la pantalla de
arranque. El táctil resistivo necesita pulsaciones firmes - dibuja botones
de al menos 40 px de alto.

![Los ajustes de HMIview: la pantalla en la que dibuja el proyecto](img/configure-04-display.png)

## WEBview

La placa sirve su página del operador a cualquier navegador de la red - abre la dirección de la placa. La página se dibuja en el editor como una pantalla.

![Los ajustes de la página WEBview](img/configure-06-webview.png)

---

[← Instalar el runtime](install.es.md) | [Resumen](README.es.md) | [Proyectos de ejemplo →](examples/README.es.md)
