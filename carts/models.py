from django.db import models
from seller.models import ProductData


# Create your models here.
class Quantity(models.Model):
    min_q = models.CharField(max_length=10)


class PCart(models.Model):
    user = models.CharField(max_length=50, null=True)
    p_name = models.ManyToManyField(ProductData)
    quant = models.ManyToManyField(Quantity)
