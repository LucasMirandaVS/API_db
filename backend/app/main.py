from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

app = FastAPI()

# Inicializa o banco de dados
models.Base.metadata.create_all(bind=database.engine)

# Rotas
@app.post("/pokedex/", response_model=schemas.Pokemon)
def add_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(database.get_db)):
    return crud.add_pokemon(db, pokemon)

@app.get("/pokedex/", response_model=list[schemas.Pokemon])
def get_pokedex(db: Session = Depends(database.get_db)):
    return crud.get_pokedex(db)
