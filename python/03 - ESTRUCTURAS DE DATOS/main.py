"""
Listas
"""
# Las listas son estructuras de datos mutables que permiten almacenar elementos ordenados.
my_list = ["Rafa", "Voley", "Python"]
print("Lista inicial:", my_list)

# Inserción de un elemento al final de la lista
my_list.append("Java")
print("Después de append:", my_list)

# Eliminación de elementos por índice o valor
my_list.remove(my_list[0])  # Elimina "Rafa"
my_list.remove("Voley")  # Elimina "Voley"
print("Después de remove:", my_list)

# Acceso a un elemento por índice
print("Último elemento:", my_list[-1])

# Actualización de un elemento por índice
my_list[0] = "Gatos"
print("Después de actualizar el primer elemento:", my_list)

# Ordenación de la lista
my_list.sort()  # Los elementos deben ser del mismo tipo
print("Lista ordenada:", my_list)

# Tipo de dato
print("Tipo de estructura:", type(my_list))

print("")  # Separador visual

"""
Tuplas
"""
# Las tuplas son estructuras inmutables que permiten almacenar elementos ordenados.
my_tuple = ("Pedro", "María", "Yoel")
print("Tupla inicial:", my_tuple)

# Acceso a un elemento por índice
print("Primer elemento:", my_tuple[0])

# Ordenación de la tupla (se genera una nueva tupla ordenada)
my_tuple = tuple(sorted(my_tuple))
print("Tupla ordenada:", my_tuple)

print("")

"""
Conjuntos (Sets)
"""
# Los sets son estructuras mutables que almacenan elementos únicos y no están ordenados.
my_set = {"Pepe", "34", "Pelota"}
print("Set inicial:", my_set)

# Inserción de un elemento
my_set.add("pepe.com")
print("Después de add:", my_set)

# Eliminación de un elemento
my_set.remove("Pelota")
print("Después de remove:", my_set)

# Ordenación de un set (genera un set nuevo ordenado como lista)
my_set = set(sorted(my_set))
print("Set ordenado (convertido a lista y luego set):", my_set)

# Tipo de dato
print("Tipo de estructura:", type(my_set))

print("")

"""
Diccionarios
"""
# Los diccionarios son estructuras mutables que almacenan pares clave-valor.
my_dict = {
    "name": "Rafa",
    "surname": "Ramírez",
    "alias": "RaeZlo",
    "age": "19"
}
print("Diccionario inicial:", my_dict)

# Inserción de un nuevo par clave-valor
my_dict["email"] = "rafa@rafa.com"
print("Después de agregar 'email':", my_dict)

# Eliminación de un par clave-valor
del my_dict["surname"]
print("Después de eliminar 'surname':", my_dict)

# Acceso a un valor por su clave
print("Valor de 'name':", my_dict["name"])

# Actualización de un valor existente
my_dict["age"] = "20"
print("Después de actualizar 'age':", my_dict)

# Ordenación del diccionario por claves (genera un nuevo diccionario)
my_dict = dict(sorted(my_dict.items()))
print("Diccionario ordenado por claves:", my_dict)

# Tipo de dato
print("Tipo de estructura:", type(my_dict))

print("")

"""
Extra
"""
# Funcionalidad principal de la agenda: búsqueda, inserción, actualización y eliminación de contactos.

def agenda():
    # Estructura para almacenar los contactos
    agenda = {}

    # Función interna para insertar un nuevo contacto
    def insertar_contacto():
        telefono = input("Ingrese el teléfono que desea guardar: ")
        # Validación del teléfono
        if telefono.isdigit() and 0 < len(telefono) <= 10:
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' añadido correctamente.")
        else:
            print("Error: Debes ingresar un teléfono válido de máximo 10 dígitos.")

    while True:
        # Menú principal
        print("\n--- Agenda de Contactos ---")
        print("1. Buscar un contacto")
        print("2. Agregar un contacto")
        print("3. Actualizar un contacto")
        print("4. Eliminar un contacto")
        print("5. Salir")

        opcion = input("\nIngrese una opción: ")

        # Procesar la opción seleccionada
        match opcion:
            case "1":
                # Búsqueda de un contacto
                nombre = input("Ingrese el nombre del contacto: ")
                if nombre in agenda:
                    print(f"El número de teléfono de {nombre} es {agenda[nombre]}.")
                else:
                    print(f"El contacto '{nombre}' no existe.")
            case "2":
                # Inserción de un contacto
                nombre = input("Ingrese el nombre del contacto: ")
                insertar_contacto()
            case "3":
                # Actualización de un contacto existente
                nombre = input("Introduce el nombre del contacto a actualizar: ")
                if nombre in agenda:
                    print(f"Contacto encontrado. Número actual: {agenda[nombre]}")
                    insertar_contacto()
                else:
                    print(f"El contacto '{nombre}' no existe.")
            case "4":
                # Eliminación de un contacto
                nombre = input("Introduce el nombre del contacto a eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                    print(f"El contacto '{nombre}' ha sido eliminado.")
                else:
                    print(f"El contacto '{nombre}' no existe.")
            case "5":
                # Finalización del programa
                print("Saliendo de la agenda... ¡Adiós!")
                break
            case _:
                # Opción no válida
                print("Error: Opción no válida. Por favor, elige una opción del 1 al 5.")

# Ejecutar la agenda
agenda()
