from django.shortcuts import render
from seller.models import ProductData
from accounts.models import UserData
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from accounts.models import SellerData
from django.contrib import messages
from carts.models import PCart, Quantity

# Create your views here.
def c1(request):
    return render(request, 'customer/c1.html')


def dis(request):
    x = ProductData.objects.all()
    l = len(list(x))
    c = []
    for i in range(0, l):
        string = 'obj-' + str(i)
        c.append(string)
    if request.method == 'POST':
        for i in c:
            y = request.POST.get(i, False)
            print(y)

    return render(request, 'customer/product_display.html', {'prods': x})


def desc(request, object_id):
    product = ProductData.objects.get(id=object_id)
    list_products = ProductData.objects.filter(p_name__icontains=product.p_name).order_by('-p_price')
    if request.method == 'POST' and 'deleter' in request.POST:
        Q = request.POST.get('quant', product.min_q)
        num_res = PCart.objects.filter(user=request.user.email).count()
        if num_res == 0:
            p = PCart(user=request.user.email)
            p.save()
        q = Quantity(min_q=Q)
        q.save()
        p1 = PCart.objects.get(user__iexact=request.user.email)
        p1.p_name.add(list_products[0])
        p1.quant.add(q)
        p1.save()
    return render(request, 'customer/product_description.html',
                  {'data': product, 'listdata': list_products})


def profile(request):
    x = UserData.objects.all()
    for y in x:
        if y.email == request.user.username:
            return render(request, 'customer/profile.html', {'data': y})


def showpage(request, object_id, p_id):
    s = SellerData.objects.get(email=object_id)
    return render(request, 'customer/showpg.html', {'data': s})
