"""
Concepto de Expresiones Regulares (RegEx)
"""
"""
Las expresiones regulares son patrones utilizados para buscar y manipular cadenas de texto.
Son útiles para validar formatos, extraer información y realizar búsquedas complejas.

En Python, se utiliza el módulo `re` para trabajar con expresiones regulares.
Principales funciones:
   - `re.findall(pattern, string)`: Encuentra todas las coincidencias de un patrón en una cadena.
   - `re.match(pattern, string)`: Comprueba si una cadena coincide con un patrón desde el inicio.
   - `re.search(pattern, string)`: Busca la primera coincidencia de un patrón en una cadena.
   - `re.sub(pattern, replacement, string)`: Reemplaza todas las coincidencias del patrón con un texto dado.
"""

import re

def encontrar_numeros(frase: str):
    return re.findall(r"\d+", frase)

# Ejemplo de uso
print(encontrar_numeros("Es lunes 30/12/24. Estoy haciendo el ejercicio 16 de Python"))

"""
Extra
"""
def validar_email(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))

# Ejemplo de uso
print(validar_email("pepe@gmail.com"))  # True
print(validar_email("pepe.gmail.com"))  # False

def validar_telefono(telefono: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", telefono))

# Ejemplo de uso
print(validar_telefono("+34 901 65 89 04"))  # True
print(validar_telefono("911"))               # True
print(validar_telefono("abc"))               # False

def validar_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www\.)?[\w]+\.[a-zA-Z]{2,}(/)?$", url))

# Ejemplo de uso
print(validar_url("https://www.python.org/"))  # True
print(validar_url("http:/python.org"))         # False
print(validar_url("www.python.org"))           # False

"""
Explicación de las Expresiones Regulares:
-----------------------------------------
1. Extraer números: `r"\d+"`
    - `\d`: Coincide con cualquier dígito.
    - `+`: Uno o más dígitos consecutivos.

2. Validar email: `r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$"`
    - `[\w.+-]+`: Coincide con letras, números, puntos, guiones y guiones bajos.
    - `@`: Debe incluir un símbolo arroba.
    - `[\w]+`: Nombre del dominio.
    - `\.`: Debe incluir un punto antes del dominio.
    - `[a-zA-Z]+`: Extensión del dominio (letras).

3. Validar teléfono: `r"^\+?[\d\s]{3,}$"`
    - `\+?`: Puede comenzar con un símbolo `+`.
    - `[\d\s]{3,}`: Tres o más dígitos o espacios.

4. Validar URL: `r"^http[s]?://(www\.)?[\w]+\.[a-zA-Z]{2,}(/)?$"`
    - `http[s]?`: Debe comenzar con `http` o `https`.
    - `(www\.)?`: Puede incluir `www.` opcionalmente.
    - `[\w]+`: Nombre del dominio.
    - `\.[a-zA-Z]{2,}`: Punto seguido de al menos dos letras.
    - `(/)?`: Puede terminar con una barra `/` opcionalmente.
"""
