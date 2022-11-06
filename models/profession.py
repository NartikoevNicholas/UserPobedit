from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.database import Base


class Profession(Base):
    __tablename__ = 'profession'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    user = relationship('User')
