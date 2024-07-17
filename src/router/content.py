from fastapi import Depends, APIRouter, HTTPException
from database.database import SessionLocal, engine
from repository.content import get_content
from schemas.content import Content as ContentSchemas
from sqlalchemy.orm import Session

routerContent = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@routerContent.get("/content/{company}", response_model=ContentSchemas)
def read_users(company:str , db: Session = Depends(get_db)):
    db_content = get_content(company=company, db=db)
    if db_content is None:
        raise HTTPException(status_code=404, detail="Gagal mendapatkan content")
    return db_content