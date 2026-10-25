---
title: 'Makerfabs MaTouch ESP32-P4 7": solución de problemas'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Makerfabs MaTouch ESP32-P4 7"
tags:
- esp32-p4
- display
- touch
- hmi
- ethernet
- makerfabs
- troubleshooting
---

# Solución de problemas

| Síntoma | Causa | Solución |
|---|---|---|
| El puerto COM no aparece | El cable solo lleva alimentación, o falta el driver CH340 | Usa un cable de datos USB-C; instala el driver CH340 (WCH CH341SER); prueba otro puerto USB. |
| La placa se reinicia cuando se enciende la pantalla | La fuente no puede con la retroiluminación | Usa una fuente de 5 V / 2 A o un hub USB con alimentación propia. |
| La pantalla sigue a oscuras después de escribir el runtime | Todavía no hay ningún proyecto en la placa | Descarga el proyecto (F5); una placa sin proyecto no muestra nada en el cristal. |
| El táctil no responde, o responde en el sitio equivocado | La orientación del proyecto no coincide con cómo está montada la placa | Ajusta la orientación en la página HMIview y vuelve a descargar. |
| La red no se levanta | No hay servidor DHCP, o no hay enlace en el puerto | Comprueba los LED de enlace del conector; pon una dirección fija en la página de la placa; para la Wi-Fi comprueba el nombre de la red y la contraseña. |
| CAN se queda en silencio | Falta el transceptor o la terminación de 120 ohmios, o una velocidad de bits distinta | Comprueba el transceptor en GPIO20 / GPIO21, una resistencia de 120 ohmios en ambos extremos del bus y la misma velocidad de bits en todos los nodos. |
| Un valor Modbus RTU se queda en 0 | A y B intercambiados, una unidad o velocidad incorrecta, o falta el pin DE | Intercambia A y B; comprueba la unidad, la velocidad y la paridad; comprueba que DE está cableado e indicado. |

El panel **Messages** del editor y el **búfer de diagnóstico** de la placa (Online → Diagnostics) dicen qué decidió el runtime y por qué - léelos primero.

---

[← Proyectos de ejemplo](examples/README.es.md) | [Resumen](README.es.md)
