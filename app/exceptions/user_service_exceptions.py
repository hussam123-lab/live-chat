from fastapi import HTTPException, status
class UserNotFoundException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class UnauthorisedUserException(HTTPException):
    def __init__(self,detail: str):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED,detail=detail)