from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models

"""создаем модель жанра"""
class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)

"""создаем модель режисера"""
class Director(models.Base):
    __tablename__ = 'director'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    """создаем модель фильма"""
    __tablename__ = 'movie'
    title = Column(String(100), unique=True, nullable=False)
    description = Column(String(3000))
    trailer = Column(String(300))
    year = Column(Integer())
    rating = Column(Float())
    genre_id = Column(Integer(), ForeignKey("genre.id"))
    genre = relationship("Genre")
    director_id = Column(Integer(), ForeignKey("directors.id"))
    director = relationship("Director")




class User(models.Base):
    """создаем модель пользователя"""
    pass


class Favorite(models.Base):
    """создаем модель избранного(не Нео)"""
    pass