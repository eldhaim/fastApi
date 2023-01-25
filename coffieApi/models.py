from typing import Union, List
from datetime import datetime
from pydantic import BaseModel


class Product(BaseModel):
    """Modelo de producto:

    - **id**: Identificador del producto(Obligatorio)
    - **name**: Nombre del producto (Obligatorio)
    - **description**: Descripción del producto (Obligatorio)
    - **is_drink**: Indica si es bebida (Opcional = True)
    - **registration_date**: Fecha de ingreso del registro (Auto)
    - **updated**: Fecha de actualizacion (Cada vez que se haga algun cambio sobre el ID)
    - **types**: Lista que contiene los tipos de producto (Opcional)
    - **active**: Indica si el usuario esta activo (Opcional = True)

    """

    class TypesOfProduct(BaseModel):
        id: int
        name: str

    class PriceBySize(BaseModel):
        size: str
        price: float

    id: int
    name: str
    description: str
    is_drink: bool = True
    registration_date: datetime = datetime.utcnow()
    updated: Union[datetime, None] = None
    types: List[TypesOfProduct] = None
    prices_by_sizes: List[PriceBySize] = None
    active: bool = True


class CustomerOrders(BaseModel):
    """Modelo de ordenes de un cliente:

    - **id**: Identificador del cliente(Opcional)
    - **dummy_identifier**: Indica si el cliente no desea identificarse (Opcional = True)
    - **client_name**: Nombre del cliente (Obligatorio)
    - **registration_date**: Fecha de ingreso del registro (Auto)
    - **updated**: Fecha de actualizacion (Cada vez que se haga algun cambio sobre el ID)
    - **orders**: Lista que contiene las ordenes asociadas al cliente (Obligatorio [Una vez por pedido])

    """

    class Order(BaseModel):
        """Modelo de pedido por cliente:

        - **id**: Identificador de la orden(Auto)
        - **observation**: Observacion con respecto a la orden (Opcional)
        - **price**: Precio completo del pedido (Obligatorio)
        - **status**: Estado del pedido (Obligatorio) -> Documento de estados
        - **paid**: Indica si fue pagado (Opcional = False)
        - **investment**: Indica si hubo inversion por parte del vendedor (Opcional = False)
        - **pending**: Indica si la transaccion sigue pendiente (Opcional = True)
        - **registration_date**: Fecha de ingreso del registro (Auto)
        - **delivery_date**: Fecha y hora de entrega (Opcional)
        - **updated**: Fecha de actualizacion (Cada vez que se haga algun cambio sobre el ID)
        - **products**: Lista que contiene los codigos asociados a los productos (Obligatorio)

        """

        class ProductInList(BaseModel):
            id: int = 0
            amount: int
            type: str
            size: str

        id: int = 0
        observation: str = None
        price: float
        status: int
        paid: bool = False
        investment: bool = False
        pending: bool = True
        registration_date: datetime = datetime.utcnow()
        delivery_date: Union[datetime, None] = None
        updated: Union[datetime, None] = None
        products: List[ProductInList]

    id: int = 0
    dummy_identifier: bool = True
    client_name: str
    registration_date: datetime = datetime.utcnow()
    updated: Union[datetime, None] = None
    orders: List[Order]
