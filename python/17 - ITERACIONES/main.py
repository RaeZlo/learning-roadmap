"""
Iteración en Python
"""
"""
La iteración es el proceso de recorrer una secuencia (lista, tupla, diccionario, etc.) o de repetir un bloque de código varias veces.
Python ofrece múltiples mecanismos para iterar valores, desde estructuras básicas hasta enfoques más avanzados y creativos.
"""

# 3 MECANISMOS PARA IMPRIMIR NÚMEROS DEL 1 AL 10

# 1. Utilizando un bucle `for` con `range`
for number in range(1, 11):
    print(number)

print("")  # Espaciado

# 2. Utilizando un bucle `while`
count = 1
while count <= 10:
    print(count)
    count += 1

print("")  # Espaciado

# 3. Utilizando recursividad
def print_number(number=1):
    if number <= 10:
        print(number)
        print_number(number + 1)

print_number()

"""
Extra
"""
print("\nMECANISMOS ADICIONALES PARA ITERAR VALORES\n")

# 4. Iterando sobre una lista
for i in [19, 20, 18, 54]:
    print(i)

# 5. Iterando sobre una tupla
for i in (19, 20, 18, 54):
    print(i)

# 6. Iterando sobre las claves de un diccionario
for i in {1: "a", 2: "b", 3: "c", 4: "d"}:
    print(i)

# 7. Iterando sobre los valores de un diccionario
for i in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(i)

# 8. Usando una lista por comprensión con `*` y `sep`
print(*[i for i in range(1, 11)], sep="\n")

# 9. Iterando sobre una cadena de texto
for c in "Python":
    print(c)

# 10. Iterando en orden inverso
for e in reversed([1, 2, 3, 4]):
    print(e)

# 11. Iterando en orden alfabético
for e in sorted(["r", "a", "f", "a", "e", "l"]):
    print(e)

# 12. Usando `enumerate` para obtener índice y valor
for i, e in enumerate(sorted(["r", "a", "f", "a", "e", "l"])):
    print(f"Índice: {i}, valor: {e}")
