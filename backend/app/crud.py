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
    
    return types[0], description  # Retorna o primeiro tipo e a descrição

# Função para criar um novo Pokémon no banco de dados
def create_pokemon(db: Session, name: str):
    # Obtém dados do Pokémon da API
    pokemon_type, description = fetch_pokemon_data(name)
    
    # Cria um novo registro de Pokémon no banco de dados
    db_pokemon = models.Pokemon(
        name=name,
        type=pokemon_type,
        description=description
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