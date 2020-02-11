from django.shortcuts import render
from seller.models import ProductData
from accounts.models import UserData
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


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
    return render(request, 'customer/product_description.html', {'data': product})


def profile(request):
    x = UserData.objects.all()
    for y in x:
        if y.email == request.user.username:
            return render(request, 'customer/profile.html', {'data': y})


def search(request):
    query = request.GET.get('q', None)
    x = ProductData.objects.none()
    if query is not None:
        lookups = Q(p_name__icontains=query) | Q(p_desc__icontains=query)
        x = ProductData.objects.filter(lookups).distinct()
        return render(request, 'customer/product_display.html', {'prods': x})
    return render(request, 'customer/product_display.html', {'prods': x})
