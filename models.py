from typing import Dict
from uuid import uuid4
from schemas import UserCreate, User

# Simple in-memory "database"
fake_user_db: Dict[str, User] = {}

def create_user(user_data: UserCreate) -> User:
    """
    Create a new user with a unique ID. The user data is provided as a UserCreate schema.
    Returns the created User object.
    """

    user_id = str(uuid4())
    user = User(id=user_id, **user_data.dict())
    fake_user_db[user_id] = user
    return user

def get_user(user_id: str) -> User or None:
    """
    Retrieve a user by ID. If the user exists, it returns the User object.
    If the user does not exist, it returns None.
    """
    return fake_user_db.get(user_id)

def get_all_users() -> list[User]:
    """
    Retrieve all users. Returns a list of User objects."""
    return list(fake_user_db.values())

def update_user(user_id: str, user_data: UserCreate) -> User or None:
    """
    Update a user by ID. If the user exists, it updates the user's data
    and returns the updated user. If the user does not exist, it returns None.
    """
    if user_id in fake_user_db:
        updated_user = User(id=user_id, **user_data.dict())
        fake_user_db[user_id] = updated_user
        return updated_user
    return None

def delete_user(user_id: str) -> bool:
    """
    Delete a user by ID. If the user exists, it removes the user from the database
    and returns True. If the user does not exist, it returns False.
    """
    return fake_user_db.pop(user_id, None) is not None
