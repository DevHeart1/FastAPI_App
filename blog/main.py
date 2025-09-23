from fastapi import FastAPI
from . import schema, models
from . database import engine
from sqlalchemy.orm import Session
from fastapi import Depends


app = FastAPI()

# Create tables if they don't exist yet using the database engine
models.Base.metadata.create_all(engine)

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

@app.post("/blog")
def create(request: schema.Blog, db : Session = Depends(get_db)):
    db.add(models.Blog(**request.dict()))
    db.commit()
    db.refresh()
    return db
    