import django
from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import CustomUser
from django.utils.timezone import now

# Create your models here.

class Portofolio(models.Model):
    class Meta:
        db_table = 'portofolios'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='portofolio', null=True)
    symbol = models.CharField(null=False, unique=True, max_length=20)
    shares = models.IntegerField(null=False, default=0)


class Contract(models.Model):
    class Meta:
        db_table = 'contracts'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contracts', null=True)
    symbol = models.CharField(null=False, max_length=20)
    datetime = models.DateTimeField(null=False, default=now)
    shares = models.IntegerField(null=False, default=0)
    price = models.DecimalField(
        null=False,
        max_digits=10,
        default=0.00,
        decimal_places=2,
        validators=[MinValueValidator(0.00)],
    )
    type = models.CharField(null=False, default='BUY', max_length=5)
