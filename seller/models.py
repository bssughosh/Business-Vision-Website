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
    s_name = models.CharField(max_length=50, null=True)
    p_img = models.ImageField(upload_to='pics')
    p_price = models.CharField(max_length=10)
    min_q = models.CharField(max_length=10)
    p_desc = models.TextField(null=True)

    def save(self, *args, **kwargs):
        x = self.p_img.name.split('.')
        if x[-1] == 'png' or x[-1] == 'PNG':
            png = Image.open(self.p_img)
            png.load()
            background = Image.new("RGB", png.size, (255, 255, 255))
            background.paste(png, mask=png.split()[3])
            new_im = BytesIO()
            background.save(new_im, 'JPEG', quality=80)
            new_image1 = File(new_im, name=self.p_img.name)
        else:
            new_image1 = self.p_img
        new_image = compress(new_image1)
        self.p_img = new_image
        super().save(*args, **kwargs)
