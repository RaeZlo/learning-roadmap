"""
Peticiones HTTP en Python
"""
"""
Las peticiones HTTP son una herramienta poderosa para interactuar con APIs.
Este ejercicio demostró cómo realizar solicitudes GET y procesar respuestas en formato JSON.
Además, se incluyeron controles de errores para mejorar la robustez del programa.
"""

import requests

# Realizar una petición HTTP a una página web
response = requests.get("https://google.com")
if response.status_code == 200:
    print("Contenido de la página solicitada:\n")
    print(response.text[:500])  # Muestra los primeros 500 caracteres del contenido
else:
    print(f"Error al realizar la petición. Código de estado: {response.status_code}")
    
"""
Extra
"""
# Solicitar información sobre un Pokémon concreto
pokemon = input("Introduce un nombre o número de Pokédex del Pokémon a buscar: ").lower()

# Realizar la petición a la PokéAPI
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    # Procesar la respuesta JSON
    data = response.json()
    print("\nInformación básica del Pokémon:")
    print(f"Nombre: {data['name']}")
    print(f"ID: {data['id']}")
    print(f"Peso: {data['weight']}")
    print(f"Altura: {data['height']}")
    print("Tipo(s):")
    for tipo in data["types"]:
        print(f"  - {tipo['type']['name']}")

    print("\nJuegos en los que aparece:")
    for game in data["game_indices"]:
        print(f"  - {game['version']['name']}")

    # Solicitar la cadena de evolución
    response_species = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response_species.status_code == 200:
        species_data = response_species.json()
        evolution_url = species_data["evolution_chain"]["url"]

        # Petición para obtener la cadena de evolución
        response_evolution = requests.get(evolution_url)
        if response_evolution.status_code == 200:
            evolution_data = response_evolution.json()
            print("\nCadena de evolución:")

            # Función recursiva para recorrer la cadena de evolución
            def obtener_evoluciones(data):
                print(f"  - {data['species']['name']}")
                if "evolves_to" in data and data["evolves_to"]:
                    for evo in data["evolves_to"]:
                        obtener_evoluciones(evo)

            obtener_evoluciones(evolution_data["chain"])
        else:
            print(f"Error {response_evolution.status_code} obteniendo las evoluciones.")
    else:
        print(f"Error {response_species.status_code} obteniendo información de la especie.")
else:
    print(f"Error {response.status_code}: Pokémon no encontrado.")
