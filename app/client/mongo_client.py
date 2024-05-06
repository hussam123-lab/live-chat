from typing import Dict, List, Optional
from pydantic import BaseModel, PrivateAttr
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder

from app.domain.users.user import User

class MongoDbClient(BaseModel):
    _instance = None
    _is_initialized = False
    _database_name: str = PrivateAttr()
    _client: MongoClient = PrivateAttr()
    _db = PrivateAttr()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDbClient, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._database_name = "live_chat"
            self._client = MongoClient("mongodb://localhost:27017/")
            self._db = self._client[self._database_name]
            self.__class__._is_initialized = True
    
    async def insert_one(self, collection: str, document: dict) -> User:
        # Insert document into the specified MongoDB collection
        json_dict =  jsonable_encoder(document)
        self._db[collection].insert_one(json_dict)
        user = User(**json_dict)
        return user
    
    async def find_one(self, collection: str, query: Dict) -> Optional[Dict]:
        json_dict =  jsonable_encoder(query)
        result = self._db[collection].find_one(json_dict)
        return result
    
    async def find(self, collection: str) -> Optional[List[Dict]]:
        result = self._db[collection].find()
        return result
    
    async def update_one(self,collection: str, query: Dict, update: Dict) -> None:
        json_query = jsonable_encoder(query)
        json_update = jsonable_encoder(update)
        self._db[collection].update_one(json_query, {'$set': json_update})