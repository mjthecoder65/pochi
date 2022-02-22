from fastapi import APIRouter, Path
from wallet.functions import get_address
router = APIRouter()


@router.post('/api/pochi/v1/transactions')
async def send_money(currency: str, address_index: int = Path(..., ge=0)):
    return { "address": get_address(currency, address_index)}
