from app.application.repositories.task_repository import TaskRepository
from app.domain.task import Task


class CreateTask:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def execute(
        self,
        task_id: int,
        title: str,
        description: str | None = None,
    ) -> Task:
        task = Task(
            id=task_id,
            title=title,
            description=description,
        )

        return self.repository.save(task)