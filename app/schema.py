from typing import Optional
import strawberry
from strawberry.fastapi import GraphQLRouter
from .db_function import all_person, create_person


@strawberry.type
class Pessoa:
    id: Optional[int]
    nome: str
    idade: int


@strawberry.type
class Query:
    all_pessoa: list[Pessoa] = strawberry.field(resolver=all_person)


@strawberry.type
class Mutation:
    create_pessoa: Pessoa = strawberry.field(resolver=create_person)

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)