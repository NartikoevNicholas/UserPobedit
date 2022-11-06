import time

from faker import Faker
from models.database import get_session, create_db
from models.user import User
from models.profession import Profession
import random


def create_profession(session):
    profession = list(map(lambda x: x.name, session.query(Profession).all()))
    list_profession = ['Конструктор', 'Программист', 'Бухгалтер', 'Столяр', 'Плотник', '1С Программист']
    for el in list_profession:
        if profession.__contains__(el) is False:
            session.add(Profession(name=el))
            session.commit()


if __name__ == '__main__':

    create_db()
    session = get_session()
    create_profession(session)
    queryset_profession = session.query(Profession).all()

    faker = Faker('ru_RU')
    while True:
        session.add(User(
            name=faker.first_name(),
            surname=faker.last_name(),
            age=random.randint(22, 70),
            profession=random.choice(queryset_profession).name
        ))
        session.commit()
        print('Create')
        time.sleep(5)
