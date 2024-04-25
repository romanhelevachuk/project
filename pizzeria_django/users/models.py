from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} | {'Customer' if self.is_customer else 'Admin'}"
