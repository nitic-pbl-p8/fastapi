from fastapi import FastAPI
from pydantic import BaseModel
from keras.models import load_model
import numpy as np

mean = 117.5364705882353
std = 52.3410265358211

model = load_model('trained_data')
model.summary()

app = FastAPI()

new_data = np.array([[0.9, 0.3], [0.4, 0.5]])
predictions = model.predict(new_data)

print(predictions)


class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{cos_id}/{date_id}/")
async def demo_get_path_id(cos_id: float, date_id: int):
    date_std = (date_id - mean)/std
    new_data = np.array([[cos_id, date_std]])
    if date_id >= 400:
        return {"res": [0, 1]}
    else:
        return {"res": model.predict(new_data).tolist()[0]}
