from database.session import session_scope
from typing import Generic, List, TypeVar
from .repositories import BaseRepository, ExpenseRepository, ExpenseCategoryRepository
from sqlalchemy.orm import Session

R = TypeVar("R", bound=BaseRepository)


class BaseService(Generic[R]):
    def __init__(self, repository: type[R]) -> None:
        self.repository = repository
    
    @session_scope(commit_required=True)
    def add(self, session: Session, data: dict):
        repository = self.repository(session)
        repository.create(data)

    @session_scope(commit_required=True)
    def delete(self, session: Session, id: int):
        repository = self.repository(session)
        repository.delete(id)

    @session_scope(commit_required=True)
    def update(self, session: Session, id: int, data: dict):
        repository = self.repository(session)
        repository.update(id, data)

    @session_scope(commit_required=False)
    def get_all(self, session: Session):
        repository = self.repository(session)
        return repository.get_all()


class ExpenseService(BaseService[ExpenseRepository]):
    def __init__(self) -> None:
        super().__init__(ExpenseRepository)

    @session_scope(commit_required=False)
    def get_total(self, session: Session):
        repository = self.repository(session)
        return repository.get_total()
    

class ExpenseCategoryService(BaseService[ExpenseCategoryRepository]):
    def __init__(self) -> None:
        super().__init__(ExpenseCategoryRepository)
