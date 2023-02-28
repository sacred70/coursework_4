from sqlalchemy import Column, String, Integer, Float, ForeignKey

from project.setup.db import models

"""создаем модель жанра"""
class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)

"""создаем модель режисера"""
class Director(models.Base):
    __tablename__ = 'director'

    name = Column(String(100), unique=True, nullable=False)


"""создаем модель фильма"""
class Movie(models.Base):
    pass



"""создаем модель пользователя"""

class User(models.Base):
    pass

"""создаем модель избранного(не Нео)"""
class Favorite(models.Base):
    pass