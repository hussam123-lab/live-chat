from copy import deepcopy
from typing import List
from uuid import UUID
from app.client.mongo_client import MongoDbClient
from app.domain.users.user import User
from pydantic import BaseModel, PrivateAttr

from app.exceptions.user_service_exceptions import UserNotFoundException

class UserService(BaseModel):

    _db:MongoDbClient  = PrivateAttr()
    _collection_name:str  = PrivateAttr()

    def __init__(self, db: MongoDbClient) -> None:
        self._db = db
        self._collection_name = "users"

    async def add_user_to_db(self, user: User) -> User:
        return await self._db.insert_one(collection=self._collection_name, document=user)
    
    async def get_users(self) -> List[User]:
        documents = await self._db.find(collection=self._collection_name)
        return [User(**doc) for doc in documents]

    async def get_user_by_id(self, user_id: UUID) -> User:
        user_dict = await self._db.find_one(self._collection_name,{'user_id': user_id})
        user = User(**user_dict)
        return user
    
    async def get_user_by_number(self, phone_number: str) -> User:
        user_dict = await self._db.find_one(self._collection_name,{'phone_number': phone_number})
        if not user_dict:
            raise UserNotFoundException("User doesnt exist")
        user = User(**user_dict)
        return user
        
    async def add_contact_to_user(self, user: User, contact: UUID ) -> None:
        user_copy = deepcopy(user)
        contacts = [contact]
        user.contacts = contacts
        print(user_copy)
        print(user)
        await self._db.update_one(collection=self._collection_name,query=user_copy,update=user)