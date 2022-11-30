from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbActor(Base):
    __tablename__ = 'actor'
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    image_2 = Column(String(100), nullable=False)
    image = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    description_long = Column(String(255), nullable=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('DbUser', back_populates='created_products')


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=True)
    created_products = relationship('DbActor', back_populates='owner')

