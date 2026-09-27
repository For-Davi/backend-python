from app.application.repositories.user_repository import UserRepository
from app.application.security.password_hasher import PasswordHasher
from app.domain.exceptions import UserAlreadyExistsError
from app.domain.user import User


class CreateUser:
    def __init__(
        self,
        repository: UserRepository,
        password_hasher: PasswordHasher,
    ) -> None:
        self.repository = repository
        self.password_hasher = password_hasher

    def execute(
        self,
        user_id: int,
        name: str,
        email: str,
        password: str,
    ) -> User:
        normalized_email = User.normalize_email(email)

        if self.repository.find_by_email(normalized_email) is not None:
            raise UserAlreadyExistsError(normalized_email)

        user = User(
            id=user_id,
            name=name,
            email=normalized_email,
            password_hash=self.password_hasher.hash(password),
        )

        return self.repository.save(user)
