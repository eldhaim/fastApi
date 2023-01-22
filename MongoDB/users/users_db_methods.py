from MongoDB import variables
from MongoDB.mongoDB import Database
from userApi import users_variables as uvar, serializers_variables as svar
from userApi.models import User, UserDb
from userApi.serializers import user_serializer
from typing import List


class UserDBMethods:
    def __init__(self):
        self.__users_table = Database.collection(uvar.COLL_USERS)
        self.__scopes_table = Database.collection(uvar.COLL_SCOPES)

    def get_scopes_by_id(self, _ids: List[int]) -> List[str]:
        scopes_list: List[str] = []
        for _id in _ids:
            query = {svar.ID: _id}
            try:
                db_scopes = self.__scopes_table.find(query)
                if db_scopes[0] is not None:
                    user_scopes = [i for i in list(db_scopes[0][uvar.SCOPES]) if i not in scopes_list]
                    scopes_list += user_scopes
            except Exception as e:
                print(f"SCOPE CON ID {_id} NO ENCONTRADO (ERROR): {e}")
        return scopes_list

    def get_users(self) -> list:
        users_db = list(self.__users_table.find())
        users = [self.generate_user_from_db(user) for user in users_db]
        return users

    def get_user_by_id(self, _id: str) -> User:
        query = {svar.ID: _id}
        user_db = self.__users_table.find(query)
        user = self.generate_user_from_db(user_db[0])
        return user

    def set_user(self, db_user: UserDb) -> User:
        user = User(
            username=db_user.username,
            name=db_user.name,
            last_name=db_user.last_name,
            email=db_user.email
        )
        self.__users_table.insert_one(user_serializer(db_user))
        return user

    def put_user(
            self,
            username: str,
            name: str = None,
            last_name: str = None,
            email: str = None,
            active: bool = None,
            password: str = None
    ):
        query = {svar.ID: username}
        user_db: UserDb = self.get_user_from_db(username)
        user_db.update_user(
            name=name,
            last_name=last_name,
            email=email,
            active=active,
            password=password
        )
        new_values = {variables.SET: user_serializer(user_db)}
        self.__users_table.update_one(query, new_values)
        return self.generate_user_from_db(user_serializer(user_db))

    def get_user_from_db(self, _id: str) -> UserDb:
        query = {svar.ID: _id}
        db_user = self.__users_table.find(query)[0]
        return UserDb(
            username=db_user[svar.ID],
            name=db_user[svar.NAME],
            last_name=db_user[svar.LAST_NAME],
            email=db_user[svar.EMAIL],
            active=db_user[svar.ACTIVE],
            password=db_user[svar.PASSWORD],
            scopes=db_user[svar.SCOPES],
            permissions=db_user[svar.PERMISSIONS]
        )

    def generate_user_from_db(self, user_db: dict) -> User:
        return User(
            username=user_db[svar.ID],
            name=user_db[svar.NAME],
            last_name=user_db[svar.LAST_NAME],
            email=user_db[svar.EMAIL],
            active=user_db[svar.ACTIVE]
        )

    def validate_user_by_username(self, username: str) -> bool:
        query = {svar.ID: username}
        try:
            if self.__users_table.find(query)[0] is not None:
                return True
        except Exception as e:
            print(f"USUARIO {username} NO ENCONTRADO: {e}")
            return False


if __name__ == '__main__':
    col = UserDBMethods()
    user = col.put_user(username='test', email='unemail@email.com.br')
    print(user.email)
