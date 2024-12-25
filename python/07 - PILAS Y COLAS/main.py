"""
Pilas y Colas en Python
"""

"""
Pila (Stack) - LIFO
"""
# - Se utiliza para almacenar elementos donde el último en entrar es el primero en salir.
# - Operaciones principales: 
#   * `push`: Introducir un elemento.
#   * `pop`: Recuperar el último elemento introducido.

# Implementación de una pila usando una lista:
stack = []

# Operación: Push (Agregar elementos)
stack.append(1)  # Agrega el número 1 a la pila.
stack.append(2)  # Agrega el número 2 a la pila.
stack.append(3)  # Agrega el número 3 a la pila.
print("Pila después de push:", stack)

# Operación: Pop (Eliminar y recuperar el último elemento)
last_item = stack.pop()  # Elimina y recupera el último elemento (3).
print("Elemento recuperado con pop:", last_item)
print("Pila después de pop:", stack)

# Operación manual de pop (sin usar `.pop()`)
last_item_manual = stack[-1]  # Accede al último elemento.
del stack[-1]  # Elimina el último elemento.
print("Elemento recuperado manualmente:", last_item_manual)
print("Pila después de eliminación manual:", stack)
print("")  # Separador visual

"""
Cola (Queue) - FIFO
"""
# - Se utiliza para almacenar elementos donde el primero en entrar es el primero en salir.
# - Operaciones principales:
#   * `enqueue`: Introducir un elemento.
#   * `dequeue`: Recuperar el primer elemento introducido.

# Implementación de una cola usando una lista:
queue = []

# Operación: Enqueue (Agregar elementos)
queue.append(1)  # Agrega el número 1 a la cola.
queue.append(2)  # Agrega el número 2 a la cola.
queue.append(3)  # Agrega el número 3 a la cola.
print("Cola después de enqueue:", queue)

# Operación: Dequeue (Eliminar y recuperar el primer elemento)
first_item = queue.pop(0)  # Elimina y recupera el primer elemento (1).
print("Elemento recuperado con dequeue:", first_item)
print("Cola después de dequeue:", queue)

# Operación manual de dequeue (sin usar `.pop(0)`)
first_item_manual = queue[0]  # Accede al primer elemento.
del queue[0]  # Elimina el primer elemento.
print("Elemento recuperado manualmente:", first_item_manual)
print("Cola después de eliminación manual:", queue)

"""
DIFICULTAD EXTRA: Simulaciones con Pilas y Colas
"""

"""
Simulación 1: Navegador web (Pilas)
"""
# - Simula un navegador web usando una pila.
# - Operaciones disponibles:
#   * "atrás": Retrocede a la página anterior (pop).
#   * "adelante": No tiene implementación (para simplicidad, es un placeholder).
#   * Cualquier otra entrada se considera como una nueva página (push).
# - Muestra siempre la página actual.

def navegador_web():
    print("\n--- Navegador Web (Pila) ---")
    stack = []

    while True:
        opcion = input("Introduce una URL o escribe 'adelante', 'atrás' o 'salir': ").strip().lower()

        if opcion == "salir":
            print("Saliendo del navegador...")
            break
        elif opcion == "adelante":
            print("Funcionalidad 'adelante' no implementada.")
        elif opcion == "atrás":
            if stack:
                stack.pop()
                if stack:
                    print(f"Página actual: {stack[-1]}")
                else:
                    print("Estás en la página de inicio.")
            else:
                print("No hay páginas anteriores.")
        else:
            stack.append(opcion)
            print(f"Página actual: {stack[-1]}")

navegador_web()
print("")  # Separador visual

"""
Simulación 2: Impresora compartida (Colas)
"""
# - Simula una impresora compartida usando una cola.
# - Operaciones disponibles:
#   * "imprimir": Imprime el documento más antiguo en la cola (dequeue).
#   * Cualquier otra entrada se considera como el nombre de un documento a agregar (enqueue).
# - Muestra siempre el estado actual de la cola de impresión.

def impresora_compartida():
    print("\n--- Impresora Compartida (Cola) ---")
    queue = []

    while True:
        opcion = input("Introduce un documento o escribe 'imprimir' o 'salir': ").strip().lower()

        if opcion == "salir":
            print("Saliendo del programa de impresión...")
            break
        elif opcion == "imprimir":
            if queue:
                print(f"Imprimiendo: {queue.pop(0)}")
            else:
                print("No hay documentos en la cola de impresión.")
        else:
            queue.append(opcion)
            print(f"Documento '{opcion}' añadido a la cola.")

        print(f"Cola de impresión actual: {queue}")

impresora_compartida()
