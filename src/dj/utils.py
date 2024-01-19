import functools

from rest_framework.exceptions import ValidationError


exceptions_mapping = {
    ValueError: ValidationError,
    AssertionError: ValidationError,
}

def validate(exception, massage):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                try:
                    raise exceptions_mapping[exception](massage.format(e))
                except KeyError:
                    raise ValidationError(massage)
        return wrapper
    return decorator
