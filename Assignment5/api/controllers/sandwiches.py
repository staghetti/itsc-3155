from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import models, schemas


def create_sandwich(db: Session, sandwich: schemas.SandwichCreate):
    # Create a new instance of the Sandwich model with the provided data
    db_sandwich = models.Sandwich(**sandwich.dict())
    # Add the newly created Sandwich object to the database session
    db.add(db_sandwich)
    # Commit the changes to the database
    db.commit()
    # Refresh the Sandwich object to ensure it reflects the current state in the database
    db.refresh(db_sandwich)
    # Return the newly created Sandwich object
    return db_sandwich


def get_all_sandwiches(db: Session):
    return db.query(models.Sandwich).all()


def get_sandwich_by_id(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()


def update_sandwich(db: Session, sandwich_id: int, updated_sandwich: schemas.SandwichUpdate):
    # Query the database for the specific sandwich to update
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
    # Update the sandwich object with the provided data
    for field, value in updated_sandwich.dict(exclude_unset=True).items():
        setattr(db_sandwich, field, value)
    # Commit the changes to the database
    db.commit()
    # Return the updated sandwich object
    return db_sandwich


def delete_sandwich(db: Session, sandwich_id: int):
    # Query the database for the specific sandwich to delete
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
    # Delete the sandwich from the database
    db.delete(db_sandwich)
    # Commit the changes to the database
    db.commit()
    return {"message": "Sandwich deleted successfully"}
