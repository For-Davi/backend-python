from app.application.repositories.user_repository import UserRepository
from app.application.security.password_hasher import PasswordHasher
from app.domain.exceptions import InvalidCredentialsError
from app.domain.user import User


class AuthenticateUser:
    def __init__(
        self,
        repository: UserRepository,
        password_hasher: PasswordHasher,
    ) -> None:
        self.repository = repository
        self.password_hasher = password_hasher

    def execute(self, email: str, password: str) -> User:
        user = self.repository.find_by_email(User.normalize_email(email))

        if user is None or not self.password_hasher.verify(
            password, user.password_hash
        ):
            raise InvalidCredentialsError()

        return user
