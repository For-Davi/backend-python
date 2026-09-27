from app.domain.user import User


class InMemoryUserRepository:
    def __init__(self) -> None:
        self.users: dict[int, User] = {}

    def save(self, user: User) -> User:
        self.users[user.id] = user
        return user

    def find_by_id(self, user_id: int) -> User | None:
        return self.users.get(user_id)

    def find_by_email(self, email: str) -> User | None:
        for user in self.users.values():
            if user.email == email:
                return user

        return None
