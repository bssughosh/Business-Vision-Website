from django.shortcuts import render, redirect
from .forms import ProductUploadForm
from django.contrib.auth.models import User, auth
from accounts.models import SellerData
from .models import ProductData
from django.db.models import Q

# Create your views here.
def s1(request):
    return render(request, 'seller/s1.html')


def product_upload(request):
    if request.method == 'POST':
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.seller_name = request.user.username
            instance.save();
            return redirect('/seller')
    else:
        form = ProductUploadForm()
    return render(request, 'seller/product_upload.html', {
        'form': form
    })


def profile(request):
    x = SellerData.objects.all()
    for y in x:
        if y.email == request.user.username:
            return render(request, 'seller/profile.html', {'data': y})


def search(request):
    query = request.GET.get('q', None)
    x = ProductData.objects.none()

    if query is not None:
        lookups = Q(p_name__icontains=query) | Q(p_desc__icontains=query)
        x = ProductData.objects.filter(lookups).distinct()
        return render(request, 'customer/product_display.html', {'prods': x})
    return render(request, 'customer/product_display.html', {'prods': x})
