from pydantic import BaseModel


class ContentBase(BaseModel):
    name: str
    logo_path: str
    company: str


class ContentCreate(ContentBase):
    pass


class Content(ContentBase):
    id: int

    class Config:
        orm_mode = True