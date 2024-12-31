"""
Concepto de Callback en Python
"""
"""
Un callback es una función que se pasa como argumento a otra función para ser invocada posteriormente.
Este mecanismo permite un control flexible sobre el flujo del programa. 
Son útiles para manejar flujos asíncronos o dependientes de eventos.

"""

import time
import random

# Ejemplo simple de callback
def ejecutar_callback(callback, mensaje):
    print("Ejecutando la función principal...")
    callback(mensaje)

def mi_callback(mensaje):
    print(f"Callback invocado: {mensaje}")

print("Ejemplo simple:")
ejecutar_callback(mi_callback, "Hola desde el callback!")
print("-" * 50)

"""
Extra
"""
# Función principal que procesa pedidos
def procesar_pedido(plato, confirmar_callback, listo_callback, entrega_callback):
    print(f"Iniciando el procesamiento del pedido: {plato}")
    confirmar_callback(plato)  # Llamada al callback de confirmación

    # Simular tiempo de preparación entre 1 y 10 segundos
    tiempo_preparacion = random.randint(1, 10)
    time.sleep(tiempo_preparacion)  # Pausa para simular el tiempo

    listo_callback(plato, tiempo_preparacion)  # Llamada al callback de listo

    # Simular tiempo de entrega entre 1 y 5 segundos
    tiempo_entrega = random.randint(1, 5)
    time.sleep(tiempo_entrega)  # Pausa para simular el tiempo

    entrega_callback(plato, tiempo_entrega)  # Llamada al callback de entrega

# Definir los callbacks
def confirmar_pedido(plato):
    print(f"Pedido confirmado: {plato}. Preparación en curso...")

def plato_listo(plato, tiempo):
    print(f"El plato '{plato}' está listo después de {tiempo} segundos.")

def entregar_pedido(plato, tiempo):
    print(f"El plato '{plato}' ha sido entregado después de {tiempo} segundos adicionales.")

# Simulación
print("Simulador de pedidos:")
procesar_pedido("Pizza Margarita", confirmar_pedido, plato_listo, entregar_pedido)
print("-" * 50)
procesar_pedido("Hamburguesa con papas", confirmar_pedido, plato_listo, entregar_pedido)
