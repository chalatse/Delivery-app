from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.get('/auth')
async def hello():
    return{"Hello":"auth router is UP"}
