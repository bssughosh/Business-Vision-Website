from django.shortcuts import render
from seller.models import ProductData
from accounts.models import UserData
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def c1(request):
    return render(request, 'customer/c1.html')


def dis(request):
    x = ProductData.objects.all()
    # if request.method == 'POST':
    #     pid = request.POST.get('pid', False)
    #     print(pid)
    flag = False
    if request.method == 'POST':
        s = request.POST.get('pname',False)
        if not s:
            for y in x:
                if s == y.p_name:
                    print('Found')
                    flag =True
                    return render(request, 'customer/product_display.html', {'prods1': y})

    return render(request, 'customer/product_display.html', {'prods': x})


def desc(request):
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
    return render(request, 'customer/product_description.html')


def profile(request):
    x = UserData.objects.all()
    for y in x:
        if y.email == request.user.username:
            return render(request, 'customer/profile.html', {'data': y})
