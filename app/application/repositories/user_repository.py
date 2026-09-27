from typing import Protocol

from app.domain.user import User


class UserRepository(Protocol):
    def save(self, user: User) -> User:
        ...

    def find_by_id(self, user_id: int) -> User | None:
        ...

    def find_by_email(self, email: str) -> User | None:
        ...
