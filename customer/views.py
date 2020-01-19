from django.shortcuts import render
from seller.models import ProductData
from accounts.models import UserData


# Create your views here.
def c1(request):
    return render(request, 'customer/c1.html')


def dis(request):
    x = ProductData.objects.all()
    return render(request, 'customer/product_display.html', {'prods': x})


def desc(request):
    return render(request, 'customer/product_description.html')


def profile(request):
    x = UserData.objects.all()
    t = []
    for y in x:
        if y.email == request.user.username:
            return render(request, 'customer/profile.html', {'data': y})
