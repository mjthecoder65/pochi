from fastapi import APIRouter, Path
router = APIRouter()


@router.get("/api/pochi/v1/users")
async def read_users():
    return {}


@router.get("/api/pochi/v1/users/{id}")
async def read_user(id: int = Path(..., ge=0)):
    return { "id": id }

@router.post("/api/pochi/v1/users")
async def create_users():
    return {}


@router.put("/api/pochi/v1/users/{id}")
async def update_user(id: int = Path(..., ge=0)):
    return {"id": id }

@router.delete("/api/pochi/v1/users/{id}")
async def read_users(id: int = Path(..., ge=0)):
    return { "id": id }
