from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserData, SellerData
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'homepage.html')


def login(request):
    if request.method == 'POST':
        u1 = request.POST.get('username1', False)
        p1 = request.POST.get('password1', False)
        u2 = request.POST.get('username2', False)
        p2 = request.POST.get('password2', False)

        if not u1:
            a = UserData.objects.all()
            x = []
            for i in a:
                x.append(i.email)
            user = auth.authenticate(username=u2, password=p2)
            if user is not None and u2 in x:
                auth.login(request, user)
            else:
                return redirect('/')
            return redirect('/cust')
        else:
            a = SellerData.objects.all()
            x = []
            for i in a:
                x.append(i.email)
            user = auth.authenticate(username=u1, password=p1)
            if user is not None and u1 in x:
                auth.login(request, user)
            else:
                return redirect('/')
            return redirect('/seller')
    return render(request, 'registration/login.html')


def cust_regis(request):
    if request.method == 'POST':
        e = request.POST.get('email', False)
        n = request.POST.get('name', False)
        m = request.POST.get('mobile', False)
        p1 = request.POST.get('password1', False)
        p2 = request.POST.get('password2', False)
        d = request.POST.get('dob', False)
        if p1 == p2:
            if User.objects.filter(username=e).exists():
                messages.info(request, 'Username taken')
                return redirect('/')
            else:
                user = User.objects.create_user(username=e, password=p1, email=e,
                                                first_name=n, last_name='1')
                user.save();
                p = UserData(password=p1, email=e, name=n, mobile=m, dob=d)
                p.save();
                messages.info(request, 'User registered')
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
        return redirect('/')

    return render(request, 'register/cust_regis.html')


def seller_regis(request):
    if request.method == 'POST':
        e = request.POST.get('email', False)
        n = request.POST.get('name', False)
        m = request.POST.get('mobile', False)
        p1 = request.POST.get('password1', False)
        p2 = request.POST.get('password2', False)
        c = request.POST.get('cname', False)
        ca = request.POST.get('address', False)
        s = request.POST.get('state', False)
        p = request.POST.get('pin', False)
        g = request.POST.get('gst', False)
        if p1 == p2:
            if User.objects.filter(username=e).exists():
                messages.info(request, 'Username taken')
                return redirect('/')
            else:
                user = User.objects.create_user(username=e, password=p1, email=e,
                                                first_name=n, last_name='0')
                user.save();
                p = SellerData(name=n, email=e, password=p1, mobile=m, comp_name=c, address=ca, gst=g, state=s,
                               pincode=p)
                p.save();
                messages.info(request, 'User registered')
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
        return redirect('/')
    return render(request, 'register/seller_regis.html')
