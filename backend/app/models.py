from sqlalchemy import Column, Integer, String
from .database import Base

class Pokemon(Base):
    __tablename__ = "pokedex"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type_1 = Column(String)
    type_2 = Column(String, nullable=True)
