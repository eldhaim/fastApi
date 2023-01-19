from typing import List
from fastapi import APIRouter, status, Depends
from userApi import users_variables as uvar

from auth import Auth
from userApi import paths, messages, user_commons
from userApi.models import User, UserDb
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
async def get_users(current_user: UserDb = Depends(Auth.get_current_user)):
    """Consulta de todos los usuarios"""
    await Auth.validate_permissions(
        scope=uvar.SCOPE,
        permission=uvar.READ,
        user_db=current_user
    )
    return controller.get_users()


@router.get(
    path=paths.GET_USER_BY_ID,
    status_code=status.HTTP_200_OK,
    response_description=messages.GET_USER_BY_USERNAME_HTTP_OK,
    summary=messages.GET_USER_BY_USERNAME_SUMMARY,
    response_model=User,
    responses=messages.BASIC_RESPONSES
)
async def get_user_by_id(username: str, current_user: UserDb = Depends(Auth.get_current_user)):
    """
    Consulta de un usuario por username:

    - **id**: Identificador del usuario (obligatiorio)
    \f
    :param username: FakeUser.username input.
    :return user: FakeUser output.
    """
    await Auth.validate_permissions(
        scope=uvar.SCOPE,
        permission=uvar.READ,
        user_db=current_user
    )
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
async def set_user(db_user: UserDb, current_user: UserDb = Depends(Auth.get_current_user)):
    """
    Creacion de un usuario con toda la informacion:

    - **id**: Identificador del usuario (obligatiorio)
    - **name**: Nombre del usuario (obligatior)
    - **last_name**: Apellido del usuario (obligatior)
    - **email**: Correco electronico del usuario (Opcional)
    - **active**: Indica si el usuario esta activo (Opcional)
    - **password**: Contraseña del usuario (obligatiorio)
    \f
    :param db_user: User with password input.
    :return user: User without password output.
    """
    await Auth.validate_permissions(
        scope=uvar.SCOPE,
        permission=uvar.WRITE,
        user_db=current_user
    )
    return controller.set_user(db_user=db_user)


@router.put(
    path=paths.PUT_USER,
    status_code=status.HTTP_200_OK,
    response_description=messages.PUT_USER_HTTP_OK,
    summary=messages.PUT_USER_SUMMARY,
    response_model=User,
    responses=messages.BASIC_RESPONSES
)
async def put_user(
        username: str,
        name: str = None,
        last_name: str = None,
        email: str = None,
        active: bool = None,
        password: str = None,
        current_user: UserDb = Depends(Auth.get_current_user)
):
    """
    Actualizacion de uno o mas campos de un usuario existente:

    **NOTA**: Los parametros se pasan por query (Por lo menos uno)

    - **username**: Identificador del usuario (obligatiorio)
    - **name**: Nombre del usuario (Opcional)
    - **last_name**: Apellido del usuario (Opcional)
    - **email**: Correco electronico del usuario (Opcional)
    - **active**: Indica si el usuario esta activo (Opcional)
    - **password**: Contraseña del usuario (obligatiorio)
    \f
    :param email: db_user.email input.
    :param username: db_user.username input.
    :param name: db_user.name input.
    :param last_name: db_user.last_name input.
    :param active: User activity indicator input.
    :param password: new password of the user input.
    :return user: User without password output.
    """
    await Auth.validate_permissions(
        scope=uvar.SCOPE,
        permission=uvar.UPDATE,
        user_db=current_user
    )
    return controller.put_user(
        username=username,
        name=name,
        last_name=last_name,
        email=email,
        active=active,
        password=password
    )
