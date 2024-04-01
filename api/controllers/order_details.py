from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import models, schemas


def create_order_detail(db: Session, order_detail: schemas.OrderDetailCreate):
    # Create a new instance of the OrderDetail model with the provided data
    db_order_detail = models.OrderDetail(**order_detail.dict())
    # Add the newly created OrderDetail object to the database session
    db.add(db_order_detail)
    # Commit the changes to the database
    db.commit()
    # Refresh the OrderDetail object to ensure it reflects the current state in the database
    db.refresh(db_order_detail)
    # Return the newly created OrderDetail object
    return db_order_detail


def get_all_order_details(db: Session):
    return db.query(models.OrderDetail).all()


def get_order_detail_by_id(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()


def update_order_detail(db: Session, order_detail_id: int, updated_order_detail: schemas.OrderDetailUpdate):
    # Query the database for the specific order detail to update
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if db_order_detail is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found")
    # Update the order detail object with the provided data
    for field, value in updated_order_detail.dict(exclude_unset=True).items():
        setattr(db_order_detail, field, value)
    # Commit the changes to the database
    db.commit()
    # Return the updated order detail object
    return db_order_detail


def delete_order_detail(db: Session, order_detail_id: int):
    # Query the database for the specific order detail to delete
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if db_order_detail is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found")
    # Delete the order detail from the database
    db.delete(db_order_detail)
    # Commit the changes to the database
    db.commit()
    return {"message": "Order detail deleted successfully"}
