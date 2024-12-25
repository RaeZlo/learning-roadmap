"""
Funciones definidas por el usuario en Python
"""
# Concepto:
# Las funciones permiten estructurar el código en bloques reutilizables. Pueden recibir parámetros y devolver valores,
# lo que las convierte en una herramienta esencial para resolver problemas complejos de forma modular.

# 1. Sin parámetros ni retorno
def greet():
    """Imprime un mensaje de bienvenida."""
    print("¡Bienvenido al mundo de Python!")

greet()

# 2. Con retorno
def return_greet():
    """Devuelve un mensaje de bienvenida."""
    return "¡Que tengas un excelente día aprendiendo Python!"

print(return_greet())

# 3. Con un argumento
def arg_greet(name):
    print(f"Hola, {name}, ¡bienvenido a la programación!")

arg_greet("Ana")

# 4. Con múltiples argumentos
def args_greet(greet, name):
    print(f"{greet}, {name}. ¡Es hora de aprender algo nuevo!")

args_greet("Hola", "Carlos")

# 5. Con un argumento predeterminado
def default_arg_greet(name="desarrollador"):
    print(f"Hola, {name}, ¡vamos a programar!")

default_arg_greet("María")
default_arg_greet()

# 6. Con múltiples argumentos y retorno
def return_args_greet(greet, name):
    return f"{greet}, {name}. ¡Hoy es un gran día para programar!"

print(return_args_greet("Hola", "Luis"))

# 7. Con retorno de múltiples valores
def multiple_return_greet():
    """Devuelve múltiples valores en un único retorno."""
    return "Buenos días", "equipo"

greet, group = multiple_return_greet()
print(greet)
print(group)

# 8. Con un número variable de argumentos
def variable_arg_greet(*topics):
    """Imprime una lista de temas utilizando un número variable de argumentos."""
    print("Hoy aprenderemos sobre:")
    for topic in topics:
        print(f"- {topic}")

variable_arg_greet("Funciones", "Bucles", "Condicionales", "Listas")

# 9. Con un número variable de argumentos con palabras clave
def variable_key_arg_greet(**student_details):
    """Imprime información de un estudiante usando argumentos con palabras clave."""
    print("Información del estudiante:")
    for key, value in student_details.items():
        print(f"{key}: {value}")

variable_key_arg_greet(
    nombre="Juan",
    nivel="Intermedio",
    lenguaje="Python",
    intereses="Automatización"
)

# --- Funciones dentro de funciones ---
def outer_function():
    def inner_function():
        print("Esto es una función dentro de otra función: ¡Sigue explorando!")
    inner_function()

outer_function()

# --- Funciones del lenguaje (built-in) ---
print(len("Pythonista"))  # Cuenta los caracteres en "Pythonista"
print(type(3.14))         # Muestra el tipo de dato (float)
print("aprende python".capitalize())  # Convierte la primera letra en mayúscula

# --- Variables locales y globales ---
global_var = "automatización"  # Variable global

def hello_python():
    local_var = "Aprendiendo"  # Variable local
    print(f"{local_var} sobre {global_var} con Python.")  # Combina ambas variables

print(global_var)  # Acceso a la variable global
# print(local_var)  # Esto daría un error, ya que no puede acceder a la variable local fuera de la función

hello_python()

"""
DIFICULTAD EXTRA
"""
def fizzbuzz(parametro1: str, parametro2: str) -> int:
    """
    Función FizzBuzz:
    Imprime números del 1 al 100 según las siguientes reglas:
    - Múltiplos de 3: Imprime `parametro1`.
    - Múltiplos de 5: Imprime `parametro2`.
    - Múltiplos de 3 y 5: Imprime `parametro1 + parametro2`.
    Retorna el número de veces que se imprimieron números en lugar de textos.
    """
    count = 0  # Contador de números impresos

    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(parametro1 + parametro2)
        elif number % 3 == 0:
            print(parametro1)
        elif number % 5 == 0:
            print(parametro2)
        else:
            print(number)
            count += 1

    return count  # Devuelve el total de números impresos

resultado = fizzbuzz("Fizz", "Buzz")
print(f"\nTotal de números impresos en lugar de textos: {resultado}")
