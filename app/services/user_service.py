from app.client.mongo_client import MongoDbClient
from app.domain.users.user import User
from pydantic import BaseModel, PrivateAttr
class UserService(BaseModel):

    _db:MongoDbClient  = PrivateAttr()
    _collection_name:str  = PrivateAttr()

    def __init__(self, db: MongoDbClient) -> None:
        self._db = db
        self._collection_name = "users"

    async def add_user_to_db(self, user: User) -> None:
        self._db.insert_one(collection=self._collection_name, document=user)