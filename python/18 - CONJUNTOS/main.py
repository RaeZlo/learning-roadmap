"""
Conjuntos en Python
"""
"""
Los conjuntos son colecciones no ordenadas de elementos únicos.
Se usan para realizar operaciones matemáticas como unión, intersección y diferencia.
"""
data = [1, 2, 3, 4, 5]
print(f"Estructura inicial: {data}")

# Añadir un elemento al final de la lista
data.append(6)
print(f"Añadiendo elemento al final: {data}")

# Añadir un elemento al principio de la lista
data.insert(0, 0)
print(f"Añadiendo elemento al principio: {data}")

# Añadir varios elementos al final de la lista
data.extend([7, 8, 9])
print(f"Añadiendo elementos al final: {data}")

# Añadir varios elementos en una posición concreta
data[3:3] = [-1, -2, -3]
print(f"Añadiendo elementos en una posición: {data}")

# Eliminar un elemento en una posición concreta
del data[3]
print(f"Eliminando un elemento concreto: {data}")

# Actualizar el valor de un elemento en una posición concreta
data[4] = -1
print(f"Actualizando un elemento concreto: {data}")

# Comprobar si un elemento está en la lista
print(f"Comprobar si un elemento existe (-1): {-1 in data}")

# Eliminar todo el contenido de la lista
data.clear()
print(f"Eliminar el contenido: {data}")

"""
Extra
"""
# Inicializamos dos conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7}

# Unión de dos conjuntos
union = conjunto1.union(conjunto2)
print(f"Unión: {union}")

# Intersección de dos conjuntos
interseccion = conjunto1.intersection(conjunto2)
print(f"Intersección: {interseccion}")

# Diferencia entre dos conjuntos
diferencia1 = conjunto1.difference(conjunto2)
diferencia2 = conjunto2.difference(conjunto1)
print(f"Diferencia (conjunto1 - conjunto2): {diferencia1}")
print(f"Diferencia (conjunto2 - conjunto1): {diferencia2}")

# Diferencia simétrica entre dos conjuntos
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(f"Diferencia simétrica: {diferencia_simetrica}")
