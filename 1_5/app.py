from fastapi import FastAPI
from models import User

app = FastAPI()

@app.post("/user")
async def user(user_data: User) -> User:
    return user_data