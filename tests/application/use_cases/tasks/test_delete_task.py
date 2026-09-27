import pytest

from app.application.use_cases.tasks.delete_task import DeleteTask
from app.domain.exceptions import TaskNotFoundError
from app.domain.task import Task
from app.infrastructure.repositories.in_memory_task_repository import (
    InMemoryTaskRepository,
)


def test_delete_task():
    repository = InMemoryTaskRepository()
    repository.save(Task(id=1, title="Estudar Python"))
    delete_task = DeleteTask(repository)

    delete_task.execute(task_id=1)

    assert repository.find_by_id(1) is None


def test_delete_task_raises_when_task_does_not_exist():
    repository = InMemoryTaskRepository()
    delete_task = DeleteTask(repository)

    with pytest.raises(TaskNotFoundError):
        delete_task.execute(task_id=999)


def test_delete_task_keeps_other_tasks():
    repository = InMemoryTaskRepository()
    repository.save(Task(id=1, title="Estudar Python"))
    repository.save(Task(id=2, title="Estudar FastAPI"))
    delete_task = DeleteTask(repository)

    delete_task.execute(task_id=1)

    assert repository.find_by_id(2) is not None
