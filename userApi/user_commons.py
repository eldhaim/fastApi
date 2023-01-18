# PRUEBAS SIN DB
from userApi import serializers_variables as svar
from userApi.models import User


class Commons:
    def __init__(self):
        self.__user = None
        self.__users = [User(username="FLuis", name="Pedro1", last_name='Puentes', email='pedro@gmail.com'),
                        User(username="EdEddEddy", name="Pedro2", last_name='Puentes', email='pedro@gmail.com'),
                        User(username="tres", name="Pedro3", last_name='Puentes', email='pedro@gmail.com'),
                        User(username="cuatro", name="Pedro4", last_name='Puentes', email='pedro@gmail.com')]

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, usuario):
        self.__user = usuario

    @property
    def users(self):
        return self.__users

    def add_user(self, user):
        self.__users.append(user)

    def validate_user_by_username(self, username: str):
        user = list(filter(lambda user: user.username == username, self.__users))
        if len(user) == 0:
            return False
        self.user = user[0]
        return True

    def generate_user_from_db(self, user_db: dict) -> User:
        user = User(
            username=user_db[svar.ID],
            name=user_db[svar.NAME],
            last_name=user_db[svar.LAST_NAME],
            email=user_db[svar.EMAIL]
        )
        return user
