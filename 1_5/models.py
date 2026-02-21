from pydantic import BaseModel, computed_field

class User(BaseModel):
    name: str
    age: int

    @computed_field
    @property
    def is_adult(self) -> bool:
        return self.age >= 18