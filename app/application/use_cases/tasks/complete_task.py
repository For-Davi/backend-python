from app.application.repositories.task_repository import TaskRepository
from app.domain.exceptions import TaskNotFoundError
from app.domain.task import Task


class CompleteTask:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def execute(self, task_id: int) -> Task:
        task = self.repository.find_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        task.complete()

        return self.repository.save(task)
