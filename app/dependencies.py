from app.client.mongo_client import MongoDbClient
from app.services.user_service import UserService
from app.services.validation_service import ValidationService


mongo_client = MongoDbClient()

user_service = UserService(db=mongo_client)

validation_service = ValidationService(user_service=user_service)

async def get_user_service() -> UserService:
    return user_service

async def get_validation_service() -> ValidationService:
    return validation_service