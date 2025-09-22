from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.category import Category
from app.schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryOut

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=list[CategoryOut])
def read_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@router.get("/{category_id}", response_model=CategoryOut)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/", response_model=CategoryOut)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.put("/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    for key, value in category.dict(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.delete("/{category_id}", response_model=CategoryOut)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(db_category)
    db.commit()
    return db_category
