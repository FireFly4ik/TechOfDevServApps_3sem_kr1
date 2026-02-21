from fastapi import FastAPI
from models import Feedback

app = FastAPI()

@app.post("/feedback")
async def feedback(feedback_data: Feedback) -> dict:
    return {"message": f"Feedback received. Thank you, {feedback_data.name}"}