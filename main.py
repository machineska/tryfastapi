from fastapi import FastAPI

app = FastAPI(
    title="Try FastAPI",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="0.0.1",
)


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}


@app.get('/users/me')
async def read_user_me():
    return {'user_id': 'the current user'}


@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}
