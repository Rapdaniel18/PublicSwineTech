# app/models.py
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Date, Float, Integer

class Base(DeclarativeBase):
    pass

class Pig(Base):
    __tablename__ = "pigs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    tag_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    birth_date: Mapped[Date] = mapped_column(Date)
    breed: Mapped[str | None] = mapped_column(String(100), nullable=True)
    weight: Mapped[float | None] = mapped_column(Float, nullable=True)
    sex: Mapped[str | None] = mapped_column(String(1), nullable=True)