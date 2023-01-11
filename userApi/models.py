from typing import Union

from pydantic import BaseModel


class User(BaseModel):
    """
    Creacion de un usuario con toda la informacion:

    - **username**: Identificador del usuario (obligatiorio)
    - **name**: Nombre del usuario (obligatior)
    - **last_name**: Apellido del usuario (obligatior)
    - **email**: Correco electronico del usuario (Opcional)
    """
    username: str
    name: str
    last_name: str
    email: Union[str, None] = None

    def update_user(
            self,
            name: str = None,
            last_name: str = None,
            email: str = None
    ):
        """Cambia los datos del usuario
    :param name: Nombre del usuario input (Opcional).
    :param last_name: Apellido del usuario input (Opcional).
    :param email: Email del usuario input (Opcional)."""
        self.name = name if name is not None else self.name
        self.last_name = last_name if last_name is not None else self.last_name
        self.email = email if email is not None else self.email
