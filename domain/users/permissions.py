from abc import ABC, abstractmethod
from domain import users
from order import order


class PermissionNotFoundObjTypeError(Exception):
    pass

class PermissionIsAuthorizedError(Exception):
    pass


class PermissionBase(ABC):
    PERMISSIONS: dict
    ACTION: str

    def __init__(self, func) -> None:
        self._func = func

    def __call__(self, *args, **kwargs):
        obj = self._func(*args, **kwargs)
        self.check_permission(obj, self.ACTION)
        return obj

    @classmethod
    def check_permission(cls, obj, per):
        try:
            perms = cls.PERMISSIONS[type(obj)]
        except KeyError:
            raise PermissionNotFoundObjTypeError 
        if per not in perms:
            raise PermissionIsAuthorizedError       


class PermissionCastomerBase(PermissionBase, ABC):
    PERMISSIONS = {
        order.OrderNew : "crud",
        order.OrderCheckout : "crud",
        order.OrderPayed : "cr",
        order.OrderReady : "r",
        order.OrderDone : "r",
        }

class PermissionCastomerCreate(PermissionCastomerBase):
    ACTION = "c"

class PermissionCastomerReade(PermissionCastomerBase):
    ACTION = "r"

class PermissionCastomerUpdate(PermissionCastomerBase):
    ACTION = "u"

class PermissionCastomerDelete(PermissionCastomerBase):
    ACTION = "d"
