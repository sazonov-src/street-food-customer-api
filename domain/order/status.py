from collections import abc
import copy
from dataclasses import dataclass
from typing import Optional

import order


class OrderDataError(Exception):
    pass


@dataclass
class ManageStatusOrder[T: order.OrderBase]:
    items: Optional[abc.Iterable[order.OrderLine]] = None
    user_data: Optional[order.UserData] = None
    payed: bool = False
    ready: bool = False
    done: bool = False

    @property
    def _true_data(self):
        data = copy.copy(self.__dict__)
        while data:
            key, value = data.popitem()
            if value:
                data.update({key: value})
                return data
        return {}

    def validate(self):
        for value in self._true_data.values():
            if not value:
                raise OrderDataError

    def _last_attr(self):
        try:
            return tuple(self._true_data)[-1]
        except IndexError:
            return "items"

    def get_order(self) -> T:
        return {
            "items": order.OrderNew,
            "user_data": order.OrderCheckout,
            "payed": order.OrderPayed,
            "ready": order.OrderReady,
            "done": order.OrderDone
       }[self._last_attr()](self.items, self.user_data)

    def __setattr__(self, __name, __value) :
        super().__setattr__(__name, __value)
        self.validate()
