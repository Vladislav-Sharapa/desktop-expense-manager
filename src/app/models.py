import datetime
from database.session import engine
from sqlalchemy import String, text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


class Base(DeclarativeBase):
    
    id: Mapped[int] = mapped_column(primary_key=True)


class ExpenseCategory(Base):
    __tablename__ = "expense_categories"
    
    title: Mapped[str]
    expenses: Mapped["Expense"] = relationship("Expense", back_populates="category", cascade='all, delete')


class Expense(Base):
    __tablename__ = "expenses"

    title: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    amount: Mapped[float]

    category_id: Mapped[int] = mapped_column(ForeignKey('expense_categories.id', ondelete='CASCADE'))
    category: Mapped["ExpenseCategory"] = relationship("ExpenseCategory", back_populates="expenses")

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    engine.echo = True
