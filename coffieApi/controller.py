from fastapi import status
import commons
from MongoDB.coffie.customer_orders_methods import CustomersOrdersMethods
from coffieApi import messages, variables as var
from coffieApi.models import CustomerOrders


class CustomerOrdersController:
    """Objeto encargado de comunicar los metodos de base de datos con el 'router'"""

    def __init__(self):
        self.__cust_orders_db_methods: CustomersOrdersMethods = CustomersOrdersMethods()
        self.__customer_order = None

    def validate_order(self) -> CustomerOrders:
        if self.__cust_orders_db_methods.val_customer_orders_by_id(self.__customer_order.id):
            return self.__cust_orders_db_methods.update_customer_orders(self.__customer_order)
        else:
            return self.__cust_orders_db_methods.set_customer_orders(self.__customer_order)

    def set_customer_order(self, customer_orders: CustomerOrders) -> CustomerOrders:
        self.__customer_order = customer_orders
        if self.__customer_order.dummy_identifier:
            if self.__customer_order.id != 0:
                commons.validation_for_response(
                    condition=False,
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=messages.SET_ORDER_HTTP_BAD_REQUEST_DUMMY
                )
        return self.validate_order()
