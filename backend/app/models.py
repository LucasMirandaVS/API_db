from sqlalchemy import Column, Integer, String
from .database import Base

class Pokemon(Base):
    __tablename__ = 'pokemons'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(String)
    description = Column(String)