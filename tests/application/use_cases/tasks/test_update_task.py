import pytest

from app.application.use_cases.tasks.update_task import UpdateTask
from app.domain.exceptions import TaskNotFoundError
from app.domain.task import Task
from app.infrastructure.repositories.in_memory_task_repository import (
    InMemoryTaskRepository,
)


def test_update_task():
    repository = InMemoryTaskRepository()
    repository.save(Task(id=1, title="Estudar Python"))
    update_task = UpdateTask(repository)

    task = update_task.execute(
        task_id=1,
        title="Estudar FastAPI",
        description="Rotas e dependências",
    )

    assert task.id == 1
    assert task.title == "Estudar FastAPI"
    assert task.description == "Rotas e dependências"
    assert repository.find_by_id(1) is task


def test_update_task_raises_when_task_does_not_exist():
    repository = InMemoryTaskRepository()
    update_task = UpdateTask(repository)

    with pytest.raises(TaskNotFoundError):
        update_task.execute(task_id=999, title="Qualquer coisa")


def test_update_task_cannot_set_empty_title():
    repository = InMemoryTaskRepository()
    repository.save(Task(id=1, title="Estudar Python"))
    update_task = UpdateTask(repository)

    with pytest.raises(ValueError):
        update_task.execute(task_id=1, title="   ")

    assert repository.find_by_id(1).title == "Estudar Python"
