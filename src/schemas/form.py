from pydantic import BaseModel


class FormBase(BaseModel):
    name: str
    email: str
    phone_number: str
    remark : str | None
    company: str

class FormCreate(FormBase):
    pass


class Form(FormBase):
    id: int

    class Config:
        orm_mode = True