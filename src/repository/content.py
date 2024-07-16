from sqlalchemy.orm import Session

from models.content import Content

def get_content(db: Session, company: str):
    return db.query(Content).filter(Content.company == company).first()