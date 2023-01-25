from MongoDB import variables
from MongoDB.mongoDB import Database
from coffieApi import variables as var
from coffieApi.models import CustomerOrders


class CustomersOrdersMethods:
    def __init__(self):
        self.__customers_orders_table = Database.collection(var.COLL_CUSTOMER_ORDERS)
        self.__products_table = Database.collection(var.COLL_PRODUCTS)

    def set_customer_order(self, customer_orders: CustomerOrders):
        pass

    def val_customer_orders_by_id(self, _id: int) -> bool:
        query = {variables.ID: _id}
        try:
            if self.__customers_orders_table.find(query)[0] is not None:
                return True
        except Exception as e:
            print(f"CLIENTE CON ID {_id} NO ENCONTRADO: {e}")
            return False

    # def query(self, query: dict):
