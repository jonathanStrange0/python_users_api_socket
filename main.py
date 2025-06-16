from fastapi import FastAPI, HTTPException
from schemas import UserCreate, User
import models

app = FastAPI()

@app.post("/users", response_model=User)
def create_user(user: UserCreate):
    return models.create_user(user)

@app.get("/users", response_model=list[User])
def list_users():
    return models.get_all_users()

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    user = models.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, user: UserCreate):
    updated = models.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    if not models.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
