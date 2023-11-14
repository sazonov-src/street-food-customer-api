# type: ignore
import pytest

import permissions

class Obj1: pass
class Obj2: pass
class Obj3: pass

class FakePermission(permissions.PermissionBase):
    ACTION = "c"
    PERMISSIONS = {
            Obj1: "c",
            Obj2: "d"
            }

def test_permission_permissed():
    def create():
        return Obj1()
    FakePermission(create)()

def test_permission_not_permissed():
    def create():
        return Obj2()
    with pytest.raises(permissions.PermissionIsAuthorizedError):
        FakePermission(create)()

def test_permission_not_found_obj():
    def create():
        return Obj3()
    with pytest.raises(permissions.PermissionNotFoundObjTypeError):
        FakePermission(create)()

def test_return_obj():
    def create():
        return Obj1()
    obj = FakePermission(create)()
    assert isinstance(obj, Obj1)

