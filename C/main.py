from fastapi import FastAPI
from time import sleep


app = FastAPI()


@app.get("/")
async def root():
    print("Request Reached Service C")
    return {"name": "Tarun Jaikishan", "age": 20}
