from pydantic import BaseModel, PrivateAttr
from app.domain.users.user import User
from app.exceptions.user_service_exceptions import UnauthorisedUserException

from app.services.user_service import UserService
class ValidationService(BaseModel):
    
    _user_service: UserService = PrivateAttr()

    def __init__(self, user_service: UserService):
        self._user_service = user_service
    
    def validate_user(self, user: User, username: str, password: str) -> User:
        found = user.password == password and user.name == username
        if not found:
            raise UnauthorisedUserException(detail="User not authorised")
        return user