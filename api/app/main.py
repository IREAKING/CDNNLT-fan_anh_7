from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated, List
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
models.Base .metadata.create_all(bind=engine)

class foodybase(BaseModel):
    Id: int
    Name: str
    Address: str
    Phone: str
    Image: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/foodies/", response_model=List[foodybase])
async def get_all_foody(db: Session = Depends(get_db)):
    return db.query(models.Foody).all()

@app.get("/foodies/{search_term}", response_model=List[foodybase])
async def search_foody_by_name(search_term: str, db: Session = Depends(get_db)):
    results = db.query(models.Foody).filter(models.Foody.Name.like(f"%{search_term}%")).all()
    if not results:
        raise HTTPException(status_code=404, detail="No foody found with the given search term")
    return results

#origins = [
#    "http://web:80" 
#]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả các origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)