from django.shortcuts import render, redirect
from seller.models import ProductData, Rating, UsersRated
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
    # l = len(list(x))
    # c = []
    # for i in range(0, l):
    #     string = 'obj-' + str(i)
    #     c.append(string)
    if request.method == 'POST':
        for i in c:
            y = request.POST.get(i, False)
            print(y)

    return render(request, 'customer/product_display.html', {'prods': x})


def desc(request, object_id):
    product = ProductData.objects.get(id=object_id)
    list_products = ProductData.objects.filter(p_name__icontains=product.p_name).order_by('-p_price')
    p1 = ProductData.objects.filter(id=list_products[0].id).values()
    s = p1[0]['seller_name']
    num_res1 = Rating.objects.filter(seller=s).count()
    if num_res1 == 0:
        co = 0
        us = []
    else:
        co = Rating.objects.filter(seller=s).values()[0]['rate']
        us1 = Rating.objects.get(seller=s)
        us = us1.users.values_list()
        print(us)
    if request.method == 'POST' and 'deleter' in request.POST:
        Q = request.POST.get('quant', list_products[0].min_q)
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
                  {'data': product, 'listdata': list_products, 't': 0, 'co': co, 'us': us})


def desc1(request, object_id):
    product = ProductData.objects.get(id=object_id)
    list_products = ProductData.objects.filter(p_name__icontains=product.p_name).order_by('-p_price')
    p1 = ProductData.objects.filter(id=product.id).values()
    s = p1[0]['seller_name']
    num_res1 = Rating.objects.filter(seller=s).count()
    if num_res1 == 0:
        co = 0
    else:
        co = Rating.objects.filter(seller=s).values()[0]['rate']
    if request.method == 'POST' and 'deleter' in request.POST:
        Q = request.POST.get('quant', product.min_q)
        num_res = PCart.objects.filter(user=request.user.email).count()
        if num_res == 0:
            p = PCart(user=request.user.email)
            p.save()
        q = Quantity(min_q=Q)
        q.save()
        p1 = PCart.objects.get(user__iexact=request.user.email)
        p1.p_name.add(product)
        p1.quant.add(q)
        p1.save()
    return render(request, 'customer/product_description.html',
                  {'data': product, 'listdata': list_products, 't': 1, 'co': co})


def profile(request):
    x = UserData.objects.all()
    for y in x:
        if y.email == request.user.username:
            return render(request, 'customer/profile.html', {'data': y})


def showpage(request, object_id, p_id):
    s = SellerData.objects.get(email=object_id)
    return render(request, 'customer/showpg.html', {'data': s})


def rate(request, p, r):
    p1 = ProductData.objects.filter(id=p).values()
    s = p1[0]['seller_name']
    u = request.user.email
    num_res = Rating.objects.filter(seller=s).count()
    if num_res == 0:
        t = Rating(seller=s, rate=r)
        t.save()
    t1 = Rating.objects.get(seller__iexact=s)
    f = False
    for i in t1.users.values():
        if u == i['user']:
            f = True
            break
    if f:
        u1 = UsersRated.objects.get(user__iexact=u)
    else:
        u1 = UsersRated(user=u)
        u1.save()
    t1.users.add(u1)
    r1 = t1.rate
    r1 = (r1 + r) // 2
    t1.rate = r1
    t1.save()
    return redirect('/cust/description1/' + str(p) + '/')
