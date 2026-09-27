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

def test_task_can_be_updated():
    task = Task(id=1, title="Estudar Python")

    task.update(title="Estudar FastAPI", description="Rotas e dependências")

    assert task.title == "Estudar FastAPI"
    assert task.description == "Rotas e dependências"


def test_task_update_cannot_set_empty_title():
    task = Task(id=1, title="Estudar Python")

    with pytest.raises(ValueError):
        task.update(title="   ")

    assert task.title == "Estudar Python"
