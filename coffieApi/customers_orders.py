from typing import List
from fastapi import APIRouter, status, Depends
from coffieApi import variables as var
from auth import Auth
from coffieApi import paths, messages
from coffieApi.models import Order, CustomerOrders
from coffieApi.controller import CustomerOrdersController
from userApi.models import UserDb

router = APIRouter(
    prefix=paths.CUSTOMERS_ORDERS_PREFIX,
    tags=[messages.TAG_DATA]
)
"""Router encargado del manejo de usuarios"""
controller = CustomerOrdersController()


# buscar como documentar una HTTPException
@router.post(
    path=paths.SET_ORDER,
    status_code=status.HTTP_200_OK,
    response_description=messages.SET_ORDER_HTTP_OK,
    summary=messages.SET_ORDER_SUMMARY,
    response_model=CustomerOrders,
    responses=messages.BASIC_RESPONSES
)
async def set_order(customer_orders: CustomerOrders, current_user: UserDb = Depends(Auth.get_current_user)):
    """
    Creacion de un usuario con toda la informacion:

    - **id**: Identificador del usuario (obligatiorio)
    - **name**: Nombre del usuario (obligatior)
    - **last_name**: Apellido del usuario (obligatior)
    - **email**: Correco electronico del usuario (Opcional)
    - **active**: Indica si el usuario esta activo (Opcional)
    - **password**: Contraseña del usuario (obligatiorio)
    \f
    :param customer_orders: User with password input.
    :return user: User without password output.
    """
    await Auth.validate_permissions(
        scope=var.SCOPE,
        permission=var.WRITE,
        user_db=current_user
    )
    return 'OK'