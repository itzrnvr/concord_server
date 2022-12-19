from fastapi import APIRouter

router = APIRouter()


@router.head("/ping")
async def ping():
    return "OK"


@router.get("/")
async def home():
    return "Yo brah"
