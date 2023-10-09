from fastapi import FastAPI
from time import sleep
import requests


app = FastAPI()


@app.get("/")
async def root():
    url = f"http://127.0.0.1:5004"
    print("Request Reached Service D")

    response = requests.get(url)

    return response.text
