# Objective: Define the SQL table and columns (SQLAlchemy FoodItem model).
# Why: The model is the authoritative schema for how data is persisted in Postgres. It defines types, constraints (e.g., unique, nullable), indexes and primary keys.
# Gotcha: Ensure DB column types map to your Pydantic types and consider constraints (unique name? case sensitivity?). Add indexes on frequently queried columns.



from sqlalchemy import Column, Integer, String, Text, Float
from app.db.base import Base

class FoodItem(Base):
    __tablename__ = "food_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    calories = Column(Integer, nullable=True)
    protien = Column(Float, nullable=True)
    fat = Column(Float, nullable=True)