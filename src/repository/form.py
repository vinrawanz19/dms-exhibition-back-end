from typing import Optional
from sqlalchemy.orm import Session

from schemas.form import FormCreate
from models.form import Form

def get_form(db: Session, email: str, company: str) -> Optional[Form]:
    return db.query(Form).filter(Form.email == email, Form.company == company).first()


def create_form(db: Session, form: FormCreate) ->Form:
    db_form = Form(**form.model_dump())
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form