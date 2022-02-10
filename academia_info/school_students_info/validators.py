from django.core.exceptions import ValidationError


def validate_greater_than_zero(value):
    if value <= 0:
        raise ValidationError("Does not accept zero number of students.")
