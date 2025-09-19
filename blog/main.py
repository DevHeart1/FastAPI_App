from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str

@app.post("/blog")
def create(request: Blog):
    return {"data": f"creating blog with title as {request.title} and body as {request.body}"}