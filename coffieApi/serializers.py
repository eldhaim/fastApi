from typing import List, Dict

from coffieApi import variables as var
from coffieApi.models import CustomerOrders, Order, ProductInList


def _products(products: List[ProductInList]) -> List[Dict]:
    products_list: List[Dict] = []
    for product in products:
        product_dict: Dict = {
            var.ID: product.id,
            var.AMOUNT: product.amount,
            var.TYPE: product.type,
            var.SIZE: product.size,
            var.REGISTRATION_DATE: product.registration_date
        }
        products_list.append(product_dict)
    return products_list


def _orders(orders: List[Order]) -> List[Dict]:
    orders_list: List[Dict] = []
    for order in orders:
        order_dict: Dict = {
            var.ID: order.id,
            var.OBSERVATION: order.observation,
            var.PRICE: order.price,
            var.STATUS: order.status,
            var.PAID: order.paid,
            var.INVESTMENT: order.investment,
            var.PENDING: order.pending,
            var.REGISTRATION_DATE: order.registration_date,
            var.DELIVERY_DATE: order.delivery_date,
            var.UPDATED: order.updated,
            var.PRODUCTS: _products(order.products)
        }
        orders_list.append(order_dict)
    return orders_list


def customer_order(customer_orders: CustomerOrders):
    return {
        var._ID: customer_orders.id,
        var.DUMMY_IDENTIFIER: customer_orders.dummy_identifier,
        var.CLIENT_NAME: customer_orders.client_name,
        var.REGISTRATION_DATE: customer_orders.registration_date,
        var.UPDATED: customer_orders.updated,
        var.ORDERS: _orders(customer_orders.orders)
    }
