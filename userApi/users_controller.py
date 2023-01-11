from fastapi import HTTPException, status

import commons
from userApi import user_commons, messages
from userApi.models import User


class UsersController:
    """Objeto encargado de tratar las validaciones
    y comunicar los modelos con el objeto 'router'"""

    def __init__(self):
        self.__comunes = user_commons.Commons()

    def get_users(self):
        if len(self.__comunes.users) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=messages.GET_USERS_HTTP_BAD_REQUEST
            )
        return self.__comunes.users

    def get_user_by_id(
            self,
            username: str
    ):
        if not self.__comunes.validate_user_by_username(username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=commons.mensaje_con_parametros(
                    mensaje=messages.GET_USER_BY_USERNAME_HTTP_BAD_REQUEST,
                    parametros=[username]
                )
            )
        return self.__comunes.user

    def set_user(
            self,
            user: User
    ):
        if self.__comunes.validate_user_by_username(user.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=commons.mensaje_con_parametros(
                    mensaje=messages.SET_USER_HTTP_BAD_REQUEST,
                    parametros=[user.username]
                )
            )
        self.__comunes.add_user(user)
        return user

    def put_user(
            self,
            username: str,
            name: str = None,
            last_name: str = None,
            email: str = None
    ):
        if name is None and last_name is None and email is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=messages.PUT_USER_HTTP_BAD_REQUEST_PARAMS
            )
        if not self.__comunes.validate_user_by_username(username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=commons.mensaje_con_parametros(
                    mensaje=messages.PUT_USER_HTTP_BAD_REQUEST,
                    parametros=[username]
                )
            )
        user: User = self.__comunes.user
        user.update_user(
            name=name,
            last_name=last_name,
            email=email
        )
        return user
