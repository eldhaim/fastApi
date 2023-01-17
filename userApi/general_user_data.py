from typing import List
from fastapi import APIRouter, status
from userApi import paths, messages, user_commons
from userApi.models import User
from userApi.users_controller import UsersController

router = APIRouter(
    prefix=paths.USERS_PREFIX,
    tags=[messages.TAG_DATA]
)
"""Router encargado del manejo de usuarios"""
comunes = user_commons.Commons()
controller = UsersController()


@router.get(
    path=paths.GET_USERS,
    status_code=status.HTTP_200_OK,
    response_description=messages.GET_USERS_HTTP_OK,
    summary=messages.GET_USERS_SUMMARY,
    response_model=List[User],
    responses=messages.BASIC_RESPONSES
)
async def get_users():
    """Consulta de todos los usuarios"""
    return controller.get_users()


@router.get(
    path=paths.GET_USER_BY_ID,
    status_code=status.HTTP_200_OK,
    response_description=messages.GET_USER_BY_USERNAME_HTTP_OK,
    summary=messages.GET_USER_BY_USERNAME_SUMMARY,
    response_model=User,
    responses=messages.BASIC_RESPONSES
)
async def get_user_by_id(username: str):
    """
    Consulta de un usuario por username:

    - **id**: Identificador del usuario (obligatiorio)
    \f
    :param username: FakeUser.username input.
    :return user: FakeUser output.
    """
    return controller.get_user_by_id(username=username)


# buscar como documentar una HTTPException
@router.post(
    path=paths.SET_USER,
    status_code=status.HTTP_200_OK,
    response_description=messages.SET_USER_HTTP_OK,
    summary=messages.SET_USER_SUMMARY,
    response_model=User,
    responses=messages.BASIC_RESPONSES
)
async def set_user(user: User):
    """
    Creacion de un usuario con toda la informacion:

    - **id**: Identificador del usuario (obligatiorio)
    - **name**: Nombre del usuario (obligatior)
    - **last_name**: Apellido del usuario (obligatior)
    - **email**: Correco electronico del usuario (Opcional)
    \f
    :param user: FakeUser input.
    :return user: FakeUser output.
    """
    return controller.set_user(user=user)


@router.put(
    path=paths.PUT_USER,
    status_code=status.HTTP_200_OK,
    response_description=messages.PUT_USER_HTTP_OK,
    summary=messages.PUT_USER_SUMMARY,
    response_model=User,
    responses=messages.BASIC_RESPONSES
)
async def put_user(username: str, name: str = None, last_name: str = None, email: str = None):
    """
    Actualizacion de uno o mas campos de un usuario existente:

    **NOTA**: Los parametros se pasan por query (Por lo menos uno)

    - **username**: Identificador del usuario (obligatiorio)
    - **name**: Nombre del usuario (Opcional)
    - **last_name**: Apellido del usuario (Opcional)
    - **email**: Correco electronico del usuario (Opcional)
    \f
    :param username: FakeUser.username input.
    :param name: FakeUser.name input.
    :param last_name: FakeUser.last_name input.
    :param email: FakeUser.email input.
    :return user: FakeUser output.
    """
    return controller.put_user(
        username=username,
        name=name,
        last_name=last_name,
        email=email
    )
