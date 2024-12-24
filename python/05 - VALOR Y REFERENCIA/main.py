"""
Asignación por Valor
"""
# Tipos de datos por valor
int_a = 10
int_b = int_a
int_b = 19
print(int_a)
print(int_b)

"""
Asignación por Referencia
"""
# Tipos de datos por referencia
list_a = [10, 19]
list_b = list_a
list_b.append(27)
print(list_a)
print(list_b)

"""
Funciones con Valor por Valor
"""
# Funciones con datos por valor
def my_int_func(my_int: int):
    my_int = 20
    print(my_int)


my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)

"""
Funciones con Valor por Referencia
"""
# Funciones con datos por referencia
def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)


my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

"""
Extra
"""

# Por valor
def intercambio_valor(valor1:int, valor2:int) -> int:
    valor3 = valor1
    valor1 = valor2
    valor2 = valor3

    return valor1, valor2

print(intercambio_valor(10, 69))

# Por referencia
def intercambio_referencia(valor1:list, valor2:list) -> list:
    valor3 = valor1
    valor1 = valor2
    valor2 = valor3

    return valor1, valor2

list_a = [10, 65]
list_b = [32, 78]
print(intercambio_valor(list_a, list_b))
