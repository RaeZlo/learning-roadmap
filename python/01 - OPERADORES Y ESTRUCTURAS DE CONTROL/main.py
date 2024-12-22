# Operadores aritméticos
print(f"Suma: 10 + 9 = {10 + 9}")
print(f"Resta: 10 - 11 = {10 - 11}")
print(f"Multiplicación: 10 * 2 = {10 * 2}")
print(f"División: 10 / 2 = {10 / 2}")
print(f"División entera: 10 // 2 = {10 // 2}")
print(f"Módulo: 10 % 2 = {10 % 2}")

print("")

# Operadores de comparación
print(f"Igualdad: 10 == 9 es {10 == 9}")
print(f"Desigualdad: 10 != 9 es {10 != 9}")
print(f"Mayor que: 10 > 9 es {10 > 9}")
print(f"Mayor o igual que: 10 >= 9 es {10 >= 9}")
print(f"Menor que: 10 < 9 es {10 < 9}")
print(f"Menor o igual que: 10 <= 9 es {10 <= 9}")

print("")

# Operadores lógicos
print(f"and: 10 == 9 and 9 == 8 {10 == 9 and 9 == 8}")
print(f"or: 10 == 9 or 9 == 9 {10 == 9 or 9 == 9}")
print(f"not: not 10 == 9 es {not 10 == 9}")

print("")

# Operadores de asignación
number = 11  # asignación
print(number)
number += 1  # suma y asignación
print(number)
number -= 1  # resta y asignación
print(number)
number *= 2  # multiplicación y asignación
print(number)
number /= 2  # división y asignación
print(number)
number %= 2  # módulo y asignación
print(number)
number **= 1  # exponente y asignación
print(number)
number //= 1  # división entera y asignación
print(number)

print("")

# Operadores de identidad
new_number = number
print(f"number is new_number es {number is new_number}")
print(f"number is not new_number es {number is not new_number}")

print("")

# Operadores de pertenencia
print(f"'z' in 'raezlo' = {'z' in 'raezlo'}")
print(f"'u' not in 'raezlo' = {'u' not in 'raezlo'}")

print("")

# Operadores de bit
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

print("")

# Estructuras de control

# Condicionales 
string = "pepe"

if string == 'pedro':
    print("el string es pedro")
elif string == 'escobar':
    print("el string es pepe")
else:
    print("el string no es pedro ni pepe")

print("")

# Bucles
for i in range(10, 26):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

print("")

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("se produjo un error")
finally:
    print("finalizacion de manejo de excepciones")

print("")

#Extra
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
