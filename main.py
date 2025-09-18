from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/blog_list")
def blog():
    return {"data": "blog list"}

@app.get("/blog/{id}")
def fetch_blog(id: int):
    return {"data": id}

@app.get("/about")
def about():
    return {"data": {"This is a simple FastAPI application."}} 