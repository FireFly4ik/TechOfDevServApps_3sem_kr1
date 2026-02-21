from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Calc(BaseModel):
    num1: int
    num2: int

@app.post("/calculate")
async def calc(calc_data: Calc):
    return {"result": calc_data.num1 + calc_data.num2}