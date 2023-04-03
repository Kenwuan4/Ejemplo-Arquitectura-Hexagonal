from adapters.Mongo_Adapter import MongoAdapter
import graphene
from graphene import ObjectType, String, Field, Schema

mongo_adapter = MongoAdapter(
    'mongodb://localhost:27017/', 'flaskmongo', 'auth')


class User(ObjectType):
    _id = String()
    email = String()
    password = String()


class CreateUser(graphene.Mutation):
    class Arguments:
        email = String(required=True)
        password = String(required=True)

    user = Field(lambda: User)

    def mutate(self, info, email, password):
        user = mongo_adapter.save(email, password)
        return CreateUser(user=user)


class Query(ObjectType):
    user = Field(User, email=String(required=True),
                 password=String(required=True))

    def resolve_user(self, info, email, password):
        usser_data = mongo_adapter.autenticate_user(email, password)
        if not usser_data:
            return False
        user = User(**usser_data)
        return user


class Mutation(ObjectType):
    create_user = CreateUser.Field()


schema = Schema(query=Query, mutation=Mutation)


def graphQuery(data):
    result = schema.execute(data["query"])
    return result.data
