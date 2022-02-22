from fastapi import FastAPI
import uvicorn
from routes.addresses import router as address_routes
from routes.users import router as user_routes

app = FastAPI()
app.include_router(address_routes)
app.include_router(user_routes)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=4000, reload=True)

