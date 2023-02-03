from typing import List

from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
