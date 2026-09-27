from app.application.repositories.task_repository import TaskRepository
from app.domain.exceptions import TaskNotFoundError
from app.domain.task import Task


class UpdateTask:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def execute(
        self,
        task_id: int,
        title: str,
        description: str | None = None,
    ) -> Task:
        task = self.repository.find_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        task.update(title=title, description=description)

        return self.repository.save(task)
