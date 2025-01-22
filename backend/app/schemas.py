from pydantic import BaseModel

# Modelo de criação de Pokémon (usuário insere apenas o nome)
class PokemonCreate(BaseModel):
    name: str

# Modelo de Pokémon com id, nome, tipo e descrição
class Pokemon(PokemonCreate):
    id: int
    type: str
    description: str

    class Config:
        orm_mode = True