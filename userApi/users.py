from fastapi import APIRouter, HTTPException

from userApi.modelos import User

router = APIRouter()

usuarios = []


@router.get("/users", status_code=200)
async def users():
    """EndPoint para traer lista de ususarios"""
    if len(usuarios) == 0:
        raise HTTPException(status_code=400, detail="No existen usuarios")
    return usuarios
