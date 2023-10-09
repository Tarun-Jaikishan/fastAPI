from fastapi import FastAPI
from time import sleep
import requests
import json

app = FastAPI()


@app.get("/")
async def root():
    url = f"http://127.0.0.1:5002"
    response = requests.get(url)
    print("Request Reached Service B")
    return response.text
