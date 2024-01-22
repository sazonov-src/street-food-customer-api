from pydantic import BaseModel


class ModalContact(BaseModel):
    name: str
    phone: str
