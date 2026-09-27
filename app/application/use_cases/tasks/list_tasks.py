from app.application.repositories.task_repository import TaskRepository
from app.domain.task import Task


class ListTasks:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def execute(self) -> list[Task]:
        return self.repository.find_all()
