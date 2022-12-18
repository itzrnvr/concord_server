from fastapi import APIRouter
from .home import router as homeRouter
from .authenticate import router as authRouter
from .chat import router as chatRouter


