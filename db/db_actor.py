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
        image_2=actor["image_2"],
        image=actor["image"],
        description=actor["description"],
        description_long=actor["description_long"],
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
        image=request.image,
        image_2=request.image_2,
        description=request.description,
        description_long=request.description_long,
    )
    db.add(new_actor)
    db.commit()
    db.refresh(new_actor)
    return new_actor


def get_all(db: Session):
    return db.query(DbActor).all()


def get_actor_by_id(actor_id: int, db: Session):
    actor = db.query(DbActor).filter(DbActor.id == actor_id).first()
    if not actor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Actor with id = {id} not found')
    return actor

def get_actor_by_category(category: str, db: Session) -> list[DbActor]:
    actor = db.query(DbActor).filter(func.upper(DbActor.category) == category.upper()).all()
    if not actor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Actor with category = {category} not found')
    return actor