from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from smartfields import fields
from django.db.models.signals import pre_delete, post_save
from django.dispatch.dispatcher import receiver
from django.conf import settings
import os


# image compression method
def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=40)
    new_image = File(im_io, name=image.name)
    return new_image


def get_name(instance, filename):
    return "{}/{}".format(instance.id, filename)


# Create your models here.
class ProductData(models.Model):
    PRODUCT_CHOICES = (
        ('Electronics', (
            ('Camera', 'CAMERA'),
            ('Fan', 'FAN'),
            ('Keyboard', 'KEYBOARD'),
            ('Monitor', 'MONITOR'),
            ('Mouse', 'MOUSE')
        ),),

        ('Home Decor', (
            ('Alarm', 'ALARM'),
            ('Showcase', 'SHOWCASE'),
            ('Table Fan', 'TABLE FAN')
        ),),

        ('Medical', (
            ('Mask', 'MASK'),
            ('Sanitizer', 'SANITIZER')
        ),),

        ('Office Supplies', (
            ('Folder', 'FOLDER'),
            ('Paper Weight', 'PAPER WEIGHT'),
            ('Pen Holder', 'PEN HOLDER'),
            ('White Board', 'WHITE BOARD')
        ),),

        ('School Supplies', (
            ('Bag', 'BAG'),
            ('Pen', 'PEN'),
            ('Pencil Box', 'PENCIL BOX')
        ),)
    )
    p_name = models.CharField(max_length=25, choices=PRODUCT_CHOICES, default='Mouse')
    seller_name = models.CharField(max_length=50, null=True)
    s_name = models.CharField(max_length=50, null=True)
    p_img = fields.ImageField(upload_to='pics')
    p_img2 = fields.ImageField(upload_to='pics', null=True)
    p_img3 = fields.ImageField(upload_to='pics', null=True)
    p_img4 = fields.ImageField(upload_to='pics', null=True)
    p_price = models.IntegerField()
    min_q = models.CharField(max_length=10)
    p_desc = models.TextField(null=True)
    tag = models.CharField(max_length=20, null=True)

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


class UsersRated(models.Model):
    user = models.CharField(max_length=50, null=True)


class Rating(models.Model):
    users = models.ManyToManyField(UsersRated)
    seller = models.CharField(max_length=50, null=True)
    rate = models.IntegerField(default=0)
