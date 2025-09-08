# app/main.py
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .db import SessionLocal, engine
from . import models, schemas

app = FastAPI(title="Piggery API", version="0.2.0")

# Create tables on startup (uses the database you created)
models.Base.metadata.create_all(bind=engine)

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Health checks
@app.get("/")
def root():
    return {"message": "Piggery API is running (MySQL)"}

@app.get("/hello")
def hello():
    return {"message": "Hello Piggery!"}

# --- PIGS CRUD (now stored in MySQL) ---
@app.get("/pigs", response_model=List[schemas.PigOut])
def list_pigs(db: Session = Depends(get_db)):
    return db.query(models.Pig).all()

@app.post("/pigs", response_model=schemas.PigOut, status_code=201)
def create_pig(pig: schemas.PigIn, db: Session = Depends(get_db)):
    # ensure tag_id is unique
    exists = db.query(models.Pig).filter(models.Pig.tag_id == pig.tag_id).first()
    if exists:
        raise HTTPException(status_code=400, detail="tag_id already exists")

    obj = models.Pig(
        tag_id=pig.tag_id,
        birth_date=pig.birth_date,
        breed=pig.breed,
        weight=pig.weight,
        sex=pig.sex,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj