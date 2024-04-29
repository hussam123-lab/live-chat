from app.client.mongo_client import MongoDbClient
from app.services.user_service import UserService


mongo_client = MongoDbClient()
user_service = UserService(db=mongo_client)

async def get_user_service() -> UserService:
    return user_service