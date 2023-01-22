from fastapi import HTTPException, status
from typing import List
from MongoDB.coffie.customer_orders_methods import CustomerOrdersMethods
from coffieApi import messages
from coffieApi.models import Order, CustomerOrders


class CustomerOrdersController:
    a = 1