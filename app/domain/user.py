from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str
    password_hash: str

    def __post_init__(self) -> None:
        self.email = self.email.strip().lower()

        if not self.name.strip():
            raise ValueError("User name cannot be empty")

        if "@" not in self.email:
            raise ValueError("User email is invalid")

        if not self.password_hash:
            raise ValueError("User password hash cannot be empty")
