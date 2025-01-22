from pydantic import BaseModel

class PokemonBase(BaseModel):
    name: str

class PokemonCreate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int
    type: str
    description: str
    number: int
    base_experience: int
    height: int
    order: int
    weight: int
    sprites: dict

    class Config:
        orm_mode = True
