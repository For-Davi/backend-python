from typing import Protocol

from app.domain.task import Task


class TaskRepository(Protocol):
    def save(self, task: Task) -> Task:
        ...
    
    def find_by_id(self, task_id: int) -> Task | None:
        ...

    def find_all(self) -> list[Task]:
        ...

    def delete(self, task_id: int) -> None:
        ...