from typing import TypeVar, Generic
from sqlalchemy import func, select
from sqlalchemy.orm import Session
from .models import Base, Expense, ExpenseCategory

Model = TypeVar("Model", bound=Base)


class BaseRepository(Generic[Model]):
    def __init__(self, model: type[Model], session: Session) -> None:
        self.session = session
        self.model = model
        
    def create(self, data: dict) -> Model:
        instance = self.model(**data)
        self.session.add(instance)
        
        return instance
    
    def delete(self, id: int) -> bool:
        instanse = self.__get_by_id(id)
        if instanse: 
            self.session.delete(instanse)
            return True
        return False
    
    def update(self, id: int, data:dict):
        instanse = self.session.query(self.model).filter(self.model.id == id)
        if instanse: 
            instanse.update(data)
    
    def __get_by_id(self, id: int) -> Model:
        instance = self.session.query(self.model).get(id)
        return instance
    
    def get_all(self):
        pass
    

class ExpenseRepository(BaseRepository[Expense]):
    """Repository to interect with `expanses` table in database"""
    def __init__(self, session: Session) -> None:
        super().__init__(Expense, session)

    def get_total(self) -> float:
        '''Get total sum of amount column in `expenses` table'''
        return self.session.query(func.sum(self.model.amount)).scalar()

    def get_all(self):
        query = (
            select(self.model.id,
                   self.model.title,
                   self.model.created_at,
                   self.model.amount,
                   self.model.category_id,
                   ExpenseCategory.title.label('cat')
                ).select_from(self.model).join(ExpenseCategory, self.model.category_id == ExpenseCategory.id)
        )
        return self.session.execute(query).all()
    
class ExpenseCategoryRepository(BaseRepository[ExpenseCategory]):
    """Repository to interect with `expanses category` table in database"""
    def __init__(self, session: Session) -> None:
        super().__init__(ExpenseCategory, session)

    def get_all(self):
        query = (
            select(self.model.id,
                   self.model.title).select_from(self.model)
        )
        return self.session.execute(query).all()