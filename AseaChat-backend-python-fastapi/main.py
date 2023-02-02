from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from login import models
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/register")
async def register(username: str, password: str, db: Session = Depends(get_db)):
    db_user = models.User(username=username, password=password)
    db.add(db_user)
    db.commit()
    return db_user




