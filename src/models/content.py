from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database.database import Base

class Content(Base):
    __tablename__ = "contents"

    id= Column(Integer, primary_key=True)
    name= Column(String)
    logo_path= Column(String)
    company=Column(String)