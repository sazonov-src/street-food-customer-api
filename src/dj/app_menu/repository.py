from app_menu.models import MenuItem
from dj.repository import BaseRepository
from domain import items


class RepositoryMenuItem(BaseRepository):
   
    def __init__(self, item: MenuItem):
        self._item = item

    def get(self) -> items.Item:
        return items.Item(
                title=self._item.title, 
                description=self._item.description, 
                price=self._item.price)

    def add(self, data: items.Item):
        self._item.title = data.title
        self._item.description = data.description
        self._item.price = data.price
        self._item.save()

    @property
    def model(self):
        return self._item
