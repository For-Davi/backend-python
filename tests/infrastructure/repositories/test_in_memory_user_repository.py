from app.domain.user import User
from app.infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)


def make_user(user_id: int = 1, email: str = "carlos@email.com") -> User:
    return User(
        id=user_id,
        name="Carlos",
        email=email,
        password_hash="hashed-password",
    )


def test_save_user():
    repository = InMemoryUserRepository()
    user = make_user()

    saved_user = repository.save(user)

    assert saved_user is user
    assert repository.find_by_id(1) is user


def test_find_by_id_returns_none_when_user_does_not_exist():
    repository = InMemoryUserRepository()

    assert repository.find_by_id(999) is None


def test_find_by_email_returns_user():
    repository = InMemoryUserRepository()
    user = make_user(email="carlos@email.com")
    repository.save(user)

    found_user = repository.find_by_email("carlos@email.com")

    assert found_user is user


def test_find_by_email_returns_none_when_user_does_not_exist():
    repository = InMemoryUserRepository()
    repository.save(make_user(email="carlos@email.com"))

    assert repository.find_by_email("outro@email.com") is None
