from fastapi import FastAPI
from models import Feedback

app = FastAPI()
feedbacks = []

@app.post("/feedback")
async def feedback(feedback_data: Feedback) -> dict:
    feedbacks.append(feedback_data)
    return {"message": f"Спасибо, {feedback_data.name}! Ваш отзыв сохранён."}