from django.core.validators import RegexValidator

phone_validator = RegexValidator(
        regex=r'^\+?7?\d{10,23}$',
        message="Номер телефона ДОЛЖЕН быть в формате: '+71112223344'. "
                "Максимальное кол-во символов 24 (из них первые два '+7')."
    )