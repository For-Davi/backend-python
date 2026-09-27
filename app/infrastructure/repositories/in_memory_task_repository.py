from app.domain.task import Task


class InMemoryTaskRepository:
    def __init__(self) -> None:
        self.tasks: dict[int, Task] = {}

    def save(self, task: Task) -> Task:
        self.tasks[task.id] = task
        return task

    def find_by_id(self, task_id: int) -> Task | None:
        return self.tasks.get(task_id)

    def find_all(self) -> list[Task]:
        return list(self.tasks.values())

    def delete(self, task_id: int) -> None:
        self.tasks.pop(task_id, None)
