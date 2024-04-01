from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import models, schemas


def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    # Create a new instance of the Recipe model with the provided data
    db_recipe = models.Recipe(**recipe.dict())
    # Add the newly created Recipe object to the database session
    db.add(db_recipe)
    # Commit the changes to the database
    db.commit()
    # Refresh the Recipe object to ensure it reflects the current state in the database
    db.refresh(db_recipe)
    # Return the newly created Recipe object
    return db_recipe


def get_all_recipes(db: Session):
    return db.query(models.Recipe).all()


def get_recipe_by_id(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()


def update_recipe(db: Session, recipe_id: int, updated_recipe: schemas.RecipeUpdate):
    # Query the database for the specific recipe to update
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    # Update the recipe object with the provided data
    for field, value in updated_recipe.dict(exclude_unset=True).items():
        setattr(db_recipe, field, value)
    # Commit the changes to the database
    db.commit()
    # Return the updated recipe object
    return db_recipe


def delete_recipe(db: Session, recipe_id: int):
    # Query the database for the specific recipe to delete
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    # Delete the recipe from the database
    db.delete(db_recipe)
    # Commit the changes to the database
    db.commit()
    return {"message": "Recipe deleted successfully"}
