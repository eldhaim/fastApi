from fastapi import HTTPException, status
import commons
from MongoDB.coffie.customer_orders_methods import CustomersOrdersMethods
from coffieApi import messages, variables as var
from coffieApi.models import CustomerOrders


class CustomerOrdersController:
    """Objeto encargado de comunicar los metodos de base de datos con el 'router'"""

    def __init__(self):
        self.__cust_orders_db_methods = CustomersOrdersMethods()

    def validation_for_response(self,
                                condition: bool,
                                status_code: int,
                                detail: dict):
        if condition:
            raise HTTPException(
                status_code=status_code,
                detail=detail
            )

    def set_customer_order(self, customer_orders: CustomerOrders):
        if customer_orders.dummy_identifier:
            if customer_orders.id != 0:
                self.validation_for_response(
                    condition=self.__cust_orders_db_methods.val_customer_orders_by_id(customer_orders.id),
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=messages.SET_ORDER_HTTP_BAD_REQUEST_DUMMY
                )
