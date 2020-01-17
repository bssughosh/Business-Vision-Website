from django.shortcuts import render
from seller.models import ProductData


# Create your views here.
def c1(request):
    return render(request, 'customer/c1.html')


def dis(request):
    x = ProductData.objects.all()
    return render(request, 'customer/product_display.html', {'prods': x})
