from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    base_experience = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    order = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    sprites = Column(JSON, nullable=False)  # Armazena dados do campo "sprites"
