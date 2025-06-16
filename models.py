from typing import Dict
from uuid import uuid4
from schemas import UserCreate, User

# Simple in-memory "database"
fake_user_db: Dict[str, User] = {}

def create_user(user_data: UserCreate) -> User:
    user_id = str(uuid4())
    user = User(id=user_id, **user_data.dict())
    fake_user_db[user_id] = user
    return user

def get_user(user_id: str) -> User or None:
    return fake_user_db.get(user_id)

def get_all_users() -> list[User]:
    return list(fake_user_db.values())

def update_user(user_id: str, user_data: UserCreate) -> User or None:
    if user_id in fake_user_db:
        updated_user = User(id=user_id, **user_data.dict())
        fake_user_db[user_id] = updated_user
        return updated_user
    return None

def delete_user(user_id: str) -> bool:
    return fake_user_db.pop(user_id, None) is not None
