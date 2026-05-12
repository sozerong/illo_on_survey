from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import UserBase


class User(UserBase):
    __tablename__ = "users"

    id:         Mapped[str]      = mapped_column(String(36), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    survey: Mapped[Optional["Survey"]] = relationship(back_populates="user", uselist=False)


class Survey(UserBase):
    __tablename__ = "surveys"

    id:          Mapped[str]           = mapped_column(String(36), primary_key=True)
    user_id:     Mapped[str]           = mapped_column(ForeignKey("users.id"), unique=True)
    job_type:    Mapped[Optional[str]] = mapped_column(String(100))
    region:      Mapped[Optional[str]] = mapped_column(String(100))
    occupation:  Mapped[Optional[str]] = mapped_column(String(100))
    career_type: Mapped[Optional[str]] = mapped_column(String(20))
    education:   Mapped[Optional[str]] = mapped_column(String(50))
    created_at:  Mapped[datetime]      = mapped_column(DateTime, default=datetime.utcnow)
    updated_at:  Mapped[datetime]      = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user: Mapped["User"] = relationship(back_populates="survey")
