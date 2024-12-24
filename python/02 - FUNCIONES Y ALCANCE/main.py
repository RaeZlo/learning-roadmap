"""
Funciones definidas por el usuario
"""

# Sin parámetros ni retorno
def greet():
    print("¡Bienvenido al mundo de Python!") 

greet()

# Con retorno
def return_greet():
    return "¡Que tengas un excelente día aprendiendo Python!"  

print(return_greet())

# Con un argumento
def arg_greet(name):
    print(f"Hola, {name}, ¡bienvenido a la programación!")  

arg_greet("Ana")

# Con múltiples argumentos
def args_greet(greet, name):
    print(f"{greet}, {name}. ¡Es hora de aprender algo nuevo!")  

args_greet("Hola", "Carlos")
# args_greet(name="Carlos", greet="Hey")  # Uso de argumentos con nombre

# Con un argumento predeterminado
def default_arg_greet(name="desarrollador"):
    print(f"Hola, {name}, ¡vamos a programar!") 

default_arg_greet("María")
default_arg_greet()

# Con múltiples argumentos y retorno
def return_args_greet(greet, name):
    return f"{greet}, {name}. ¡Hoy es un gran día para programar!" 

print(return_args_greet("Hola", "Luis"))

# Con retorno de múltiples valores
def multiple_return_greet():
    return "Buenos días", "equipo"  

greet, group = multiple_return_greet()
print(greet)
print(group)

# Con un número variable de argumentos
def variable_arg_greet(*topics):
    print("Hoy aprenderemos sobre:")
    for topic in topics:
        print(f"- {topic}")  

variable_arg_greet("Funciones", "Bucles", "Condicionales", "Listas")

# Con un número variable de argumentos con palabras clave
def variable_key_arg_greet(**student_details):
    print("Información del estudiante:")
    for key, value in student_details.items():
        print(f"{key}: {value}")  

variable_key_arg_greet(
    nombre="Juan",
    nivel="Intermedio",
    lenguaje="Python",
    intereses="Automatización"
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Esto es una función dentro de otra función: ¡Sigue explorando!")
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in)
"""

print(len("Pythonista"))  # Cuenta los caracteres en "Pythonista"
print(type(3.14))         # Muestra el tipo de dato (float)
print("aprende python".capitalize())  # Convierte la primera letra en mayúscula

"""
Variables locales y globales
"""

global_var = "automatización"  # Variable global

def hello_python():
    local_var = "Aprendiendo"  # Variable local
    print(f"{local_var} sobre {global_var} con Python.")  # Combina ambas variables

print(global_var)  # Acceso a la variable global
# print(local_var)  # Esto daría un error, ya que no puede acceder a la variable local fuera de la función

hello_python()

"""
Extra
"""

def fizzbuzz(parametro1: str, parametro2: str) -> int:
    """
    Imprime números del 1 al 100, pero sustituye:
    - Múltiplos de 3 por el primer parámetro.
    - Múltiplos de 5 por el segundo parámetro.
    - Múltiplos de 3 y 5 por la concatenación de ambos.
    Retorna la cantidad de veces que se imprimió el número en lugar de los textos.
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
            print(number)  # Imprime el número
            count += 1  # Incrementa el contador

    return count  # Devuelve el total de números impresos

# Ejecución de la función
resultado = fizzbuzz("Fizz", "Buzz")
print(f"\nTotal de números impresos en lugar de textos: {resultado}")
