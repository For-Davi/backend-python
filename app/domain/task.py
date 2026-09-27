from dataclasses import dataclass

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
        self.completed = True

    def reopen(self) -> None:
        self.completed = False

    @staticmethod
    def _validate_title(title: str) -> None:
        if not title.strip():
            raise ValueError("Task title cannot be empty")
