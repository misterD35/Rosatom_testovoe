import typing
import strawberry
import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Top_manager:
    name: str
    age: int


@strawberry.type
class Rockets:
    name: str
    link: str


@strawberry.type
class Query:
    users: typing.List[Top_manager]

    @strawberry.field
    def users(self) -> typing.List[Top_manager]:
        return [
            Top_manager(name="Elon Mask", age=51),
            Top_manager(name="Gwynne Shotwel", age=59)
        ]

    @strawberry.field
    def rockets(self) -> typing.List[Rockets]:
        return [
            Rockets(
                name="Falcon 9",
                link="https://en.wikipedia.org/wiki/Falcon_9",
            ),
            Rockets(
                name="Falcon Heavy",
                link="https://en.wikipedia.org/wiki/Falcon_Heavy",
            ),
        ]


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
