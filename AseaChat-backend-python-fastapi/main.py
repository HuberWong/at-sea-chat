from fastapi import FastAPI, Depends, HTTPException
from login import add_user, login, correct_token

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
