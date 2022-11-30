from fastapi import HTTPException, status
from router.schemas import actorRequestSchema
from sqlalchemy.orm.session import Session
from .actors_feed import actors
from sqlalchemy import func
from db.models import DbActor


def db_feed(db: Session):
    new_actor_list = [DbActor(
        category=actor["category"],
        name=actor["name"],
        sku=actor["sku"],
        price=actor["price"],
        image=actor["image"],
        description=actor["description"],
        description_long=actor["description_long"],
        currency=actor["currency"],
        countInStock=actor["countInStock"]
    ) for actor in actors]
    db.query(DbActor).delete()
    db.commit()
    db.add_all(new_actor_list)
    db.commit()
    return db.query(DbActor).all()


def create(db: Session, request: actorRequestSchema):
    new_actor = DbActor(
        category=request.category,
        name=request.name,
        sku=request.sku,
        # price=request.price,
        image=request.image,
        description=request.description,
        description_long=request.description_long,
        currency=request.currency,
        countInStock=request.countInStock
    )
    db.add(new_actor)
    db.commit()
    db.refresh(new_actor)
    return new_actor


def get_all(db: Session):
    return db.query(DbActor).all()


def get_product_by_id(product_id: int, db: Session):
    product = db.query(DbActor).filter(DbActor.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Product with id = {id} not found')
    return product


# def get_product_by_category(category: str, db: Session):
#     product = db.query(DbProduct).filter(DbProduct.category == category).all()
#     if not product:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'Product with category = {id} not found')
#     return product
def get_product_by_category(category: str, db: Session) -> list[DbActor]:
    product = db.query(DbActor).filter(func.upper(DbActor.category) == category.upper()).all()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Product with category = {category} not found')
    return product