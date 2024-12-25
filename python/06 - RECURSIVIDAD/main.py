"""
Recursividad
"""
# Concepto:
# La recursividad es una técnica de programación donde una función se llama a sí misma 
# para resolver un problema dividiéndolo en partes más pequeñas del mismo tipo.
# Cada llamada recursiva debe reducir el problema hacia un caso base para evitar 
# un bucle infinito.

# Cuándo usar recursividad:
# - Cuando el problema tiene una estructura repetitiva o jerárquica, como árboles, gráficos o listas anidadas.
# - Para problemas que se pueden dividir en subproblemas similares.
# - Cuando un algoritmo iterativo sería menos intuitivo o más complejo de implementar.

def cuenta_atras(numero: int):
    """
    Imprime los números del valor recibido hasta 0 de forma recursiva.
    
    :param numero: Número desde el que inicia la cuenta regresiva.
    """
    if numero >= 0:
        print(numero)
        cuenta_atras(numero - 1)

print("Cuenta regresiva del 100 al 0:")
cuenta_atras(100)

"""
DIFICULTAD EXTRA
"""
def factorial(numero: int) -> int:
    """
    Calcula el factorial de un número de forma recursiva.
    
    :param numero: Número del que se calculará el factorial.
    :return: Factorial del número dado.
    """
    if numero < 0:
        print("No se permiten números negativos.")
        return 0
    elif numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

numero_factorial = 5
print(f"\nEl factorial de {numero_factorial} es: {factorial(numero_factorial)}")

def fibonacci(posicion: int) -> int:
    """
    Calcula el valor de un elemento específico en la sucesión de Fibonacci.
    
    :param posicion: Posición en la sucesión (1-indexada).
    :return: Valor correspondiente en la sucesión.
    """
    if posicion <= 0:
        print("No se admiten posiciones negativas o cero.")
        return 0
    elif posicion == 1:
        return 0
    elif posicion == 2:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

posicion_fibonacci = 6
print(f"\nEl valor en la posición {posicion_fibonacci} de la sucesión de Fibonacci es: {fibonacci(posicion_fibonacci)}")
