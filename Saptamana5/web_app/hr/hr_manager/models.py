from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employer(BaseModel):
    class Meta:
        db_table = 'employers'

    name = models.CharField(max_length=255, null=False, unique=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, default=1)
    employees = models.ManyToManyField(
        User, through='Employee', related_name='employees')

    def __str__(self):
        return self.name


class Employee(BaseModel):
    class Meta:
        db_table = 'employees'

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=100.00,
        null=False,
        validators=[MinValueValidator(0.00)]
    )
