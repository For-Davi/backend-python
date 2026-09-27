import pytest

from app.application.use_cases.tasks.complete_task import CompleteTask
from app.domain.exceptions import TaskAlreadyCompletedError, TaskNotFoundError
from app.domain.task import Task
from app.infrastructure.repositories.in_memory_task_repository import (
    InMemoryTaskRepository,
)


def test_complete_task():
    repository = InMemoryTaskRepository()
    repository.save(Task(id=1, title="Estudar Python"))
    complete_task = CompleteTask(repository)

    task = complete_task.execute(task_id=1)

    assert task.completed is True
    assert repository.find_by_id(1) is task


def test_complete_task_raises_when_task_does_not_exist():
    repository = InMemoryTaskRepository()
    complete_task = CompleteTask(repository)

    with pytest.raises(TaskNotFoundError):
        complete_task.execute(task_id=999)


def test_complete_task_raises_when_task_is_already_completed():
    repository = InMemoryTaskRepository()
    repository.save(Task(id=1, title="Estudar Python", completed=True))
    complete_task = CompleteTask(repository)

    with pytest.raises(TaskAlreadyCompletedError):
        complete_task.execute(task_id=1)
