"""
Operaciones con Cadenas de Caracteres
"""

# Ejemplo base
s1 = "Mundo"
s2 = "Programación"
s3 = "Juan Pérez @devjuan"

"""
Concatenación
"""
print(f"Concatenación: {s1 + ', ' + s2 + '!'}")

"""
Repetición
"""
print(f"Repetición: {s1 * 2}")

"""
Indexación
"""
print(f"Indexación: {s1[0]}, {s1[1]}, {s1[2]}, {s1[3]}")

"""
Longitud
"""
print(f"Longitud: {len(s2)}")

"""
Slicing (porción)
"""
print(f"Subcadena (índice 1 a 5): {s2[1:5]}")
print(f"Subcadena desde índice 3: {s2[3:]}")
print(f"Subcadena hasta índice 4: {s2[:4]}")

"""
Búsqueda de caracteres o subcadenas
"""
print(f"¿'u' en {s1}? {'u' in s1}")
print(f"¿'z' en {s1}? {'z' in s1}")

"""
Reemplazo
"""
print(f"Reemplazo: {s1.replace('u', 'a')}")

"""
División
"""
print(f"División: {s2.split('a')}")

"""
Mayúsculas, minúsculas y formatos de texto
"""
print(f"Mayúsculas: {s1.upper()}")
print(f"Minúsculas: {s1.lower()}")
print(f"Formato título: {'carlos ruiz'.title()}")
print(f"Primera letra en mayúscula: {'carlos ruiz'.capitalize()}")

"""
Eliminación de espacios
"""
print(f"Sin espacios: {' curso de python '.strip()}")

"""
Búsqueda al principio y al final
"""
print(f"¿Empieza con 'Mu'? {s1.startswith('Mu')}")
print(f"¿Termina con 'do'? {s1.endswith('do')}")

"""
Búsqueda de posición
"""
print(f"Posición de 'Pérez': {s3.find('Pérez')}")
print(f"Posición de '@': {s3.find('@')}")
print(f"Posición de 'j' (case insensitive): {s3.lower().find('j')}")

"""
Búsqueda de ocurrencias
"""
print(f"Número de ocurrencias de 'e': {s3.lower().count('e')}")

"""
Formateo
"""
print(f"Formateo con format(): {'Palabra 1: {}, palabra 2: {}!'.format(s1, s2)}")
print(f"Interpolación: Palabra 1: {s1}, palabra 2: {s2}!")

"""
Transformación en lista de caracteres
"""
print(f"Lista de caracteres: {list(s3)}")

"""
Transformación de lista en cadena
"""
l1 = [s1, ", ", s2, "!"]
print(f"Lista a cadena: {''.join(l1)}")

"""
Transformaciones numéricas
"""
s4 = "789456"
s5 = "789456.123"
print(f"Transformación a entero: {int(s4)}")
print(f"Transformación a flotante: {float(s5)}")

"""
Comprobaciones varias
"""
print(f"¿Es alfanumérico?: {s1.isalnum()}")
print(f"¿Solo contiene letras?: {s2.isalpha()}")
print(f"¿Solo contiene números?: {s4.isnumeric()}")

"""
Extra
"""

def check_word(word1:str, word2:str) -> str:
   
    # Palíndromo
    print(f"{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas
    def isogram(word: str) -> bool:

            word_dict = dict()
            for character in word:
                word_dict[character] = word_dict.get(character, 0) + 1

            isogram = True
            values = list(word_dict.values())
            isogram_len = values[0]
            for word_count in values:
                if word_count != isogram_len:
                    isogram = False
                    break

            return isogram

    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")

check_word("radar", "pelota")
check_word("amor", "roma")
