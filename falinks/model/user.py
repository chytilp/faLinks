from __future__ import annotations
from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from falinks.database import Model
from falinks.model.user_role import UserRole


class User(Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    active: Mapped[datetime]
    roles: Mapped[list[Role]] = relationship(secondary=UserRole, back_populates="users")

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name})"


class Role(Model):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    active: Mapped[datetime]
    users: Mapped[list[User]] = relationship(secondary=UserRole, back_populates="roles")

    def __repr__(self) -> str:
        return f"Role(id={self.id}, name={self.name})"
