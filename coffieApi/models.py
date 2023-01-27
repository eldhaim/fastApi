from typing import Union, List
from datetime import datetime
from pydantic import BaseModel


class TypesOfProduct(BaseModel):
    id: int
    name: str


class PriceBySize(BaseModel):
    size: str
    price: float


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

    id: int
    name: str
    description: str
    is_drink: bool = True
    registration_date: str = str(datetime.utcnow())
    updated: str = None
    types: List[TypesOfProduct] = None
    prices_by_sizes: List[PriceBySize] = None
    active: bool = True


class ProductInList(BaseModel):
    id: int
    amount: int
    type: str
    size: str
    registration_date: str = str(datetime.utcnow())


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

    id: int = None
    observation: str = None
    price: float
    status: int
    paid: bool = False
    investment: bool = False
    pending: bool = True
    registration_date: str = str(datetime.utcnow())
    delivery_date: str = None
    updated: str = None
    products: List[ProductInList]


class CustomerOrders(BaseModel):
    """Modelo de ordenes de un cliente:

    - **id**: Identificador del cliente(Opcional)
    - **dummy_identifier**: Indica si el cliente no desea identificarse (Opcional = True)
    - **client_name**: Nombre del cliente (Obligatorio)
    - **registration_date**: Fecha de ingreso del registro (Auto)
    - **updated**: Fecha de actualizacion (Cada vez que se haga algun cambio sobre el ID)
    - **orders**: Lista que contiene las ordenes asociadas al cliente (Obligatorio [Una vez por pedido])

    """

    id: int = 0
    dummy_identifier: bool = True
    client_name: str
    registration_date: str = str(datetime.utcnow())
    updated: str = None
    orders: List[Order]
