from django.contrib import admin
from .models import ProductData, Rating, UsersRated

# Register your models here.
admin.site.register(ProductData)
admin.site.register(Rating)
admin.site.register(UsersRated)
