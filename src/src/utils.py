import functools

from rest_framework.exceptions import ValidationError


def validate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            raise ValidationError(e)
    return wrapper

def convert_camel_to_snake(class_name):
    result = [class_name[0].lower()]
    for char in class_name[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)
    return ''.join(result)

def set_repo(class_repo, get=True, add=True):
    def decorator(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            cart_repo = class_repo(self.get_user)
            attr_name = '_'.join(convert_camel_to_snake(class_repo.__name__).split('_')[:-1])
            if get:
                setattr(self, attr_name, cart_repo.get())
            res = method(self, *args, **kwargs)
            if add:
                cart_repo.add(getattr(self, attr_name))
            return res
        return wrapper
    return decorator
