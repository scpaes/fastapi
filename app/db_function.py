from sqlmodel import Session, select
from .models import Person, engine

def create_person(nome: str, idade:int):
    person = Person(nome=nome, idade=idade)
    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)

    return person


def all_person():
        query = select(Person)
        with Session(engine) as session:
            result = session.execute(query).scalars().all()
        return result