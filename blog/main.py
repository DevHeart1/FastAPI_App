from fastapi import FastAPI
from . import schema, models
from . database import engine


app = FastAPI()

# Create tables if they don't exist yet using the database engine
models.Base.metadata.create_all(engine)

@app.post("/blog")
def create(request: schema.Blog):
    return {"data": f"creating blog with title as {request.title} and body as {request.body}"}