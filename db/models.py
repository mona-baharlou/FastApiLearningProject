from uuid import UUID, uuid4

from sqlalchemy import String
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import Mapped, mapped_column

from .engine import Base


class User(Base):
    __tablename__ = "Users"

    username: Mapped[str] = mapped_column(String(150), unique=True,
                                          nullable=False)
    password: Mapped[str] = mapped_column(String(150), nullable=False)

    id: Mapped[UUID] = mapped_column(UNIQUEIDENTIFIER, primary_key=True,
                                     default=uuid4)
