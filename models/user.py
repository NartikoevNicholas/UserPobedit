from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base


class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    profession = Column(String, ForeignKey('profession.name'))
