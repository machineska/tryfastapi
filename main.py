from enum import Enum

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
