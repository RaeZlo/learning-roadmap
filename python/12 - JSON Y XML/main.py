"""
Manejo de Archivos XML y JSON en Python
"""
"""
1. Conceptos Básicos:
   -XML (eXtensible Markup Language):
     - Es un formato de texto estructurado utilizado para almacenar y transportar datos.
     - Los datos se representan como elementos anidados en una estructura jerárquica.
   -JSON (JavaScript Object Notation):
     - Es un formato de texto ligero para el intercambio de datos.
     - Utiliza pares clave-valor y estructuras como listas y objetos.
   - Ambos formatos son ampliamente utilizados en aplicaciones modernas para la persistencia y transporte de datos.
"""

import os
import xml.etree.ElementTree as xml
import json

# Datos iniciales
datos = {
    "nombre": "Rafael Perazzolo",
    "edad": 19,
    "fecha_nacimiento": "22-01-2005",
    "lenguajes_programacion": ["Python", "Java"]
}

# Archivos a crear
xml_file = "ejemplo.xml"
json_file = "ejemplo.json"

# Función para crear un archivo XML.
def crear_xml():
    root = xml.Element("data")  # Nodo raíz del XML

    # Iterar sobre los datos y generar nodos
    for key, value in datos.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):  # Para listas, crear subnodos
            for item in value:
                xml.SubElement(child, "item").text = item
        else:  # Para valores simples
            child.text = str(value)

    # Guardar el XML en un archivo
    tree = xml.ElementTree(root)
    tree.write(xml_file)

# Función para crear un archivo JSON.
def crear_json():
    with open(json_file, "w") as datos_json:
        json.dump(datos, datos_json)  # Serializar los datos como JSON

# Crear y mostrar el archivo XML
crear_xml()
print("\nContenido del archivo XML:")
with open(xml_file, "r") as datos_xml:
    print(datos_xml.read())

# Crear y mostrar el archivo JSON
crear_json()
print("\nContenido del archivo JSON:")
with open(json_file, "r") as datos_json:
    print(datos_json.read())

# Borrar los archivos
os.remove(xml_file)
os.remove(json_file)
print("\nArchivos XML y JSON eliminados.")

"""
Extra
"""
# Crear nuevamente los archivos para la dificultad extra
crear_xml()
crear_json()

# Clase personalizada para los datos
class Datos:
    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes_programacion):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes_programacion = lenguajes_programacion

# Leer datos desde XML y transformarlos en un objeto de la clase `Datos`
with open(xml_file, "r") as datos_xml:
    root = xml.fromstring(datos_xml.read())
    nombre = root.find("nombre").text
    edad = int(root.find("edad").text)
    fecha_nacimiento = root.find("fecha_nacimiento").text
    lenguajes_programacion = [item.text for item in root.find("lenguajes_programacion")]

    # Crear la instancia de la clase desde XML
    clase_xml = Datos(nombre, edad, fecha_nacimiento, lenguajes_programacion)
    print("\nDatos leídos desde XML:", clase_xml.__dict__)

# Leer datos desde JSON y transformarlos en un objeto de la clase `Datos`
with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)

    # Crear la instancia de la clase desde JSON
    clase_json = Datos(
        json_dict["nombre"],
        json_dict["edad"],
        json_dict["fecha_nacimiento"],
        json_dict["lenguajes_programacion"]
    )
    print("\nDatos leídos desde JSON:", clase_json.__dict__)

# Borrar los archivos
os.remove(xml_file)
os.remove(json_file)
print("\nArchivos XML y JSON eliminados tras la dificultad extra.")
