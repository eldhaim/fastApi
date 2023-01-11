# TAGS
TAG_DATA = "TREATMENT OF USERS DATA"
# BASIC RESPONSES
BASIC_RESPONSES = {
    400: {
        "message": "Bad request"
    }
}
# GET_USER
GET_USERS_HTTP_OK = "Existe uno o mas usuarios"
GET_USERS_HTTP_BAD_REQUEST = "No existen usuarios"
GET_USERS_SUMMARY = "Consultar usuarios"
# GET_USER_BY_USERNAME
GET_USER_BY_USERNAME_HTTP_OK = "Existe el usuario solicitado"
GET_USER_BY_USERNAME_HTTP_BAD_REQUEST = "El usuario con username [0] no existe"
GET_USER_BY_USERNAME_SUMMARY = "Consultar usuario por username"
# SET_USER
SET_USER_HTTP_OK = "El usuario fue insertado correctamente"
SET_USER_HTTP_BAD_REQUEST = "El usuario con username [0] ya existe"
SET_USER_SUMMARY = "Crear usuario"
# PUT_USER
PUT_USER_HTTP_OK = "El usuario fue actualizado correctamente"
PUT_USER_HTTP_BAD_REQUEST = "El usuario con username [0] no existe"
PUT_USER_HTTP_BAD_REQUEST_PARAMS = "Debe actualizar por lo menos un campo"
PUT_USER_SUMMARY = "Actualizar un usuario"
