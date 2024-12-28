"""
Asincronía en Python
"""
"""
La programación asíncrona permite ejecutar funciones de manera concurrente,
lo que optimiza el rendimiento cuando se manejan tareas que implican esperas,
como la realización de operaciones de entrada/salida (I/O).

Módulo `asyncio`:
   - Es una librería de Python para ejecutar código de manera asíncrona.
   - Funciones principales:
       - `async def`: Define una función asíncrona.
       - `await`: Suspende la ejecución de una función asíncrona hasta que se complete.
       - `asyncio.run()`: Ejecuta una función asíncrona desde un programa síncrono.
       - `asyncio.gather()`: Ejecuta múltiples funciones asíncronas en paralelo.
"""

import datetime
import asyncio

async def task(name: str, duration: int):
    start_time = datetime.datetime.now()
    print(
        f"Tarea: {name}. Duración: {duration}s. Inicio: {start_time}")
    await asyncio.sleep(duration)  # Pausa la tarea durante `duration` segundos
    end_time = datetime.datetime.now()
    print(f"Tarea: {name}. Fin: {end_time}")

# Ejecución de una tarea asíncrona de ejemplo
asyncio.run(task("Pantalla de carga", 5))

"""
Extra:
"""
async def tasks():
    print("\n--- Inicio de Ejecución Asíncrona ---\n")
    # Ejecutar tareas C, B y A en paralelo
    await asyncio.gather(
        task("C", 3), 
        task("B", 2), 
        task("A", 1)
    )
    print("\n--- Todas las tareas paralelas han finalizado ---\n")
    # Ejecutar tarea D después de las anteriores
    await task("D", 1)

# Ejecutar todas las tareas orquestadas
asyncio.run(tasks())
