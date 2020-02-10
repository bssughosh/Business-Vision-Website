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
    p_name = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100, null=True)
    p_img = models.ImageField(upload_to='pics')
    p_price = models.CharField(max_length=10)
    min_q = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        new_image = compress(self.p_img)
        self.p_img = new_image
        super().save(*args, **kwargs)
