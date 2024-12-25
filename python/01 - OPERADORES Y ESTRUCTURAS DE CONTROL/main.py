"""
Operadores y Estructuras de Control en Python
"""
# Concepto General:
# Los operadores y las estructuras de control son fundamentales para la manipulación de datos 
# y el flujo lógico de los programas. Esta sección incluye ejemplos para comprender los tipos 
# de operadores disponibles y cómo usarlos, junto con ejemplos de control de flujo y manejo de excepciones.

# --- Operadores Aritméticos ---
# Usados para realizar cálculos matemáticos básicos.
print("Operadores Aritméticos:")
print(f"Suma: 10 + 9 = {10 + 9}")
print(f"Resta: 10 - 11 = {10 - 11}")
print(f"Multiplicación: 10 * 2 = {10 * 2}")
print(f"División: 10 / 2 = {10 / 2}")
print(f"División entera: 10 // 2 = {10 // 2}")
print(f"Módulo: 10 % 2 = {10 % 2}")
print("")

# --- Operadores de Comparación ---
# Evalúan relaciones entre valores.
print("Operadores de Comparación:")
print(f"Igualdad: 10 == 9 es {10 == 9}")
print(f"Desigualdad: 10 != 9 es {10 != 9}")
print(f"Mayor que: 10 > 9 es {10 > 9}")
print(f"Mayor o igual que: 10 >= 9 es {10 >= 9}")
print(f"Menor que: 10 < 9 es {10 < 9}")
print(f"Menor o igual que: 10 <= 9 es {10 <= 9}")
print("")

# --- Operadores Lógicos ---
# Combinan expresiones lógicas.
print("Operadores Lógicos:")
print(f"and: 10 == 9 and 9 == 8 es {10 == 9 and 9 == 8}")
print(f"or: 10 == 9 or 9 == 9 es {10 == 9 or 9 == 9}")
print(f"not: not 10 == 9 es {not 10 == 9}")
print("")

# --- Operadores de Asignación ---
# Usados para actualizar valores.
print("Operadores de Asignación:")
number = 11
print(f"Asignación inicial: {number}")
number += 1
print(f"Suma y asignación: {number}")
number -= 1
print(f"Resta y asignación: {number}")
number *= 2
print(f"Multiplicación y asignación: {number}")
number /= 2
print(f"División y asignación: {number}")
number %= 2
print(f"Módulo y asignación: {number}")
print("")

# --- Operadores de Identidad ---
# Comparan referencias en memoria.
print("Operadores de Identidad:")
new_number = number
print(f"number is new_number: {number is new_number}")
print(f"number is not new_number: {number is not new_number}")
print("")

# --- Operadores de Pertenencia ---
# Comprueban si un elemento pertenece a una colección.
print("Operadores de Pertenencia:")
print(f"'z' in 'raezlo': {'z' in 'raezlo'}")
print(f"'u' not in 'raezlo': {'u' not in 'raezlo'}")
print("")

# --- Operadores de Bits ---
# Operan a nivel binario.
print("Operadores de Bits:")
a = 10  # 1010 en binario
b = 3   # 0011 en binario
print(f"AND: 10 & 3 = {a & b}")
print(f"OR: 10 | 3 = {a | b}")
print(f"XOR: 10 ^ 3 = {a ^ b}")
print(f"NOT: ~10 = {~a}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {a >> 2}")
print(f"Desplazamiento a la izquierda: 10 << 2 = {a << 2}")
print("")

# --- Estructuras de Control ---
# Permiten dirigir el flujo lógico del programa.
print("Estructuras de Control:")

# Condicionales
string = "pepe"
if string == 'pedro':
    print("El string es pedro")
elif string == 'pepe':
    print("El string es pepe")
else:
    print("El string no es pedro ni pepe")
print("")

# Bucles
print("Bucle for:")
for i in range(10, 26):  # Desde 10 hasta 25
    print(i)

print("Bucle while:")
i = 0
while i <= 10:
    print(i)
    i += 1
print("")

# --- Manejo de Excepciones ---
# Permite controlar errores en tiempo de ejecución.
print("Manejo de Excepciones:")
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Se produjo un error de división por cero")
finally:
    print("Finalización de manejo de excepciones")
print("")

"""
Dificultad Extra: Números entre 10 y 55
"""
# Filtra números con condiciones específicas.
print("Dificultad Extra:")
print("Números entre 10 y 55 que son pares, no son 16 y no son múltiplos de 3:")
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
