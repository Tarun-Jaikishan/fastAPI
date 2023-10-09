from fastapi import FastAPI
from time import sleep


app = FastAPI()


@app.get("/")
async def root():
    print("Request Reached Service E")

    return {"name": "Langesh", "age": 21}
