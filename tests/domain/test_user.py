import pytest

from app.domain.user import User


def test_create_user():
    user = User(
        id=1,
        name="Carlos",
        email="carlos@email.com",
        password_hash="hashed-password",
    )

    assert user.id == 1
    assert user.name == "Carlos"
    assert user.email == "carlos@email.com"
    assert user.password_hash == "hashed-password"


def test_user_email_is_normalized():
    user = User(
        id=1,
        name="Carlos",
        email="  Carlos@Email.COM  ",
        password_hash="hashed-password",
    )

    assert user.email == "carlos@email.com"


def test_user_cannot_have_empty_name():
    with pytest.raises(ValueError):
        User(id=1, name="   ", email="carlos@email.com", password_hash="hash")


def test_user_cannot_have_invalid_email():
    with pytest.raises(ValueError):
        User(id=1, name="Carlos", email="carlos.email.com", password_hash="hash")


def test_user_cannot_have_empty_password_hash():
    with pytest.raises(ValueError):
        User(id=1, name="Carlos", email="carlos@email.com", password_hash="")
