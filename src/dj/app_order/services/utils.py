from rest_framework.exceptions import ValidationError, NotFound

from domain.order.orders import NotFoundException

def validate(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFoundException as ex:
            raise NotFound(ex)
        except (ValueError, KeyError) as ex:
            raise ValidationError(ex)
    return wrapper
