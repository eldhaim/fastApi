# TAGS
TAG_DATA = "TREATMENT OF ORDERS BY CUSTOMER"
# BASIC RESPONSES
BASIC_RESPONSES = {
    400: {
        "message": "Bad request"
    }
}


# Methods
def response(code: int, message: str):
    return {
        "code": code,
        "message": message
    }


# SET_ORDER
SET_ORDER_HTTP_OK = response(1, "El usuario fue insertado correctamente")
SET_ORDER_HTTP_BAD_REQUEST_DUMMY = response(2, "Si el cliente no se identifica la identificación debe ser 0")
SET_ORDER_HTTP_BAD_REQUEST_STATUS = response(3, "Status inexistente")
SET_ORDER_HTTP_BAD_REQUEST_TYPE = response(4, "Tipo de producto inexistente")
SET_ORDER_HTTP_BAD_REQUEST_PRODUCT_ID = response(5, "Prodcuto inexistente")
SET_ORDER_HTTP_BAD_REQUEST_SIZE = response(6, "Tamanio del producto inexistente")
SET_ORDER_SUMMARY = "Ingresar orden"
