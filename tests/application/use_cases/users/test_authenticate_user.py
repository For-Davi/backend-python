import pytest

from app.application.use_cases.users.authenticate_user import AuthenticateUser
from app.domain.exceptions import InvalidCredentialsError
from app.domain.user import User
from app.infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from tests.fakes.fake_password_hasher import FakePasswordHasher


def make_authenticate_user() -> AuthenticateUser:
    password_hasher = FakePasswordHasher()
    repository = InMemoryUserRepository()
    repository.save(
        User(
            id=1,
            name="Carlos",
            email="carlos@email.com",
            password_hash=password_hasher.hash("secret123"),
        )
    )
    return AuthenticateUser(repository, password_hasher)


def test_authenticate_user():
    authenticate_user = make_authenticate_user()

    user = authenticate_user.execute(email="carlos@email.com", password="secret123")

    assert user.id == 1
    assert user.email == "carlos@email.com"


def test_authenticate_user_normalizes_email():
    authenticate_user = make_authenticate_user()

    user = authenticate_user.execute(email="  CARLOS@Email.com ", password="secret123")

    assert user.id == 1


def test_authenticate_user_raises_when_email_does_not_exist():
    authenticate_user = make_authenticate_user()

    with pytest.raises(InvalidCredentialsError):
        authenticate_user.execute(email="outro@email.com", password="secret123")


def test_authenticate_user_raises_when_password_is_wrong():
    authenticate_user = make_authenticate_user()

    with pytest.raises(InvalidCredentialsError):
        authenticate_user.execute(email="carlos@email.com", password="wrong-password")


def test_authenticate_user_does_not_reveal_which_credential_is_wrong():
    authenticate_user = make_authenticate_user()

    with pytest.raises(InvalidCredentialsError) as unknown_email:
        authenticate_user.execute(email="outro@email.com", password="secret123")

    with pytest.raises(InvalidCredentialsError) as wrong_password:
        authenticate_user.execute(email="carlos@email.com", password="wrong-password")

    assert str(unknown_email.value) == str(wrong_password.value)
