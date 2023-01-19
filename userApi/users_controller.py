import commons
from fastapi import HTTPException, status
from typing import List
from MongoDB.users_db_methods import UserDBMethods
from userApi import messages
from userApi.models import User, UserDb


class UsersController:
    """Objeto encargado de comunicar los metodos de base de datos con el 'router'"""

    def __init__(self):
        self.__users_db_methods = UserDBMethods()

    def get_users(self) -> List[User]:
        users = self.__users_db_methods.get_users()
        if len(users) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=messages.GET_USERS_HTTP_BAD_REQUEST
            )
        return users

    def get_user_by_id(
            self,
            username: str
    ):
        if not self.__users_db_methods.validate_user_by_username(username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=commons.mensaje_con_parametros(
                    mensaje=messages.GET_USER_BY_USERNAME_HTTP_BAD_REQUEST,
                    parametros=[username]
                )
            )
        return self.__users_db_methods.get_user_by_id(username)

    def set_user(
            self,
            db_user: UserDb
    ):
        if self.__users_db_methods.validate_user_by_username(db_user.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=commons.mensaje_con_parametros(
                    mensaje=messages.SET_USER_HTTP_BAD_REQUEST,
                    parametros=[db_user.username]
                )
            )
        return self.__users_db_methods.set_user(db_user)

    def put_user(
            self,
            username: str,
            name: str = None,
            last_name: str = None,
            email: str = None,
            active: bool = None,
            password: str = None
    ):
        if name is None and last_name is None and email is None and active is None and password is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=messages.PUT_USER_HTTP_BAD_REQUEST_PARAMS
            )
        if not self.__users_db_methods.validate_user_by_username(username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=commons.mensaje_con_parametros(
                    mensaje=messages.PUT_USER_HTTP_BAD_REQUEST,
                    parametros=[username]
                )
            )
        return self.__users_db_methods.put_user(
            username=username,
            name=name,
            last_name=last_name,
            email=email,
            active=active,
            password=password
        )
