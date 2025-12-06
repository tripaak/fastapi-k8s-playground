"""
Item Service - Business logic for managing food items.

Objective: Encapsulate CRUD operations and business logic for food items.
Why: Separates database operations from API endpoints, making code reusable and testable.
Gotcha: Always use the session passed in, don't create your own. Handle DB errors gracefully.
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.models.item import FoodItem
from app.schemas.item import FoodItemCreate, FoodItemUpdate, FoodItemResponse
from typing import List, Optional


class ItemService:
    """Service class for managing food items."""

    @staticmethod
    def get_item(db: Session, item_id: int) -> Optional[FoodItem]:
        """Retrieve a single item by ID."""
        return db.query(FoodItem).filter(FoodItem.id == item_id).first()

    @staticmethod
    def get_items(
        db: Session,
        skip: int = 0,
        limit: int = 100,
    ) -> List[FoodItem]:
        """Retrieve multiple items with pagination."""
        return db.query(FoodItem).offset(skip).limit(limit).all()

    @staticmethod
    def get_item_by_name(db: Session, name: str) -> Optional[FoodItem]:
        """Retrieve an item by name."""
        return db.query(FoodItem).filter(FoodItem.name == name).first()

    @staticmethod
    def create_item(db: Session, item: FoodItemCreate) -> FoodItem:
        """Create a new food item."""
        try:
            db_item = FoodItem(
                name=item.name,
                calories=item.calories,
                protien=item.protien,
                fat=item.fat,
            )
            db.add(db_item)
            db.commit()
            db.refresh(db_item)
            return db_item
        except IntegrityError as e:
            db.rollback()
            raise ValueError(f"Database integrity error: {str(e)}")

    @staticmethod
    def update_item(
        db: Session,
        item_id: int,
        item_update: FoodItemUpdate,
    ) -> Optional[FoodItem]:
        """Update an existing food item."""
        db_item = db.query(FoodItem).filter(FoodItem.id == item_id).first()
        if not db_item:
            return None

        update_data = item_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_item, field, value)

        try:
            db.add(db_item)
            db.commit()
            db.refresh(db_item)
            return db_item
        except IntegrityError as e:
            db.rollback()
            raise ValueError(f"Database integrity error: {str(e)}")

    @staticmethod
    def delete_item(db: Session, item_id: int) -> bool:
        """Delete a food item by ID."""
        db_item = db.query(FoodItem).filter(FoodItem.id == item_id).first()
        if not db_item:
            return False

        db.delete(db_item)
        db.commit()
        return True
