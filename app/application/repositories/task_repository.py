from typing import Protocol

from app.domain.task import Task


class TaskRepository(Protocol):
    def save(self, task: Task) -> Task:
        ...