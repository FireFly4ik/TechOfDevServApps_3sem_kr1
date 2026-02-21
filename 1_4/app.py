from fastapi import FastAPI
from models import User

app = FastAPI()

@app.get("/users")
async def users() -> User:
    return User(name="Галанов Андрей", id=1)