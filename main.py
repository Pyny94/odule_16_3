from fastapi import FastAPI,Path
from typing import Annotated



app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/user")
async def main() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def info(username: str,age:int) -> str:
    new_id = str(max(int(key) for key in users.keys())+1) if users else 0
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def user_put(user_id: str, username: str, age: int):
    if user_id in users:
        users[user_id] = f"Имя: {username},возраст: {age}"
    return f"The user {user_id} is registered"

@app.delete("/user/{user_id}")
async def user_delete(user_id: str):
    if user_id in users:
        del users[user_id]
    return f"The user {user_id} is delete"