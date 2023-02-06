import uvicorn
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/register/")
async def register(username: str, password: str):
    print(f'get username: {username} and password: {password}' )
    return {'token': 'a_token',
            'username': username,
            'password': password, }


@app.get("/login/{user_name: str}")
async def login(password: str):
    pass


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info')
# uvicorn main:app --host '0.0.0.0' --port 8000 --reload