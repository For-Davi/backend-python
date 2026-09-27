import pytest

from app.application.use_cases.users.create_user import CreateUser
from app.domain.exceptions import UserAlreadyExistsError
from app.domain.user import User
from app.infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from tests.fakes.fake_password_hasher import FakePasswordHasher


def test_create_user():
    repository = InMemoryUserRepository()
    create_user = CreateUser(repository, FakePasswordHasher())

    user = create_user.execute(
        user_id=1,
        name="Carlos",
        email="carlos@email.com",
        password="secret123",
    )

    assert user.id == 1
    assert user.name == "Carlos"
    assert user.email == "carlos@email.com"
    assert repository.find_by_id(1) is user


def test_create_user_stores_password_hash_instead_of_plain_password():
    repository = InMemoryUserRepository()
    create_user = CreateUser(repository, FakePasswordHasher())

    user = create_user.execute(
        user_id=1,
        name="Carlos",
        email="carlos@email.com",
        password="secret123",
    )

    assert user.password_hash == "hashed:secret123"
    assert user.password_hash != "secret123"


def test_create_user_raises_when_email_already_exists():
    repository = InMemoryUserRepository()
    existing_user = User(
        id=1,
        name="Carlos",
        email="carlos@email.com",
        password_hash="hashed:secret123",
    )
    repository.save(existing_user)
    create_user = CreateUser(repository, FakePasswordHasher())

    with pytest.raises(UserAlreadyExistsError):
        create_user.execute(
            user_id=2,
            name="Outro Carlos",
            email="  CARLOS@Email.com ",
            password="another123",
        )

    assert repository.find_by_id(2) is None
