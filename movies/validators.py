from django.core.exceptions import ValidationError


def rating_validator(value):
    if value < 0 or value > 10:
        raise ValidationError(
            message=(
                'Значение поля "rating" должен быть в пределах от 0 до 10'
                f'Текущее значение: {value}'))
