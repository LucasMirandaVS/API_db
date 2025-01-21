from pydantic import BaseModel

class PokemonBase(BaseModel):
    name: str
    type_1: str
    type_2: str | None = None

class PokemonCreate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int

    class Config:
        orm_mode = True
