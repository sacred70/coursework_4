from project.setup.db import db
from sqlalchemy import Column, DateTime, func, Integer


class Base(db.Model):
    # Базовый класс для создания моделей
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())
