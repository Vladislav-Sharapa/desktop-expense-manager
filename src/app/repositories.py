from typing import TypeVar, Generic
from sqlalchemy.orm import Session
from .models import *

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
        instanse = self.get_by_id(id)
        if instanse: 
            self.session.delete(instanse)
            return True
        return False
    
    def get_by_id(self, id: int) -> Model:
        instance = self.session.query(self.model).filter(self.model.id == id).first()
        return instance
    

class ExpenseRepository(BaseRepository[Expense]):
    """Repository to interect with `expanses` table in database"""
    def __init__(self, session: Session) -> None:
        super().__init__(Expense, session)


class ExpenseCategoryRepository(BaseRepository[ExpenseCategory]):
    """Repository to interect with `expanses category` table in database"""
    def __init__(self, session: Session) -> None:
        super().__init__(ExpenseCategory, session)