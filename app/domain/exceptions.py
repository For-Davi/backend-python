class DomainError(Exception):
    """Base para erros de regra de negócio."""


class TaskNotFoundError(DomainError):
    def __init__(self, task_id: int) -> None:
        self.task_id = task_id
        super().__init__(f"Task {task_id} not found")



class TaskAlreadyCompletedError(DomainError):
    def __init__(self, task_id: int) -> None:
        self.task_id = task_id
        super().__init__(f"Task {task_id} is already completed")

