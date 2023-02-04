from fastapi import FastAPI, Depends, HTTPException
from login import add_user, login, correct_token

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/register/")
async def register(user_name: str, password: str, email: str):
    return add_user(user_name, password, email)


@app.get("/login/{user_name: str}")
async def login(password: str):
    pass
