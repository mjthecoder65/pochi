from fastapi import APIRouter, Path
from wallet.functions import get_address
router = APIRouter()


@router.get('/api/pochi/v1/addresses/{address_index}')
async def get_wallet_address(currency: str, address_index: int = Path(..., ge=0)):
    return { "address": get_address(currency, address_index)}
