from fastapi import FastAPI
from app.routers import contacts, validate
app = FastAPI()

app.include_router(contacts.router)
app.include_router(validate.router)