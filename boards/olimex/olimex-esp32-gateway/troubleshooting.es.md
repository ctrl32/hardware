---
title: 'Olimex ESP32-GATEWAY: solución de problemas'
slug: troubleshooting
sidebar_position: 90
image: img/board-01.jpg
image_alt: Olimex ESP32-GATEWAY
tags:
- esp32
- ethernet
- gateway
- olimex
- troubleshooting
---

# Solución de problemas

| Síntoma | Causa | Solución |
|---|---|---|
| El puerto COM no aparece, el selector de puertos se queda vacío | El cable solo lleva alimentación, o falta el driver USB | Usa un cable de datos; instala el driver del chip USB de la placa; prueba otro puerto USB. |
| Flash runtime se detiene al conectar | Otro programa tiene ocupado el puerto | Cierra el monitor serie o la otra herramienta que tiene el puerto abierto y vuelve a intentarlo. |
| La placa se reinicia cada pocos segundos | El puerto USB no puede dar la corriente | Usa un hub USB con alimentación propia o una fuente de 5 V de al menos 1 A. |
| La red no se levanta | No hay servidor DHCP, o no hay enlace en el puerto | Comprueba los LED de enlace del conector; pon una dirección fija en la página de la placa; prueba otro puerto del switch. |
| La placa no se encuentra por su nombre .local | La red bloquea mDNS (multicast) | Usa la dirección IP de la placa - la lista de clientes del router y Find devices del editor la muestran. |
| Una salida no hace nada | El pin es solo de entrada, o se indicó un pin equivocado | Comprueba el pin en la página de la placa - los pines solo de entrada están marcados; pasa la salida a un pin de E/S libre. |
| Un valor Modbus se queda en 0 | La dirección del dispositivo, la unidad o el registro son incorrectos | Comprueba la IP y la unidad del dispositivo en el árbol de dispositivos y el registro en el manual del dispositivo. |

El panel **Messages** del editor y el **búfer de diagnóstico** de la placa (Online → Diagnostics) dicen qué decidió el runtime y por qué - léelos primero.

---

[← Proyectos de ejemplo](examples/README.es.md) | [Resumen](README.es.md)
