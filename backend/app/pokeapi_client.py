import requests

def fetch_pokemon_info(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    types = [t["type"]["name"] for t in data["types"]]
    return {"name": name, "type_1": types[0], "type_2": types[1] if len(types) > 1 else None}
