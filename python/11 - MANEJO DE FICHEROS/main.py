"""
Manejo de Ficheros en Python
"""
"""
   - En Python, se puede trabajar con archivos para leer, escribir, modificar o eliminar información almacenada en ellos.
   - Las operaciones con ficheros se realizan utilizando funciones incorporadas como `open()`, `read()`, `write()`, y `close()`.
   - Modos comunes de apertura:
       - `r`: Modo de lectura.
       - `w`: Modo de escritura (sobrescribe el archivo si existe).
       - `a`: Modo de agregar texto al final del archivo.
       - `r+`: Lectura y escritura.
"""
import os  # Para operaciones con el sistema de archivos

# Parte 1: Creación y manejo básico de un archivo
file_name = "RaeZlo.txt"

# Crear y escribir en el archivo
with open(file_name, "w") as file:
    file.write("Rafael Perazzolo\n")
    file.write("19\n")
    file.write("Python")

# Leer el contenido del archivo
with open(file_name, "r") as file:
    print("Contenido del archivo:")
    print(file.read())

# Eliminar el archivo
os.remove(file_name)
print("\nEl archivo ha sido eliminado.")

"""
Extra
"""
# Nombre del archivo para almacenar datos de ventas
file_name = "shop.txt"

# Crear el archivo vacío
open(file_name, "a").close()

# Bucle principal del programa
while True:
    # Menú de opciones
    print("\nGestión de Ventas")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    # Capturar la opción seleccionada por el usuario
    option = input("\nSelecciona una opción: ")

    # Manejo de las opciones con `match-case`
    match option:
        case "1":
            # Añadir un nuevo producto
            nombre = input("Nombre del producto: ")
            cantidad = input("Cantidad vendida: ")
            precio = input("Precio del producto: ")

            # Escribir el producto en el archivo
            with open(file_name, "a") as file:
                file.write(f"{nombre}, {cantidad}, {precio}\n")
            print("Producto añadido con éxito.")

        case "2":
            # Consultar un producto por su nombre
            nombre = input("Nombre del producto a consultar: ")
            encontrado = False
            with open(file_name, "r") as file:
                for line in file:
                    if line.startswith(nombre):
                        print(f"Producto encontrado: {line.strip()}")
                        encontrado = True
                        break
            if not encontrado:
                print("Producto no encontrado.")

        case "3":
            # Actualizar un producto existente
            nombre = input("Nombre del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad: ")
            nuevo_precio = input("Nuevo precio: ")

            with open(file_name, "r") as file:
                lines = file.readlines()

            # Sobreescribir el archivo con los datos actualizados
            with open(file_name, "w") as file:
                for line in lines:
                    if line.startswith(nombre):
                        file.write(f"{nombre}, {nueva_cantidad}, {nuevo_precio}\n")
                    else:
                        file.write(line)
            print("Producto actualizado con éxito.")

        case "4":
            # Borrar un producto
            nombre = input("Nombre del producto a borrar: ")
            with open(file_name, "r") as file:
                lines = file.readlines()

            # Escribir nuevamente excluyendo el producto a borrar
            with open(file_name, "w") as file:
                for line in lines:
                    if not line.startswith(nombre):
                        file.write(line)
            print("Producto borrado con éxito.")

        case "5":
            # Mostrar todos los productos
            print("Productos en inventario:")
            with open(file_name, "r") as file:
                print(file.read().strip())

        case "6":
            # Calcular la venta total
            total = 0
            with open(file_name, "r") as file:
                for line in file:
                    _, cantidad, precio = line.strip().split(", ")
                    total += int(cantidad) * float(precio)
            print(f"Venta total: ${total:.2f}")

        case "7":
            # Calcular venta por producto
            nombre = input("Nombre del producto: ")
            total = 0
            encontrado = False
            with open(file_name, "r") as file:
                for line in file:
                    if line.startswith(nombre):
                        _, cantidad, precio = line.strip().split(", ")
                        total = int(cantidad) * float(precio)
                        encontrado = True
                        break
            if encontrado:
                print(f"Venta total de {nombre}: ${total:.2f}")
            else:
                print("Producto no encontrado.")

        case "8":
            # Salir del programa y eliminar el archivo
            os.remove(file_name)
            print("Saliendo del programa. Archivo eliminado.")
            break

        case _:
            print("Opción no válida. Por favor, elige una opción entre 1 y 8.")
