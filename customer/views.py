from django.shortcuts import render
from seller.models import ProductData
from accounts.models import UserData
from django.views.decorators.csrf import csrf_exempt


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
    # if request.method == 'POST':
    #     pid = request.body
    #     pid1 = pid.split('-')
    #     pid = pid1[1]
    #     print(pid)
    #     x = ProductData.objects.all()
    #     y = x[int(pid)]
    #
    # else:
    #     y = ProductData()
    product = ProductData.objects.get(id=object_id)
    return render(request, 'customer/product_description.html', {'data': product})


def profile(request):
    x = UserData.objects.all()
    for y in x:
        if y.email == request.user.username:
            return render(request, 'customer/profile.html', {'data': y})
