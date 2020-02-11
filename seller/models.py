from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File


# image compression method
def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=40)
    new_image = File(im_io, name=image.name)
    return new_image


# Create your models here.
class ProductData(models.Model):
    PRODUCT_CHOICES = (
        ('Mouse', 'MOUSE'),
        ('Keyboard', 'KEYBOARD'),
        ('Camera', 'CAMERA'),
        ('Shirt', 'SHIRT'),
        ('T Shirt', 'T-SHIRT'),
        ('Jeans', 'JEANS'),
        ('Trousers', 'TROUSERS'),
        ('Bat', 'BAT'),
        ('Ball', 'BALL'),
        ('Cap', 'CAP'),
        ('Pen', 'PEN'),
        ('Pen Holder', 'PEN HOLDER'),
        ('Paper Weight', 'PAPER WEIGHT'),
        ('White Board', 'WHITE BOARD'),
        ('Table Fan', 'TABLE FAN'),
        ('Showcase', 'SHOWCASE'),
        ('Air Purifier', 'AIR PURIFIER'),
    )
    p_name = models.CharField(max_length=25, choices=PRODUCT_CHOICES, default='Mouse')
    seller_name = models.CharField(max_length=50, null=True)
    p_img = models.ImageField(upload_to='pics')
    p_price = models.CharField(max_length=10)
    min_q = models.CharField(max_length=10)
    p_desc = models.TextField(null=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.p_img)
        self.p_img = new_image
        super().save(*args, **kwargs)
