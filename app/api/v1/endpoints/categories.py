from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.category import Category
from app.schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryOut
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter(tags=["categories"])

@router.get("/", response_model=list[CategoryOut])
def read_categories(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # retorna apenas as categorias do usuário logado
    return db.query(Category).filter(Category.user_id == current_user.id).all()

@router.get("/{category_id}", response_model=CategoryOut)
def read_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    category = db.query(Category).filter(
        Category.id == category_id, Category.user_id == current_user.id
    ).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/", response_model=CategoryOut)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_category = Category(**category.dict(), user_id=current_user.id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.put("/{category_id}", response_model=CategoryOut)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_category = db.query(Category).filter(
        Category.id == category_id, Category.user_id == current_user.id
    ).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    for key, value in category.dict(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.delete("/{category_id}", response_model=CategoryOut)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_category = db.query(Category).filter(
        Category.id == category_id, Category.user_id == current_user.id
    ).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(db_category)
    db.commit()
    return db_category
