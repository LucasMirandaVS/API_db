import requests
from sqlalchemy.orm import Session
from . import models, schemas

# Função para buscar informações do Pokémon na API
def fetch_pokemon_data(name: str):
    # URL da API para obter dados do Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    
    # Realiza a requisição para a API
    response = requests.get(url)
    
    if response.status_code != 200:
        raise ValueError(f"Não foi possível encontrar o Pokémon {name}")
    
    data = response.json()
    
    # Obtém o tipo do Pokémon
    types = [t['type']['name'] for t in data['types']]
    
    # Obtém a descrição do Pokémon (de uma segunda requisição na API)
    species_url = data['species']['url']
    species_response = requests.get(species_url)
    
    if species_response.status_code != 200:
        raise ValueError("Não foi possível obter a descrição do Pokémon")
    
    species_data = species_response.json()
    description = ""
    
    for flavor_text in species_data['flavor_text_entries']:
        if flavor_text['language']['name'] == 'en':  # Garantindo que a descrição seja em inglês
            description = flavor_text['flavor_text']
            break
    
    # Retorna todas as informações necessárias
    return {
        "type": types[0],  # Primeiro tipo
        "description": description,
        "number": data["id"],
        "base_experience": data["base_experience"],
        "height": data["height"],
        "order": data["order"],
        "weight": data["weight"],
        "sprites": {
            "front_default": data["sprites"]["front_default"],
            "back_default": data["sprites"]["back_default"]
        }
    }

# Função para criar um novo Pokémon no banco de dados
def create_pokemon(db: Session, name: str):
    # Obtém dados do Pokémon da API
    pokemon_data = fetch_pokemon_data(name)
    
    # Cria um novo registro de Pokémon no banco de dados
    db_pokemon = models.Pokemon(
        name=name,
        type=pokemon_data["type"],
        description=pokemon_data["description"],
        number=pokemon_data["number"],
        base_experience=pokemon_data["base_experience"],
        height=pokemon_data["height"],
        order=pokemon_data["order"],
        weight=pokemon_data["weight"],
        sprites=pokemon_data["sprites"]
    )
    
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

# Função para obter todos os Pokémons
def get_pokemons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()

# Função para obter um Pokémon pelo ID
def get_pokemon_by_id(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()

# Função para excluir um Pokémon pelo nome
def delete_pokemon_by_name(db: Session, pokemon_name: str):
    # Encontrando o Pokémon pelo nome
    db_pokemon = db.query(models.Pokemon).filter(models.Pokemon.name == pokemon_name).first()
    if db_pokemon is None:
        raise ValueError(f"Pokemon with name '{pokemon_name}' not found")
    
    # Excluindo o Pokémon
    db.delete(db_pokemon)
    db.commit()
    return db_pokemon
