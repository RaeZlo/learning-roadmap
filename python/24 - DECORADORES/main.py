"""
Patrón de Diseño: Decoradores
-----------------------------
Un decorador en Python es una función que modifica o extiende el comportamiento de otra función o método.
Se utiliza principalmente para añadir funcionalidades sin modificar directamente el código original.

Características de los Decoradores:
1. Son funciones que aceptan una función como entrada y devuelven otra función como salida.
2. Pueden usarse para añadir lógica antes o después de la ejecución de la función decorada.
3. Se implementan utilizando el símbolo `@` antes de la declaración de la función a decorar.
"""

# Decorador Genérico: Imprimir mensaje al llamar a una función
def print_call(function):
    """
    Decorador que imprime un mensaje cuando se llama a una función.
    """
    def wrapper_function():
        print(f"La función '{function.__name__}' ha sido llamada.")
        return function()  # Ejecuta la función decorada
    return wrapper_function

# Aplicación del decorador
@print_call
def example_function():
    print("Ejecutando example_function...")

@print_call
def example_function_2():
    print("Ejecutando example_function_2...")

@print_call
def example_function_3():
    print("Ejecutando example_function_3...")

# Llamadas a las funciones decoradas
example_function()
example_function_2()
example_function_3()

print("-" * 50)

"""
Dificultad Extra
----------------
Implementación de un decorador que cuente cuántas veces se ha llamado una función.
Este decorador es útil para monitorear la frecuencia de uso de ciertas funciones.
"""

def call_counter(function):
    """
    Decorador que cuenta las veces que se llama a una función.
    """
    def counter_function():
        counter_function.call_count += 1  # Incrementa el contador
        print(
            f"La función '{function.__name__}' se ha llamado {counter_function.call_count} veces."
        )
        return function()  # Ejecuta la función decorada

    counter_function.call_count = 0  # Inicializa el contador
    return counter_function

# Aplicación del decorador
@call_counter
def example_function_4():
    print("Ejecutando example_function_4...")

@call_counter
def example_function_5():
    print("Ejecutando example_function_5...")

# Llamadas a las funciones decoradas
example_function_4()
example_function_4()
example_function_4()
example_function_5()
example_function_4()
example_function_5()

"""
Conclusión:
-----------
Los decoradores son herramientas poderosas en Python para añadir funcionalidades de manera modular y reutilizable.
En este ejemplo, exploramos dos aplicaciones prácticas:
1. Imprimir un mensaje al llamar una función.
2. Contar cuántas veces se ha llamado a una función.
Estos patrones son comunes en frameworks y librerías, como Flask o Django.
"""
