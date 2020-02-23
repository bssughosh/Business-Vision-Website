from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductUploadForm
from django.contrib.auth.models import User, auth
from accounts.models import SellerData
from .models import ProductData
from django.db.models import Q
from django.contrib import messages
import os


# Create your views here.
def s1(request):
    return render(request, 'seller/s1.html')


def product_upload(request):
    b = list(SellerData.objects.filter(email=request.user.username).values_list('name', flat=True))
    if request.method == 'POST':
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.seller_name = request.user.username
            instance.s_name = b[0]
            instance.save();
            messages.info(request, 'Product uploaded successfully!')
            return redirect('/seller')
        else:
            return render(request, 'seller/product_upload.html', {'form': form})
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


def browse(request):
    p = ProductData.objects.all()
    return render(request, 'seller/products_display.html', {'prods': p})


def my_prod(request):
    s_email = request.user.username
    p = ProductData.objects.filter(seller_name__exact=s_email)
    return render(request, 'seller/my_prod.html', {'prods': p})


def editpage(request, object_id):
    obj = get_object_or_404(ProductData, id=object_id)
    form = ProductUploadForm(request.POST or None, request.FILES or None, instance=obj)
    context = {'form': form}

    if request.method == 'POST' and 'deleter' in request.POST:
        file = obj.p_img.path
        ProductData.objects.filter(id=object_id).delete()
        os.remove(file)
        messages.info(request, 'Product Deleted')
        return redirect('/seller')

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.info(request, 'Product updated successfully!')
        context = {'form': form}
        # return render(request, 'seller/product_upload.html', context)
        return redirect('/seller')

    else:
        context = {'form': form}
        return render(request, 'seller/edit_prod.html', context)


def delete_record(request, object_id):
    obj = get_object_or_404(ProductData, id=object_id)
    file = obj.p_img.path
    ProductData.objects.filter(id=object_id).delete()
    os.remove(file)
    messages.info(request, 'Product Deleted')
    return redirect('/seller')
