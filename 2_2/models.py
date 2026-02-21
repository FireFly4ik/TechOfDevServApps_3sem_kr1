import re
from pydantic import BaseModel, Field, field_validator

class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    @field_validator('message')
    def val_msg(cls, s):
        s = s.lower()
        for i in ('кринж', 'рофл', 'вайб'):
            if re.search(rf'\b{i}[а-яё]*\b', s):
                raise ValueError('мы не кринжуем, не вайбим и не рофлим')
        return s