from app.domain.task import Task
from app.infrastructure.repositories.in_memory_task_repository import (
    InMemoryTaskRepository,
)

def test_save_task():
    repository = InMemoryTaskRepository()
    task = Task(id=1, title="Estudar Python")

    saved_task = repository.save(task)

    assert saved_task is task
    assert repository.find_by_id(1) is task


def test_save_overwrites_existing_task():
    repository = InMemoryTaskRepository()
    repository.save(Task(id=1, title="Estudar Python"))
    updated_task = Task(id=1, title="Estudar FastAPI")

    repository.save(updated_task)

    assert repository.find_by_id(1) is updated_task


def test_find_by_id_returns_task():
    repository = InMemoryTaskRepository()
    task = Task(id=1, title="Estudar Python")
    repository.save(task)

    found_task = repository.find_by_id(1)

    assert found_task is task


def test_find_by_id_returns_none_when_task_does_not_exist():
    repository = InMemoryTaskRepository()

    found_task = repository.find_by_id(999)

    assert found_task is None


def test_find_all_returns_all_tasks():
    repository = InMemoryTaskRepository()
    task_1 = Task(id=1, title="Estudar Python")
    task_2 = Task(id=2, title="Estudar FastAPI")
    repository.save(task_1)
    repository.save(task_2)

    tasks = repository.find_all()

    assert tasks == [task_1, task_2]


def test_find_all_returns_empty_list_when_there_are_no_tasks():
    repository = InMemoryTaskRepository()

    tasks = repository.find_all()

    assert tasks == []


def test_delete_removes_task():
    repository = InMemoryTaskRepository()
    repository.save(Task(id=1, title="Estudar Python"))

    repository.delete(1)

    assert repository.find_by_id(1) is None


def test_delete_does_nothing_when_task_does_not_exist():
    repository = InMemoryTaskRepository()

    repository.delete(999)

    assert repository.find_all() == []
