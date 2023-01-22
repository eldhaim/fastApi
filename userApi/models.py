from typing import Union, List
from pydantic import BaseModel


class User(BaseModel):
    """
    Creacion de un usuario con toda la informacion:

    - **username**: Identificador del usuario (obligatiorio)
    - **name**: Nombre del usuario (obligatior)
    - **last_name**: Apellido del usuario (obligatior)
    - **email**: Correco electronico del usuario (Opcional)
    - **active**: Indica si el usuario esta activo (Opcional)
    """
    username: str
    name: str
    last_name: str
    email: Union[str, None] = None
    active: bool = True


class UserDb(User):
    """
    Usuario con contraseña para uso de la DB:

    - **username**: Identificador del usuario (obligatiorio)
    - **name**: Nombre del usuario (obligatior)
    - **last_name**: Apellido del usuario (obligatior)
    - **email**: Correco electronico del usuario (Opcional)
    - **password**: Contraseña del usuario (obligatiorio)
    - **scopes**: Apis a las que pertenece (Debe ser ingresado por DB)
    - **permissions**: Contiene los permisos [READ, WRITE, UPDATE, DELETE] (Debe ser ingresado por DB)
    """
    password: str
    scopes: List[int] = []
    permissions: List[str] = []

    def update_user(
            self,
            name: str = None,
            last_name: str = None,
            email: str = None,
            active: bool = None,
            password: str = None
    ):
        """Cambia los datos del usuario
        :param password: Contrasena del usuario (Opcional).
        :param active: Indicador de actividad del usuario (Opcional).
        :param name: Nombre del usuario input (Opcional).
        :param last_name: Apellido del usuario input (Opcional).
        :param email: Email del usuario input (Opcional)."""
        self.name = name if name is not None else self.name
        self.last_name = last_name if last_name is not None else self.last_name
        self.email = email if email is not None else self.email
        self.active = active if active is not None else self.active
        self.password = password if password is not None else self.password
