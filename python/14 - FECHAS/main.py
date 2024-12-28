"""
Manejo de Fechas en Python
"""
"""
   - `datetime`:
     - Es un módulo en Python que proporciona clases para trabajar con fechas y horas.
   - Objetos `datetime`:
     - Permiten representar y manipular fechas y horas con precisión.
   - Métodos Comunes:
     - `now()`: Obtiene la fecha y hora actual.
     - `strftime()`: Formatea fechas en cadenas según un formato especificado.
     - `timedelta`: Representa la diferencia entre dos objetos `datetime`.
"""

from datetime import datetime

# Fecha y hora actuales
now = datetime.now()

# Fecha y hora de nacimiento (puedes modificar la hora según prefieras)
birth_date = datetime(2005, 1, 22, 9, 0, 0)

# Impresión de ambas fechas
print(f"Fecha actual: {now}")
print(f"Fecha de nacimiento: {birth_date}\n")

# Calcula la diferencia entre las fechas
difference = now - birth_date

# Obtén los años transcurridos
years = difference.days // 365
print(f"Hasta la fecha actual, han transcurrido {years} años desde mi nacimiento.\n")

"""
Extra:
"""
# 1. Día, mes y año (varias variantes)
print("1. Formato día/mes/año corto:", birth_date.strftime("%d/%m/%y"))
print("2. Formato día-mes-año largo:", birth_date.strftime("%d-%m-%Y"))

# 2. Hora, minuto y segundo
print("3. Hora:minuto:segundo:", birth_date.strftime("%H:%M:%S"))

# 3. Día del año (ordinal)
print("4. Día del año:", birth_date.strftime("%j"))

# 4. Día de la semana
print("5. Día de la semana:", birth_date.strftime("%A"))

# 5. Nombre del mes
print("6. Nombre del mes corto:", birth_date.strftime("%b"))
print("7. Nombre del mes completo:", birth_date.strftime("%B"))

# 6. Representación según el sistema local
print("8. Representación por defecto (locale):", birth_date.strftime("%c"))
print("9. Fecha formateada según locale:", birth_date.strftime("%x"))
print("10. Hora formateada según locale:", birth_date.strftime("%X"))

# 7. Representación AM/PM
print("11. Representación AM/PM:", birth_date.strftime("%p"))
