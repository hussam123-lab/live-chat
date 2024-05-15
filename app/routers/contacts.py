import datetime
from typing import List
from app.dependencies import get_user_service
from app.domain.users.contacts_request import ContactsRequest
from app.domain.users.user import User
from app.domain.users.user_request import UserRequest
from app.exceptions.user_service_exceptions import UserNotFoundException
from app.services.user_service import UserService
from fastapi import APIRouter, Depends
from uuid import UUID, uuid4
from pydantic import ValidationError
router = APIRouter(tags=["users"])

@router.post("/users")
async def create_user(user_request: UserRequest, user_service: UserService = Depends(get_user_service)) -> User:
    try:
        user = User(**user_request.dict(),user_id=uuid4(),contacts = [])
        return await user_service.add_user_to_db(user=user)
    
    except ValidationError as err:
        print("Validation error:", err)

@router.get("/users")
async def get_users(user_service: UserService = Depends(get_user_service)) -> List[User]:
    try:
        return await user_service.get_users()
    
    except ValidationError as err:
        print("Validation error:", err)

@router.post("/users/{user_id}/add_contact")
async def add_contact_by_phone_number(user_id: UUID, contacts_request: ContactsRequest, user_service: UserService = Depends(get_user_service)) -> None:
    try:
        user = await user_service.get_user_by_id(user_id)
        contact = await user_service.get_user_by_number(contacts_request.phone_number)
        await user_service.add_contact_to_user(user=user,contact=contact.user_id)
        
    except UserNotFoundException as e:
        raise e
    except ValidationError as err:
        print("Validation error:", err)