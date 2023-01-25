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
SET_ORDER_HTTP_BAD_REQUEST_DUMMY = response(2, "Si el cliente no se identifica no debe ingresar identificacion")
SET_ORDER_SUMMARY = "Ingresar orden"
