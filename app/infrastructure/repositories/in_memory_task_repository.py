from app.domain.task import Task


class InMemoryTaskRepository:
    def __init__(self) -> None:
        self.tasks: dict[int, Task] = {}

    def save(self, task: Task) -> Task:
        self.tasks[task.id] = task
        return task