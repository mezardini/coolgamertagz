from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import declarative_base, relationship
from enum import Enum

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256))
    email = Column(String(256))


class GamerTag(Base):
    __tablename__ = 'gamer_tags'
    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String(256))
    prompt = Column(String(256))
