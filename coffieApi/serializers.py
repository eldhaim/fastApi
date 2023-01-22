from userApi.models import UserDb
from userApi import serializers_variables as svar


def user_serializer(user: UserDb):
    return {
        svar.ID: user.username,
        svar.NAME: user.name,
        svar.LAST_NAME: user.last_name,
        svar.EMAIL: user.email,
        svar.ACTIVE: user.active,
        svar.PASSWORD: user.password
    }
