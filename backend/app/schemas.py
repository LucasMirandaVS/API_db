from pydantic import BaseModel
from typing import Optional, Dict


# Modelo para criação de Pokémon
class PokemonCreate(BaseModel):
    name: str


# Modelo para atualização parcial de Pokémon
class PokemonUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    number: Optional[int] = None
    base_experience: Optional[int] = None
    height: Optional[int] = None
    order: Optional[int] = None
    weight: Optional[int] = None
    sprites: Optional[Dict] = None


# Modelo para resposta de Pokémon
class PokemonResponse(BaseModel):
    id: int
    name: str
    type: str
    description: str
    number: int
    base_experience: int
    height: int
    order: int
    weight: int
    sprites: Dict

    class Config:
        orm_mode = True
