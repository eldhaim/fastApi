from typing import List

import commons
from MongoDB import variables
from MongoDB.mongoDB import Database
from coffieApi import variables as var, messages, serializers
from coffieApi.models import CustomerOrders, Order, ProductInList
from fastapi import status


class CustomersOrdersMethods:
    def __init__(self):
        self.__customers_orders_table = Database.collection(var.COLL_CUSTOMER_ORDERS)
        self.__products_table = Database.collection(var.COLL_PRODUCTS)

    def val_customer_orders_by_id(self, _id: int) -> bool:
        query = {variables.ID: _id}
        try:
            if self.__customers_orders_table.find(query)[0] is not None:
                return True
        except Exception as e:
            print(f"CLIENTE CON ID {_id} NO ENCONTRADO: {e}")
            return False

    def status_validation(self, status_order: int):  # CREAR TABLA Y VALIDAR QUE EXISTA
        validacion = True  # debe llenarse aca y cambiar nombre de la variable
        commons.validation_for_response(
            condition=validacion,
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=messages.SET_ORDER_HTTP_BAD_REQUEST_STATUS
        )

    def validate_product_type(self, product_type_id: str):  # CREAR TABLA Y VALIDAR QUE EXISTA
        validacion = True  # debe llenarse aca y cambiar nombre de la variable
        commons.validation_for_response(
            condition=validacion,
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=messages.SET_ORDER_HTTP_BAD_REQUEST_TYPE
        )

    def validate_product_id(self, product_id: int):  # CREAR TABLA Y VALIDAR QUE EXISTA
        validacion = True  # debe llenarse aca y cambiar nombre de la variable
        commons.validation_for_response(
            condition=validacion,
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=messages.SET_ORDER_HTTP_BAD_REQUEST_PRODUCT_ID
        )

    def validate_size(self, product_size: str):  # CREAR TABLA Y VALIDAR QUE EXISTA
        validacion = True  # debe llenarse aca y cambiar nombre de la variable
        commons.validation_for_response(
            condition=validacion,
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=messages.SET_ORDER_HTTP_BAD_REQUEST_SIZE
        )

    def validate_product(self, product_list: List[ProductInList]):#RECUPERAR PRODUCTO DE LA BASE Y TRATAR
        for product in product_list:
            self.validate_product_id(product.id)
            self.validate_product_type(product.type)
            self.validate_size(product.size)

    def set_customer_orders(self, customer_orders: CustomerOrders) -> CustomerOrders:
        orders: Order = customer_orders.orders[0]
        self.status_validation(orders.status)
        self.validate_product(orders.products)
        self.__customers_orders_table.insert_one(serializers.customer_order(customer_orders))
        return customer_orders

    def update_customer_orders(self, customer_orders: CustomerOrders) -> CustomerOrders:#POSIBLE PUT
        pass
