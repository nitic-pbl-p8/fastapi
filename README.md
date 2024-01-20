# API description

## 1.エンドポイント

```pythoon

class Request(BaseModel):
    similarity : float
    date_difference : float

```


```https://fast-api-production.up.railway.app/path/```


- similarity : コサイン類似度・float

- date_difference : 日付のズレをmsにしたもの
  

```python
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

```
## 2.戻り値

```python
class Response(BaseModel):
    data: [float, float]
    error: Optional[str] = None
```

{"res":[rate_true,rate_false]}

- rate_true : その人の落とし物である確率
- rate_false : その人の落とし物でない確率


---

# FastAPI Example

This example starts up a [FastAPI](https://fastapi.tiangolo.com/) server.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/-NvLj4?referralCode=milo)
## ✨ Features

- FastAPI
- Python 3

## 💁‍♀️ How to use

- Deploy using the button 👆
- Clone locally and install packages with Pip using `pip install -r requirements.txt` or Poetry using `poetry install`
- Connect to your project using `railway link`
- Run locally using `uvicorn main:app --reload`

## 📝 Notes

- To learn about how to use FastAPI with most of its features, you can visit the [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/).
- FastAPI provides automatic documentation to call and test your API directly from the browser. You can access it at `/docs` with [Swagger](https://github.com/swagger-api/swagger-ui) or at `/redoc` with [Redoc](https://github.com/Rebilly/ReDoc).
