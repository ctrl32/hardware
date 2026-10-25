---
title: 'Raspberry Pi 3 Model B+: solución de problemas'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Raspberry Pi 3 Model B+
tags:
- raspberry-pi
- linux
- hmi
- opc-ua
- troubleshooting
---

# Solución de problemas

| Síntoma | Causa | Solución |
|---|---|---|
| Look at the device no consigue conectar | SSH está desactivado, la dirección es incorrecta o el PC está en otra red | Activa SSH en los ajustes del Imager y vuelve a grabar la tarjeta; haz ping a la dirección desde el PC. |
| Prepare no ofrece ninguna instalación | El runtime de ctrl32 ya está instalado en la Pi | Un runtime instalado se actualiza con Flash runtime y la dirección de la Pi en el selector de puertos. |
| El monitor sigue en negro después de la descarga | El monitor se conectó después del arranque, o el proyecto no tiene pantalla | Conecta el monitor antes de encender la Pi; añade una pantalla al proyecto. |
| WEBview no se abre | El puerto equivocado | Abre http://<dirección>:8080 - el runtime sirve en el 8080. |
| El adaptador USB-RS485 desaparece | Subtensión - la fuente es demasiado débil | Usa la fuente oficial de 27 W. |
| CAN se queda en silencio | El driver del HAT no está cargado, falta la terminación, o una velocidad de bits distinta | Marca el HAT en Prepare a Linux device; una resistencia de 120 ohmios en ambos extremos del bus; la misma velocidad de bits en todos los nodos. |
| Un cliente OPC UA no ve ninguna variable | La variable se ha dejado fuera del servidor, o un cortafuegos bloquea el puerto 4840 | Comprueba la marca OPC UA en la lista de variables; abre el puerto 4840. |

El panel **Messages** del editor y el **búfer de diagnóstico** de la placa (Online → Diagnostics) dicen qué decidió el runtime y por qué - léelos primero.

---

[← Proyectos de ejemplo](examples/README.es.md) | [Resumen](README.es.md)
