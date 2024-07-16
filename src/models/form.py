from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database.database import Base

class Form(Base):
    __tablename__ = "forms"

    id= Column(Integer, primary_key=True)
    name= Column(String)
    email= Column(String)
    phone_number= Column(String)
    company= Column(String)
    remark= Column(String)