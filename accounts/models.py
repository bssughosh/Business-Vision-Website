from django.db import models
from gst_field.modelfields import GSTField


# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    dob = models.CharField(max_length=15)


class SellerData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    gst = GSTField()
    comp_name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=8)
