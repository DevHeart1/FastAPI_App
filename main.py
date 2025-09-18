from fastapi import FastAPI
from pydentic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/blog")
def blog(limit: int, published: bool):
    if published:
        return {"data": f"{limit} published blog list"}
    return {"data": f"{limit} blog list"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get("/fetch_blog/{id}")
def fetch_blog(id: int):
    return {"data": id}

@app.get("/about")
def about():
    return {"data": {"This is a simple FastAPI application."}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(blog: dict):
    return {"data": "blog is created"}