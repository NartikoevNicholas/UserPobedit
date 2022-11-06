from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_user = 'dima'
db_password = 'pobedit_123'
db_name = 'pobedit'

Base = declarative_base()
engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@localhost/{db_name}")


def create_db():
    Base.metadata.create_all(engine)


def get_session():
    session = sessionmaker(bind=engine)
    return session()
