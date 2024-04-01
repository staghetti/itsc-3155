from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import models, schemas


def create_resource(db: Session, resource: schemas.ResourceCreate):
    # Create a new instance of the Resource model with the provided data
    db_resource = models.Resource(**resource.dict())
    # Add the newly created Resource object to the database session
    db.add(db_resource)
    # Commit the changes to the database
    db.commit()
    # Refresh the Resource object to ensure it reflects the current state in the database
    db.refresh(db_resource)
    # Return the newly created Resource object
    return db_resource


def get_all_resources(db: Session):
    return db.query(models.Resource).all()


def get_resource_by_id(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()


def update_resource(db: Session, resource_id: int, updated_resource: schemas.ResourceUpdate):
    # Query the database for the specific resource to update
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if db_resource is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    # Update the resource object with the provided data
    for field, value in updated_resource.dict(exclude_unset=True).items():
        setattr(db_resource, field, value)
    # Commit the changes to the database
    db.commit()
    # Return the updated resource object
    return db_resource


def delete_resource(db: Session, resource_id: int):
    # Query the database for the specific resource to delete
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if db_resource is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    # Delete the resource from the database
    db.delete(db_resource)
    # Commit the changes to the database
    db.commit()
    return {"message": "Resource deleted successfully"}
