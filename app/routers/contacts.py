import datetime
from app.dependencies import get_user_service
from app.domain.users.user import User
from app.domain.users.user_request import UserRequest
from app.services.user_service import UserService
from fastapi import APIRouter, Depends
from uuid import uuid4
from pydantic import ValidationError
router = APIRouter(tags=["users"])

@router.post("/users")
async def create_user(user_request: UserRequest, user_service: UserService = Depends(get_user_service)) -> None:
    try:
        user = User(**user_request.dict(),user_id=uuid4(),contacts = [])
        await user_service.add_user_to_db(user=user)
    
    except ValidationError as err:
        print("Validation error:", err)