from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    description: str | None = None
    completed: bool = False

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("Task title cannot be empty")

    def complete(self) -> None:
        self.completed = True

    def reopen(self) -> None:
        self.completed = False