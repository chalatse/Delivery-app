from fastapi import APIRouter

order_router = APIRouter()

@order_router.get('/order')
async def root():
    return {"Hello":"The oder router is UP"}

