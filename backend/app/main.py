import sys
import os

# Adicionando o diretório `backend` ao caminho de busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas  # Corrigido para importar corretamente de 'app'
from .database import SessionLocal, engine
from . import models

# O resto do seu código permanece igual

# Criação das tabelas no banco de dados (caso ainda não existam)
models.Base.metadata.create_all(bind=engine)

application = FastAPI()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um novo Pokémon
@application.post("/pokemons/", response_model=schemas.Pokemon)
def create_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_pokemon(db=db, name=pokemon.name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Rota para obter todos os Pokémons
@application.get("/pokemons/", response_model=list[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_pokemons(db=db, skip=skip, limit=limit)

# Rota para obter um Pokémon específico pelo ID
@application.get("/pokemons/{pokemon_id}", response_model=schemas.Pokemon)
def get_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    db_pokemon = crud.get_pokemon_by_id(db=db, pokemon_id=pokemon_id)
    if db_pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return db_pokemon

# Rota para excluir um Pokémon específico pelo nome
@application.delete("/pokemons/{pokemon_name}", response_model=schemas.Pokemon)
def delete_pokemon(pokemon_name: str, db: Session = Depends(get_db)):
    try:
        return crud.delete_pokemon_by_name(db=db, pokemon_name=pokemon_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

