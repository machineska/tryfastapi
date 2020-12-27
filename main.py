from enum import Enum
from typing import Optional

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


app = FastAPI(
    title="Try FastAPI",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="0.0.1",
)

fake_items_db = [
    {'item_name': 'Foo'}, {'item_name': 'Bar'}, {'item_name': 'Baz'}
]


@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get('/items/{item_id}')
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

@app.get('/')
async def root():
    return {'message': 'Hello World'}



@app.get('/users/me')
async def read_user_me():
    return {'user_id': 'the current user'}


@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}

    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'leCNN all the images'}

    return {'model_name': model_name, 'message': 'Have some residuals'}


@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}
