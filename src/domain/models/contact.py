from pydantic import BaseModel


class ModalContact(BaseModel):
    name: str
    phone: str

    def __hash__(self):
        return hash((self.name, self.phone))
