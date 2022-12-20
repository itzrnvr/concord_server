import json

from fastapi import APIRouter
from ..database import Database
from ..models.user import User

baseApi = "/api/v1"
router = APIRouter(prefix=baseApi + "/auth/users")
db = Database()


@router.post("/login")
async def login(user: User):
    return db.login(user)


@router.post("/register")
async def register(user: User):
    return db.register(user)


@router.get("/all")
async def getAllUsers():
    return db.getAllUsers()


@router.delete("/remove/{userID}")
async def deleteUser(userID: int):
    return db.deleteUser(userID)
