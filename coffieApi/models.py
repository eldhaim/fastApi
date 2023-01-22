from itertools import product
from typing import Union, List
from datetime import datetime
from pydantic import BaseModel


class Order(BaseModel):
    """Modelo de pedido por cliente"""
    id: int = 0
    products: List[int]
    observation: str
    price: float
    status: int
    paid: bool = False
    investment: bool = False
    pending: bool = True
    registration_date: datetime = datetime.utcnow()
    delivery_date: Union[datetime, None] = None
    updated: Union[datetime, None] = None


class CustomerOrders(BaseModel):
    """Modelo de cliente"""
    id: int = 0
    dummy_identifier: bool = True
    client_name: str
    registration_date: datetime = datetime.utcnow()
    updated: Union[datetime, None] = None
    orders: List[Order]
