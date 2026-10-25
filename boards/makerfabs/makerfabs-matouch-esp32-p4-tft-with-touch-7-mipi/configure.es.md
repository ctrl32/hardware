---
title: Configurar la Makerfabs MaTouch ESP32-P4 7" en el editor ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: La página de la placa Makerfabs MaTouch ESP32-P4 7" en el editor
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
---

# Configurar la placa

## La página de la placa

Haz doble clic en la placa en el árbol de dispositivos. La página muestra lo que lleva la placa y cada pin: un pin libre recibe una variable con un clic - una entrada, una salida o, en un pin con capacidad analógica, una entrada analógica.

![La página de la placa: los pines libres y lo que puede hacer cada uno](img/configure-01-board.png)

## Red

El puerto Ethernet arranca por sí solo y toma su dirección de tu router
(DHCP). La Wi-Fi del ESP32-C6 se ajusta en la página **WiFi** del árbol de
dispositivos - el nombre de la red y la contraseña. Una dirección fija se
ajusta en la página de la placa, en su sección **Network**.


## Entradas, salidas y variables

Cada señal del programa es una **variable**. Una variable en un pin lee o acciona el pin; una variable analógica indica qué hay conectado (una tensión, 4-20 mA, un termistor) y su rango en unidades.

![Las variables del ejemplo all-in-one](img/configure-03-variables.png)

## Comunicación

**Modbus TCP.** Un dispositivo de la red se añade en **Ethernet → Modbus TCP master**; sus registros se convierten en variables.

**Modbus RTU / RS-485.** La placa no tiene transceptor RS-485: pon un módulo transceptor de 3,3 V en pines libres (TX, RX y el pin de dirección DE) e indícalos en la página de la placa - el ejemplo usa GPIO4 / GPIO5 / GPIO32. ctrl32 es entonces maestro o esclavo Modbus RTU en esa línea.

**CAN.** El ESP32-P4 tiene un controlador CAN (TWAI). La placa no tiene transceptor CAN: pon un módulo transceptor de 3,3 V en dos pines libres e indícalos en la página de la placa (**Bus pins**) - el ejemplo usa GPIO20 / GPIO21. Los dispositivos CANopen, las tramas CAN en bruto y los buses de vehículos (J1939) funcionan todos sobre él.

**MQTT.** La placa publica las variables elegidas en un broker; en el modo Home Assistant el broker las encuentra por sí solo, y una variable marcada como *write* se puede ajustar desde allí.

![La página MQTT: el broker y las variables publicadas](img/configure-05-mqtt.png)

## Pantalla y táctil

El proyecto se dibuja a los 1024 x 600 propios del cristal. La página
HMIview ajusta la orientación (tal como está montada, o girada - el táctil
la sigue), el tamaño del lienzo de WEBview y la pantalla de arranque. El
táctil no necesita configuración: el controlador GT911 forma parte de la
placa.

![Los ajustes de HMIview: la pantalla en la que dibuja el proyecto](img/configure-04-display.png)

## WEBview

La placa sirve su página del operador a cualquier navegador de la red - abre la dirección de la placa. La página se dibuja en el editor como una pantalla.

![Los ajustes de la página WEBview](img/configure-06-webview.png)

---

[← Instalar el runtime](install.es.md) | [Resumen](README.es.md) | [Proyectos de ejemplo →](examples/README.es.md)
