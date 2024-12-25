"""
Estructuras de datos en Python
"""

"""
Listas
"""
# - Son estructuras de datos MUTABLES.
# - Permiten almacenar elementos ordenados que pueden repetirse.
# - Admiten operaciones de inserción, eliminación, actualización y ordenación.

# Ejemplo básico de lista:
my_list = ["Rafa", "Voley", "Python"]
print("Lista inicial:", my_list)

# Inserción:
my_list.append("Java")  # Agrega un elemento al final.
print("Después de append:", my_list)

# Eliminación:
my_list.remove("Voley")  # Elimina un elemento por valor.
print("Después de remove:", my_list)

# Actualización:
my_list[0] = "Gatos"  # Cambia el primer elemento.
print("Después de actualizar:", my_list)

# Ordenación:
my_list.sort()  # Ordena los elementos en orden ascendente.
print("Lista ordenada:", my_list)

# Tipo de dato:
print("Tipo de estructura:", type(my_list))
print("")  # Separador visual

"""
Tuplas
"""
# - Son estructuras de datos INMUTABLES.
# - Permiten almacenar elementos ordenados, pero no pueden modificarse una vez creadas.
# - Útiles para datos constantes o que no deben cambiar.

# Ejemplo básico de tupla:
my_tuple = ("Pedro", "María", "Yoel")
print("Tupla inicial:", my_tuple)

# Acceso:
print("Primer elemento:", my_tuple[0])

# Ordenación:
sorted_tuple = tuple(sorted(my_tuple))  # Devuelve una nueva tupla ordenada.
print("Tupla ordenada:", sorted_tuple)

# Tipo de dato:
print("Tipo de estructura:", type(my_tuple))
print("")

"""
Conjuntos (Sets)
"""
# - Son estructuras MUTABLES y NO ORDENADAS.
# - Almacenan elementos únicos (no permiten duplicados).
# - Útiles para operaciones de conjuntos (unión, intersección, diferencia).

# Ejemplo básico de conjunto:
my_set = {"Pepe", "34", "Pelota"}
print("Set inicial:", my_set)

# Inserción:
my_set.add("Pythonista")  # Agrega un nuevo elemento.
print("Después de add:", my_set)

# Eliminación:
my_set.remove("Pelota")  # Elimina un elemento.
print("Después de remove:", my_set)

# Ordenación:
sorted_set = set(sorted(my_set))  # Ordena y genera un nuevo set.
print("Set ordenado (convertido a lista y luego set):", sorted_set)

# Tipo de dato:
print("Tipo de estructura:", type(my_set))
print("")

"""
Diccionarios
"""
# - Son estructuras MUTABLES que almacenan pares clave-valor.
# - Cada clave debe ser única.
# - Permiten acceso directo a los valores mediante sus claves.

# Ejemplo básico de diccionario:
my_dict = {
    "name": "Rafa",
    "surname": "Ramírez",
    "alias": "RaeZlo",
    "age": "19"
}
print("Diccionario inicial:", my_dict)

# Inserción:
my_dict["email"] = "rafa@rafa.com"  # Agrega un nuevo par clave-valor.
print("Después de agregar 'email':", my_dict)

# Eliminación:
del my_dict["surname"]  # Elimina un par clave-valor.
print("Después de eliminar 'surname':", my_dict)

# Acceso:
print("Valor de 'name':", my_dict["name"])  # Accede al valor asociado a la clave "name".

# Actualización:
my_dict["age"] = "20"  # Cambia el valor asociado a la clave "age".
print("Después de actualizar 'age':", my_dict)

# Ordenación:
sorted_dict = dict(sorted(my_dict.items()))  # Ordena por claves y genera un nuevo diccionario.
print("Diccionario ordenado por claves:", sorted_dict)

# Tipo de dato:
print("Tipo de estructura:", type(my_dict))
print("")

"""
Dificultad Extra: Agenda de Contactos
"""
def agenda():
    """
    Implementación de una agenda de contactos que permite:
    - Buscar contactos.
    - Agregar contactos.
    - Actualizar contactos existentes.
    - Eliminar contactos.
    - Validar que los números de teléfono sean numéricos y de longitud máxima definida.
    """
    # Estructura para almacenar los contactos:
    contactos = {}

    while True:
        # Menú principal
        print("\n--- Agenda de Contactos ---")
        print("1. Buscar un contacto")
        print("2. Agregar un contacto")
        print("3. Actualizar un contacto")
        print("4. Eliminar un contacto")
        print("5. Salir")

        opcion = input("\nElige una opción: ")

        # Procesar la opción seleccionada
        if opcion == "1":
            # Buscar un contacto
            nombre = input("Introduce el nombre del contacto: ")
            if nombre in contactos:
                print(f"El número de {nombre} es {contactos[nombre]}.")
            else:
                print(f"El contacto '{nombre}' no existe.")
        elif opcion == "2":
            # Agregar un contacto
            nombre = input("Introduce el nombre del contacto: ")
            telefono = input("Introduce el número de teléfono: ")
            if telefono.isdigit() and len(telefono) <= 11:
                contactos[nombre] = telefono
                print(f"Contacto '{nombre}' añadido con éxito.")
            else:
                print("Error: El teléfono debe ser numérico y de máximo 11 dígitos.")
        elif opcion == "3":
            # Actualizar un contacto
            nombre = input("Introduce el nombre del contacto a actualizar: ")
            if nombre in contactos:
                telefono = input("Introduce el nuevo número de teléfono: ")
                if telefono.isdigit() and len(telefono) <= 11:
                    contactos[nombre] = telefono
                    print(f"Contacto '{nombre}' actualizado.")
                else:
                    print("Error: El teléfono debe ser numérico y de máximo 11 dígitos.")
            else:
                print(f"El contacto '{nombre}' no existe.")
        elif opcion == "4":
            # Eliminar un contacto
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            if nombre in contactos:
                del contactos[nombre]
                print(f"Contacto '{nombre}' eliminado.")
            else:
                print(f"El contacto '{nombre}' no existe.")
        elif opcion == "5":
            # Salir
            print("Saliendo de la agenda... ¡Adiós!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

agenda()
