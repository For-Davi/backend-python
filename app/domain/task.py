from dataclasses import dataclass
from app.domain.exceptions import TaskAlreadyCompletedError

@dataclass
class Task:
    id: int
    title: str
    description: str | None = None
    completed: bool = False

    def __post_init__(self) -> None:
        self._validate_title(self.title)

    def update(self, title: str, description: str | None = None) -> None:
        self._validate_title(title)
        self.title = title
        self.description = description

    def complete(self) -> None:
        if self.completed:
            raise TaskAlreadyCompletedError(self.id)

        self.completed = True


    def reopen(self) -> None:
        self.completed = False

    @staticmethod
    def _validate_title(title: str) -> None:
        if not title.strip():
            raise ValueError("Task title cannot be empty")
