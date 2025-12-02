# Objective: Define request/response data shapes (validation + serialization) using Pydantic models.
# Why: Schemas validate incoming data and control what your API returns. They protect against bad input and ensure consistent output. orm_mode = True makes Pydantic read SQLAlchemy objects.
# Gotcha: Separate create/update schemas from response schema so you don’t accept or expose fields you shouldn’t (e.g., id in create request).

from pydantic import BaseModel

class FoodItemBase(BaseModel):
    name: str
    calories: int | None = None
    protien: float | None = None
    fat: float | None = None

class FoodItemCreate(FoodItemBase):
    pass        

class FoodItemUpdate(FoodItemBase):
    pass        

class FoodItemResponse(FoodItemBase):
    id: int

    class Config:
        orm_mode = True