from app.dependencies import get_validation_service, get_user_service
from app.domain.users.user import User
from app.domain.users.validate_request import ValidateRequest
from app.exceptions.user_service_exceptions import UnauthorisedUserException, UserNotFoundException
from app.services.user_service import UserService
from app.services.validation_service import ValidationService
from fastapi import APIRouter, Depends
from pydantic import ValidationError
router = APIRouter(tags=["authorize"])

@router.post("/validate-user")
async def create_user(validate_request: ValidateRequest, user_service: UserService = Depends(get_user_service), validation_service: ValidationService = Depends(get_validation_service)) -> User:
    try:
        user = await user_service.get_user_by_number(validate_request.phone_number)
        return validation_service.validate_user(user=user,username=user.name,password=validate_request.password)
    
    except UserNotFoundException as e:
        raise e
    except UnauthorisedUserException as e:
        raise e
    except ValidationError as err:
        print("Validation error:", err)

