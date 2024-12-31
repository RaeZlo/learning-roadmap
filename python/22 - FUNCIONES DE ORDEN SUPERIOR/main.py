"""
Concepto de Funciones de Orden Superior
"""
"""
Una función de orden superior es aquella que cumple con al menos una de las siguientes condiciones:
1. Recibe una o más funciones como argumento(s).
2. Retorna una función como resultado.

Este tipo de funciones son útiles para simplificar tareas repetitivas y trabajar con datos de forma más expresiva.
"""

from functools import reduce
from datetime import datetime

# Ejemplo de función de orden superior como argumento
def apply_func(func, x):
    """
    Aplica una función `func` al valor `x` y retorna el resultado.
    """
    return func(x)

print("Aplicando función 'len' a una cadena:")
print(apply_func(len, "MoureDev"))  # Resultado: 8
print("-" * 50)

# Ejemplo de función de orden superior que retorna otra función
def apply_multiplier(n):
    """
    Retorna una función que multiplica un valor por `n`.
    """
    def multiplier(x):
        return x * n
    return multiplier

print("Aplicando funciones generadas dinámicamente:")
multiplier = apply_multiplier(2)  # Genera una función que multiplica por 2
print(multiplier(5))  # Resultado: 10
print(apply_multiplier(3)(2))  # Resultado: 6
print("-" * 50)

# Aplicaciones prácticas con listas
numbers = [1, 3, 4, 2, 5]

# Usando map() para transformar elementos
def apply_double(n):
    """
    Doble del valor `n`.
    """
    return n * 2

print("Usando map para duplicar valores en una lista:")
print(list(map(apply_double, numbers)))  # Resultado: [2, 6, 8, 4, 10]
print("-" * 50)

# Usando filter() para filtrar elementos
def is_even(n):
    """
    Determina si `n` es par.
    """
    return n % 2 == 0

print("Usando filter para obtener solo números pares:")
print(list(filter(is_even, numbers)))  # Resultado: [4, 2]
print("-" * 50)

# Usando sorted() para ordenar elementos
print("Ordenando una lista:")
print("Ascendente:", sorted(numbers))  # Resultado: [1, 2, 3, 4, 5]
print("Descendente:", sorted(numbers, reverse=True))  # Resultado: [5, 4, 3, 2, 1]
print("Orden inverso con clave lambda:", sorted(numbers, key=lambda x: -x))  # Resultado: [5, 4, 3, 2, 1]
print("-" * 50)

# Usando reduce() para agregar valores
def sum_values(x, y):
    """
    Retorna la suma de `x` e `y`.
    """
    return x + y

print("Usando reduce para sumar todos los valores de la lista:")
print(reduce(sum_values, numbers))  # Resultado: 15
print("-" * 50)

"""
Extra
"""
students = [
    {"name": "Brais", "birthdate": "29-04-1987", "grades": [5, 8.5, 3, 10]},
    {"name": "Moure", "birthdate": "04-08-1995", "grades": [1, 9.5, 2, 4]},
    {"name": "MoureDev", "birthdate": "15-12-2000", "grades": [4, 6.5, 5, 2]},
    {"name": "SuperMoureDev", "birthdate": "25-01-1980", "grades": [10, 9, 9.7, 9.9]}
]

# Promedio de calificaciones por estudiante
def average(grades):
    """
    Calcula el promedio de una lista de calificaciones.
    """
    return sum(grades) / len(grades)

print("Promedio de calificaciones por estudiante:")
print(
    list(
        map(lambda student: {
            "name": student["name"],
            "average": average(student["grades"])
        }, students)
    )
)
print("-" * 50)

# Filtrar estudiantes con promedio mayor o igual a 9
print("Estudiantes con promedio mayor o igual a 9:")
print(
    list(
        map(
            lambda student: student["name"],
            filter(lambda student: average(student["grades"]) >= 9, students)
        )
    )
)
print("-" * 50)

# Ordenar estudiantes por fecha de nacimiento (más reciente primero)
print("Estudiantes ordenados por fecha de nacimiento (recientes primero):")
print(
    sorted(
        students,
        key=lambda student: datetime.strptime(student["birthdate"], "%d-%m-%Y"),
        reverse=True
    )
)
print("-" * 50)

# Calificación más alta entre todos los estudiantes
print("Calificación más alta entre todos los estudiantes:")
print(max(map(lambda student: max(student["grades"]), students)))  # Resultado: 10
print("-" * 50)
