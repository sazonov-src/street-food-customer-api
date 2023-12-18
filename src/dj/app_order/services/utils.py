from rest_framework.exceptions import ValidationError


def validate(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError) as ex:
            raise ValidationError(ex)
    return wrapper
