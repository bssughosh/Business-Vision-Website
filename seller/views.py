from django.shortcuts import render, redirect
from .forms import ProductUploadForm
from django.contrib.auth.models import User, auth


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
