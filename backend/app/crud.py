from sqlalchemy.orm import Session
from . import models, schemas

def add_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    db_pokemon = models.Pokemon(**pokemon.dict())
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

def get_pokedex(db: Session):
    return db.query(models.Pokemon).all()
