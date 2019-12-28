from django.db import models


# Create your models here.
class ProductData(models.Model):
    p_name = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    p_img = models.ImageField(upload_to='pics')
    p_price = models.CharField(max_length=10)
    min_q = models.CharField(max_length=10)
