from fastapi import FastAPI, File, UploadFile, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickledb
import nanoid
import pathlib
import time
import requests
from typing import Optional


class GenerateImageRequestBody(BaseModel):
    image_style: int = 0
    user_prompt: str = ''


db = pickledb.load('./generated_image_list.db', False)
app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.post('/generate-image')
def generate_image(body: GenerateImageRequestBody):
    generated_image_id = nanoid.generate()

    db.set(generated_image_id, {
        'image_style': body.image_style,
        'user_prompt': body.user_prompt
    })

    db.dump()

    return {
        'message': 'SUCCESS',
        'generated_image_id': generated_image_id
    }


@app.post('/generate-image/upload-image/{generated_image_id}')
def receive_image_form(generated_image_id: str, image: Optional[UploadFile] = File(None)):
    if image is None:
        return {
            'message': 'SUCCESS',
            'filename': '',
            'image_id': ''
        }

    file_location = f'./user_defined_images/{generated_image_id}'

    # * create a directory for the file, using the generate id as the directory name
    pathlib.Path(file_location).mkdir(exist_ok=True, parents=True)

    # suffix returns the file extension with the dot
    file_location += f'/{nanoid.generate()}{pathlib.Path(image.filename).suffix}'

    # * saving the file to the given directory
    with open(file_location, 'wb+') as file_object:
        file_object.write(image.file.read())

    return {
        'message': 'SUCCESS',
        'filename': image.filename,
        'image_id': generated_image_id
    }


@app.get('/generate-image/{generated_image_id}/ws')
async def get_generated_image_id(websocket: WebSocket):
    await websocket.accept()

    while True:
        await websocket.send_text('who')
        time.sleep(5)
