from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    cash = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=3,
        default=10000.00
    )

    def __str__(self):
        return self.username