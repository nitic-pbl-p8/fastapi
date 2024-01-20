from fastapi import FastAPI
from pydantic import BaseModel
from keras.models import load_model
import numpy as np
from pydantic import BaseModel
from typing import Optional, List



class Request(BaseModel):
    similarity : float
    date_difference : float


class Response(BaseModel):
    data: List[float]
    error: Optional[str] = None


mean = 117.5364705882353
std = 52.3410265358211

model = load_model('trained_data')
model.summary()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.post("/predict/", response_model=Response)
async def demo_get_path_id(req_body: Request):
    try:
        ch_sec = req_body.date_id / 1000 / 1000
        date_std = (ch_sec - mean)/std
        new_data = np.array([[req_body.cos_id, date_std]])
        if ch_sec >= 400:
            return Response(data=[0, 1])
        else:
            return Response(data=[model.predict(new_data)[0],model.predict(new_data)[1]])

    except Exception as e:
        return Response(data=[-1, 1], error=str(e))
