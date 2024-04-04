from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

from src.main import main




app = FastAPI()

class Prompt(BaseModel):
    prompt: str





@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("ask")
def ask_model(input:Prompt):
    resp = main(Prompt.prompt)
    return resp
