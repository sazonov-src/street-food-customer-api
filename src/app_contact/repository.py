from domain.models import contact

from .models import Contact
from .serializers import ContactSerializer


def get_last_contact(user):
    contact_ = Contact.objects.filter(user=user).last()
    if contact_:
        serializer = ContactSerializer(contact_)
        return contact.Contact(**serializer.data)
    raise ValueError("Contact not found")


class ContactRepository:
    def __init__(self, user) -> None:
        self.user = user

    def get(self):
        return get_last_contact(self.user)


        

