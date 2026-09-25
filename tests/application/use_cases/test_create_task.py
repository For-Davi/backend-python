import pytest

from app.application.use_cases.create_task import CreateTask
from app.domain.task import Task
from app.infrastructure.repositories.in_memory_task_repository import (
    InMemoryTaskRepository,
)


def test_create_task():
    repository = InMemoryTaskRepository()
    create_task = CreateTask(repository)

    task = create_task.execute(
        task_id=1,
        title="Estudar Clean Architecture",
    )

    assert isinstance(task, Task)
    assert task.id == 1
    assert task.title == "Estudar Clean Architecture"
    assert task.description is None
    assert task.completed is False
    assert repository.tasks[1] is task


def test_create_task_cannot_have_empty_title():
    repository = InMemoryTaskRepository()
    create_task = CreateTask(repository)

    with pytest.raises(ValueError):
        create_task.execute(
            task_id=1,
            title="   ",
        )