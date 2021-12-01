from fastapi import FastAPI
from typing import Optional
from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    select,
    Session
)


engine = create_engine('sqlite:///database.db')


class Pessoa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    idade: int


SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
def home():
    return {
        'message': 'Deu bom.'
    }


@app.get('/pessoa/')
def get_pessoa():
    query = select(Pessoa.nome)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()
    return result