from app.application.use_cases.tasks.list_tasks import ListTasks
from app.domain.task import Task
from app.infrastructure.repositories.in_memory_task_repository import (
    InMemoryTaskRepository,
)


def test_list_tasks():
    repository = InMemoryTaskRepository()
    task_1 = Task(id=1, title="Estudar Python")
    task_2 = Task(id=2, title="Estudar FastAPI")
    repository.save(task_1)
    repository.save(task_2)
    list_tasks = ListTasks(repository)

    tasks = list_tasks.execute()

    assert tasks == [task_1, task_2]


def test_list_tasks_returns_empty_list_when_there_are_no_tasks():
    repository = InMemoryTaskRepository()
    list_tasks = ListTasks(repository)

    tasks = list_tasks.execute()

    assert tasks == []
