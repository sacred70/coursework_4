from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    """создаем модель жанра"""
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    """создаем модель режисера"""
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    """создаем модель фильма"""
    __tablename__ = 'movies'
    title = Column(String(100), unique=True, nullable=False)
    description = Column(String(3000))
    trailer = Column(String(300))
    year = Column(Integer())
    rating = Column(Float())
    genre_id = Column(Integer(), ForeignKey("genre.id"), nullable=False)
    genre = relationship("Genre")
    director_id = Column(Integer(), ForeignKey("director.id"), nullable=False)
    director = relationship("Director")


class User(models.Base):
    """создаем модель пользователя"""
    __tablename__ = 'users'
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favorite_genre = Column(String(100))


class Favorite(models.Base):
    """создаем модель избранного"""
    __tablename__ = 'favorites'
    user_id = Column(Integer(), ForeignKey("users.id"))
    user = relationship("User")
    movie_id = Column(Integer(), ForeignKey("movies.id"))
    movie = relationship("Movie")
