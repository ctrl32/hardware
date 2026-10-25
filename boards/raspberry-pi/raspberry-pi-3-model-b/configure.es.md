---
title: Configurar la Raspberry Pi 3 Model B+ en el editor ctrl32
slug: configure
sidebar_position: 40
image: img/configure-01-board.png
image_alt: La página de la placa Raspberry Pi 3 Model B+ en el editor
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
---

# Configurar la placa

## La página de la placa

Haz doble clic en la placa en el árbol de dispositivos. La página muestra lo que lleva la placa y cada pin: un pin libre recibe una variable con un clic - una entrada, una salida o, en un pin con capacidad analógica, una entrada analógica.

![La página de la placa: los pines libres y lo que puede hacer cada uno](img/configure-01-board.png)

## Red

La Pi conserva los ajustes de red de su sistema operativo: DHCP del router,
salvo que **Prepare a Linux device** haya puesto una dirección fija.
Encuéntrala por su nombre de host o con **Find devices** del editor.


## Entradas, salidas y variables

Cada señal del programa es una **variable**. Una variable en un pin lee o acciona el pin; una variable analógica indica qué hay conectado (una tensión, 4-20 mA, un termistor) y su rango en unidades.

![Las variables del ejemplo all-in-one](img/configure-03-variables.png)

## Comunicación

**Modbus TCP.** Un dispositivo de la red se añade en **Ethernet → Modbus TCP master**; sus registros se convierten en variables.

**Modbus RTU / RS-485.** Un adaptador USB-RS485 (`/dev/ttyUSB0`, la dirección conmuta sola) o un HAT RS-485 en la UART de la Pi. ctrl32 es maestro o esclavo Modbus RTU en él, hasta en cuatro líneas.

**CAN.** CAN llega desde un HAT CAN en SPI (MCP2515, MCP251xFD) o un adaptador CAN USB; el runtime lo usa como interfaz SocketCAN (`can0`, hasta cuatro buses). Prepare a Linux device añade el driver del HAT; la velocidad de bits es la del proyecto.

**MQTT.** La placa publica las variables elegidas en un broker; en el modo Home Assistant el broker las encuentra por sí solo, y una variable marcada como *write* se puede ajustar desde allí.

![La página MQTT: el broker y las variables publicadas](img/configure-05-mqtt.png)

## Pantalla

El runtime dibuja en el monitor HDMI conectado (o en una pantalla DSI) y
escala el proyecto a él; el ejemplo está dibujado a 1280 x 720. El táctil
USB de un monitor táctil funciona sin driver. Sin monitor, la Pi sirve sus
pantallas solo a navegadores (WEBview).

![Los ajustes de HMIview: la pantalla en la que dibuja el proyecto](img/configure-04-display.png)

## OPC UA y EtherCAT

- **OPC UA** - cada variable del proyecto es un nodo del propio servidor
  de la Pi (`opc.tcp://<dirección>:4840`, `ns=1;s=<nombre>`); una variable
  se puede dejar fuera con una marca en la lista de variables. No se
  ajusta nada más.
- **EtherCAT** - un maestro en un adaptador Ethernet USB para terminales
  de E/S; para servoaccionamientos con un ciclo de bus corto una
  Raspberry Pi 4 o 5 es la mejor opción.

## WEBview

La placa sirve su página del operador a cualquier navegador de la red - abre la dirección de la placa. La página se dibuja en el editor como una pantalla.

![Los ajustes de la página WEBview](img/configure-06-webview.png)

---

[← Instalar el runtime](install.es.md) | [Resumen](README.es.md) | [Proyectos de ejemplo →](examples/README.es.md)
