from django.contrib.auth.models import User

from django.db import models


class CustomUser(User):
    phone = models.CharField(max_length=20, unique=True)
