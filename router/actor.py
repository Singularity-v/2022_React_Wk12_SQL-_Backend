from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import actorRequestSchema, actorResponseSchema
from db.database import get_db
from db import db_actor
from typing import List

router = APIRouter(
    prefix='/api/v1/actors',
    tags=['actors']
)

@router.post('', response_model=actorResponseSchema)
def create(request: actorRequestSchema, db: Session = Depends(get_db)):
    return db_actor.create(db, request)

@router.get('/feed', response_model=List[actorResponseSchema])
def feed_initial_actors(db: Session = Depends(get_db)):
    return db_actor.db_feed(db)


@router.get('/all', response_model=List[actorResponseSchema])
def get_all_actors(db: Session = Depends(get_db)):
    return db_actor.get_all(db)


@router.get('/id/{actor_id}', response_model=actorResponseSchema)
def get_actor_by_id(actor_id: int, db: Session = Depends(get_db)):
    return db_actor.get_actor_by_id(actor_id, db)


@router.get("/{category}", response_model=List[actorResponseSchema])
def get_actor_by_category(category:str, db: Session = Depends(get_db)):
    return db_actor.get_actor_by_category(category, db)