from fastapi import FastAPI
from time import sleep
import requests
import json

app = FastAPI()


@app.get("/")
async def root():
    url1 = f"http://127.0.0.1:5001"
    url2 = f"http://127.0.0.1:5003"
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    print(json.loads(response1.text))
    print(json.loads(response2.text))
    return "Request Success"
