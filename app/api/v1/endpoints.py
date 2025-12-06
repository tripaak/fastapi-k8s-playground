"""
API v1 endpoints for food items.

Objective: Define FastAPI route handlers for CRUD operations on food items.
Why: Keeps endpoints organized by version and entity type. Each handler maps HTTP requests to business logic.
Gotcha: Dependency injection (Depends) is used for DB session and other dependencies.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.item import FoodItemCreate, FoodItemUpdate, FoodItemResponse
from app.services.item_service import ItemService

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=List[FoodItemResponse])
def list_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """List all food items with pagination."""
    items = ItemService.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=FoodItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """Retrieve a single food item by ID."""
    item = ItemService.get_item(db, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return item


@router.post("/", response_model=FoodItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: FoodItemCreate, db: Session = Depends(get_db)):
    """Create a new food item."""
    existing_item = ItemService.get_item_by_name(db, item.name)
    if existing_item:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Item with name '{item.name}' already exists",
        )
    return ItemService.create_item(db, item)


@router.put("/{item_id}", response_model=FoodItemResponse)
def update_item(
    item_id: int,
    item_update: FoodItemUpdate,
    db: Session = Depends(get_db),
):
    """Update an existing food item."""
    db_item = ItemService.get_item(db, item_id)
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return ItemService.update_item(db, item_id, item_update)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete a food item by ID."""
    success = ItemService.delete_item(db, item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return None
