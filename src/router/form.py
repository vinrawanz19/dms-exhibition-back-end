from fastapi import Depends, APIRouter, HTTPException
from database.database import SessionLocal, engine
from repository.form import create_form, get_form
from schemas.form import FormCreate, Form
from sqlalchemy.orm import Session

routerForm = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@routerForm.post("/form", response_model=Form)
async def router_create_form(form:FormCreate , db: Session = Depends(get_db)):
    db_form_search = get_form(db, form.email, form.company)
    if(db_form_search is not None):
        raise HTTPException(status_code=404, detail="Email telah digunakan, mohon untuk menggunakan email lain")

    return create_form(form=form, db=db)