import pytest

from app.domain.task import Task


def test_task_cannot_have_empty_title():
    with pytest.raises(ValueError):
        Task(id=1, title="")


def test_task_can_be_completed():
    task = Task(id=1, title="Estudar Python")

    task.complete()

    assert task.completed is True


def test_task_can_be_reopened():
    task = Task(id=1, title="Estudar Python")

    task.complete()
    task.reopen()

    assert task.completed is False