from urllib.request import urlopen
import requests

URL_BASE = "https://pokeapi.co/api/v2/"
URL_GENERATION = f"{URL_BASE}/generation/"
URL_POKEMOM = f"{URL_BASE}/pokemon_species/"

def getPokemonId(pokemon):
    url = pokemon['url']
    return int(url[len(URL_POKEMOM)-1:len(url)-1])

def getNationalPokedexByGeneration():

    try:
        pk = int(input("Ingrese el número de generación: "))
    except:
        print("ERROR: Debe ingresar un número!")
    else:
        url = f"{URL_GENERATION}/{pk}/"
        res = requests.get(url)

        if res.status_code != 200:
            print("Generación no encontrada")
        else:
            response = res.json()
            pokemons = response['pokemon_species']
            pokedex = dict()
            for pokemon in pokemons:
                id = getPokemonId(pokemon)
                pokedex[id] = pokemon['name']
            for key in sorted(pokedex.keys()):
                print(f"#{key:03}: {pokedex[key]}")


getNationalPokedexByGeneration()