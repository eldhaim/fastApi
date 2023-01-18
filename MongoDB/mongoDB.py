from pymongo import MongoClient
import os

# from userApi.models import UserDb
# from userApi.serializers import user_serializer
from MongoDB import variables

if variables.DEBUG:
    from MongoDB import local_env as local


class Database:
    __usr = local.DB_USER if variables.DEBUG else os.environ.get(variables.USER)
    __password = local.DB_PASSWORD if variables.DEBUG else os.environ.get(variables.PASSWORD)
    __db_name = local.DB_NAME if variables.DEBUG else os.environ.get(variables.DB_NAME)
    __client = MongoClient(
        f"{variables.MONGO_CLIENT_1}{__usr}{variables.MONGO_CLIENT_T}{__password}{variables.MONGO_CLIENT_A}{__db_name}{variables.MONGO_CLIENT_2}")
    __db = __client.FastApiDB

    @classmethod
    def collection(cls, collection_name: str):
        return cls.__db[collection_name]


# if __name__ == '__main__':
#     col = Database.collection('Users')
#     user = UserDb(username='test', name='test_name', password='test', email='test@test.com', last_name='test_last')
#     insert_user = col.find()
#     print(list(insert_user)[0])
