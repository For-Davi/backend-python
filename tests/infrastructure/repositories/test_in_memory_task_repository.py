from app.domain.task import Task
from app.infrastructure.repositories.in_memory_task_repository import (
    InMemoryTaskRepository,
)


def test_save_task():
    repository = InMemoryTaskRepository()
    task = Task(id=1, title="Estudar Python")

    saved_task = repository.save(task)

    assert saved_task is task
    assert repository.tasks[1] is task