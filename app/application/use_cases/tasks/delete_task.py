from app.application.repositories.task_repository import TaskRepository
from app.domain.exceptions import TaskNotFoundError


class DeleteTask:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def execute(self, task_id: int) -> None:
        task = self.repository.find_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self.repository.delete(task_id)
