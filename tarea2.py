import requests

class Game:

    def __init__(self):
        pass

    def run(self):
        self._showOptions()
        self._executeOption()

    def _showOptions(self):
        print("Bienvenido a la PokeApi!")
        print("\nLas opciones a elegir son: \n")
        print(f"\t1) Listar Pokemon por generación.")
        print(f"\t2) Listar Pokemon por forma.")
        print(f"\t3) Listar Pokemon por habilidad.")
        print(f"\t4) Listar Pokemon por habitat.")
        print(f"\t5) Listar Pokemon por tipo.")

    def _executeOption(self):
        try:
            n = int(input("\nIngrese una de las opciones [id]: "))
        except:
            print("ERROR: Debe ingresar un número")
        else:
            if n == 1:
                self._getNationalPokedexByGeneration()
            elif n==2:
                self._getByShape()
            elif n==3:
                self._getPokemonByAbility()
            elif n==4:
                self._getPokemonByHabitat()
            elif n==5:
                self._getPokemonByType()
            else:
                print("Debe ingresar una opción válida")

    def _getNationalPokedexByGeneration(self):

        try:
            pk = int(input("\nIngrese el número de generación: "))
        except:
            print("ERROR: Debe ingresar un número!")
        else:
            url = f"https://pokeapi.co/api/v2/generation/{pk}/"
            res = requests.get(url)

            if res.status_code != 200:
                print("Generación no encontrada")
            else:
                response = res.json()
                pokemons = response['pokemon_species']
                pokedex = dict()
                for pokemon in pokemons:
                    id = self._extractId("https://pokeapi.co/api/v2/pokemon-species/", pokemon['url'])
                    if id < 1200:
                        pokedex[id] = pokemon['name']
                print("\nPokemons:\n")
                for key in sorted(pokedex.keys()):
                    pokemon = Pokemon(key,pokedex[key])
                    pokemon.print()
                    print("-----------------------------------------------------------")

    def _getByShape(self):

        url = "https://pokeapi.co/api/v2/pokemon-shape/"
        res = requests.get(url)
        if res.status_code != 200:
            print("ERROR")
        else:
            response = res.json()
            results = response["results"]
            shape = dict()
            for result in results:
                id = self._extractId(url, result['url'])
                name = result["name"].capitalize()
                shape[id] = name
            print("\nLas Habilidades Pokemon son las siguientes:\n")
            for key in sorted(shape.keys()):
                    print(f"{key:<2}: {shape[key]}")
            try:
                pk = int(input("\nIngrese una habilidad [id]: "))
            except:
                print("ERROR: Debe ingresar un número!")
            else:
                url = f"https://pokeapi.co/api/v2/pokemon-shape/{pk}/"
                res = requests.get(url)
                if res.status_code != 200:
                    print("ERROR: Tipo no encontrado")
                else:
                    response = res.json()
                    pokemons = response["pokemon_species"]
                    print("\nPokemons:\n")
                    for pokemon in pokemons:
                        id = self._extractId("https://pokeapi.co/api/v2/pokemon-species/", pokemon['url'])
                        name = pokemon['name']
                        if id < 1200:
                            pokemon = Pokemon(id, name)
                            pokemon.print()
                            print("-----------------------------------------------------------")
    def _getPokemonByType(self):

        url = "https://pokeapi.co/api/v2/type/"
        res = requests.get(url)
        if res.status_code != 200:
            print("ERROR")
        else:
            response = res.json()
            results = response["results"]
            types = dict()
            for result in results:
                id = self._extractId(url, result['url'])
                name = result["name"].capitalize()
                if id <= 18:
                    types[id] = name
            print("\nLos tipos de Pokemon son los siguientes:\n")
            for key in sorted(types.keys()):
                print(f"{key:<2}: {types[key]}")
            try:
                pk = int(input("\nIngrese un tipo de Pokemon [id]: "))
            except:
                print("ERROR: Debe ingresar un número!")
            else:
                url = f"https://pokeapi.co/api/v2/type/{pk}/"
                res = requests.get(url)
                if res.status_code != 200:
                    print("ERROR: Tipo no encontrado")
                else:
                    response = res.json()
                    pokemons = response["pokemon"]
                    print("\nPokemons:\n")
                    for pokemon in pokemons:
                        pokemon = pokemon['pokemon']
                        id = self._extractId("https://pokeapi.co/api/v2/pokemon/", pokemon['url'])
                        name = pokemon['name']
                        if id < 1200:
                            pokemon = Pokemon(id, name)
                            pokemon.print()
                            print("-----------------------------------------------------------")
    
    #option3
    def _getPokemonByAbility(self):
        url = "https://pokeapi.co/api/v2/ability/"
        res = requests.get(url+"?limit=327&offset=0")
        if res.status_code != 200:
            print("ERROR")
        else:
            response = res.json()
            results = response["results"]
            ability = dict()
            for result in results:
                id = self._extractId(url, result['url'])
                name = result["name"].capitalize()
                ability[id] = name
            print("\nLas Habilidades Pokemon son las siguientes:\n")
            for key in sorted(ability.keys()):
                    print(f"{key:<3}: {ability[key]}")
            try:
                pk = int(input("\nIngrese una habilidad [id]: "))
            except:
                print("ERROR: Debe ingresar un número!")
            else:
                url = f"https://pokeapi.co/api/v2/ability/{pk}/"
                res = requests.get(url)
                if res.status_code != 200:
                    print("ERROR: Tipo no encontrado")
                else:
                    response = res.json()
                    pokemons = response["pokemon"]
                    print("\nPokemons:\n")
                    for pokemon in pokemons:
                        pokemon = pokemon['pokemon']
                        id = self._extractId("https://pokeapi.co/api/v2/pokemon/", pokemon['url'])
                        name = pokemon['name']
                        if id < 1200:
                            pokemon = Pokemon(id, name)
                            pokemon.print()
                            print("-----------------------------------------------------------")


    def _getPokemonByHabitat(self):

        url = "https://pokeapi.co/api/v2/pokemon-habitat/"
        res = requests.get(url)
        if res.status_code != 200:
            print("ERROR")
        else:
            response = res.json()
            results = response["results"]
            habitat = dict()
            for result in results:
                id = self._extractId(url, result['url'])
                name = result["name"].capitalize()
                if id <= 18:
                    habitat[id] = name
            print("\nLos Habitat de los Pokemones son los siguientes:\n")
            for key in sorted(habitat.keys()):
                print(f"{key:<2}: {habitat[key]}")
            try:
                pk = int(input("\nIngrese un tipo de Habitat [id]: "))
            except:
                print("ERROR: Debe ingresar un número!")
            else:
                url = f"https://pokeapi.co/api/v2/type/{pk}/"
                res = requests.get(url)
                if res.status_code != 200:
                    print("ERROR: Tipo no encontrado")
                else:
                    response = res.json()
                    pokemons = response["pokemon"]
                    print("\nPokemons:\n")
                    for pokemon in pokemons:
                        pokemon = pokemon['pokemon']
                        id = self._extractId("https://pokeapi.co/api/v2/pokemon/", pokemon['url'])
                        name = pokemon['name']
                        if id < 1200:
                            pokemon = Pokemon(id, name)
                            pokemon.print()
                            print("-----------------------------------------------------------")

    def _extractId(self,baseURL, url):
        a = len(baseURL)
        b = len(url)-1
        return int(url[a:b])

class Pokemon:

    def __init__(self,id,name):
        self._id = id
        self._name = name.capitalize()
        self._getInformation()

    def _getInformation(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self._id}"
        res = requests.get(url)
        response = res.json()
        results = response['abilities']
        abilities = []
        for result in results:
            abilities.append(result['ability']['name'])
        self._abilities = abilities
        self._image = response['sprites']['front_default']

    def print(self):
        print(f"N.° {self._id:03}")
        print(f"Name: {self._name}")
        print(f"Abilities:")
        for abilitie in self._abilities:
            print(f"\t{abilitie}")
        print(f"ImageURL: {self._image}")

game = Game()
game.run()