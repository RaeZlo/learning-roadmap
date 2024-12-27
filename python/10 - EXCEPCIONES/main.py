"""
Manejo de Excepciones en Python
"""
"""
1. Manejo de Excepciones:
   - Las excepciones son errores que ocurren durante la ejecución de un programa y que pueden interrumpir su flujo normal.
   - Python permite capturar y manejar excepciones utilizando bloques `try`, `except`, `else`, y `finally`.

2. Estructura Básica:
   - `try`: Contiene el código que podría generar una excepción.
   - `except`: Captura y maneja la excepción si ocurre.
   - `else`: Se ejecuta si no se produce ninguna excepción.
   - `finally`: Se ejecuta siempre, ocurra o no una excepción. Útil para liberar recursos o realizar acciones finales.
"""

# Ejemplo Básico: Manejo de errores comunes
try:
    lista = [10, 69, "pepe"]
    item = lista[4]  # Provocamos un error de índice
except IndexError as e:  # Capturamos el error específico
    print(f"Error: {e}")
finally:
    print("El bloque `finally` se ejecuta siempre.\n")

print()

try:
    division = 10 / 0  
except ZeroDivisionError as e:  
    print(f"Error: {e}")
else:
    print("La operación fue exitosa.")

"""
Extra
"""
# Excepción personalizada
class StrTypeError(Exception):
    """Excepción personalizada para manejar valores no permitidos."""
    pass

def process_params(parameters: list):
    """
    Procesa una lista de parámetros y lanza excepciones según su contenido.

    Reglas:
    - Si la lista tiene menos de 3 elementos, lanza un IndexError.
    - Si el segundo elemento es 0, lanza un ZeroDivisionError.
    - Si el tercer elemento es un string, lanza una StrTypeError.

    Args:
        parameters (list): Lista de parámetros a procesar.
    """
    # Validar que la lista tenga al menos 3 elementos
    if len(parameters) < 3:
        raise IndexError("La lista debe tener al menos 3 elementos.")
    
    # Validar que el segundo elemento no sea 0 (para evitar división por cero)
    elif parameters[1] == 0:
        raise ZeroDivisionError("El segundo elemento no puede ser 0.")
    
    # Validar que el tercer elemento no sea un string
    elif isinstance(parameters[2], str):
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto.")

    # Operaciones si no hay errores
    print(f"El tercer elemento es: {parameters[2]}")
    print(f"Resultado de la división: {parameters[0] / parameters[1]}")
    print(f"Suma con 5: {parameters[2] + 5}")


# Bloque principal para manejar las excepciones
try:
    # Probar con diferentes listas para observar el manejo de errores
    process_params([1, 2, 3, 4])  # Ejemplo sin errores
except IndexError as e:
    print(f"Error de índice: {e}")
except ZeroDivisionError as e:
    print(f"Error de división: {e}")
except StrTypeError as e:
    print(f"Error personalizado: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print("No se ha producido ningún error.")
finally:
    print("El programa finaliza sin detenerse.")
