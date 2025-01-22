import requests

def fetch_pokemon_info(name: str):
    # Define a URL da PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    
    try:
        # Faz a requisição GET para a PokeAPI
        response = requests.get(url)
        # Se o status da resposta for diferente de 200, retorne None
        response.raise_for_status()  # Levanta uma exceção para status code 4xx/5xx
    except requests.exceptions.RequestException as e:
        # Caso haja algum erro, como problemas de conexão ou erro no status code
        print(f"Erro ao consultar Pokémon '{name}': {e}")
        return None
    
    # Se a resposta for bem-sucedida, processa os dados
    data = response.json()
    
    # Extrai os tipos do Pokémon
    types = [t["type"]["name"] for t in data["types"]]
    
    # Retorna um dicionário com o nome e os tipos (até 2 tipos)
    return {
        "name": name,
        "type_1": types[0],
        "type_2": types[1] if len(types) > 1 else None
    }
