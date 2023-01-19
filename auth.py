from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from MongoDB.users_db_methods import UserDBMethods
from userApi.models import UserDb


class Auth:
    __users_db_methods = UserDBMethods()

    @classmethod
    def fake_hash_password(cls, password: str):
        return "fakehashed" + password

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    @classmethod
    async def get_current_user(cls, token: str = Depends(oauth2_scheme)) -> UserDb:
        print("get_current_user")
        if not cls.__users_db_methods.validate_user_by_username(token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return cls.__users_db_methods.get_user_from_db(token)

    # VALIDA LA VALIDEZ DEL USUARIO
    @classmethod
    async def get_current_active_user(cls, current_user: UserDb = Depends(get_current_user)) -> UserDb:
        print("get_current_active_user")
        if not current_user.active:
            print("if current_user.disabled:")
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user

    @classmethod
    async def validate_permissions(cls, scope: str, permission: str, user_db: UserDb):
        if scope not in user_db.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Does not have permissions"
            )
        if permission not in user_db.permissions:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Does not have permissions"
            )