from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserData, SellerData
from django.contrib import messages
from pandas.io.json import json_normalize
import requests


# Create your views here.
def home(request):
    return render(request, 'homepage.html')


def login(request):
    if request.method == 'POST':
        u1 = request.POST.get('email', False)
        p1 = request.POST.get('pass', False)
        a = list(UserData.objects.filter(email=u1).values_list('email', flat=True))
        b = list(SellerData.objects.filter(email=u1).values_list('email', flat=True))
        if u1 in a:
            user = auth.authenticate(username=u1, password=p1)
            if user is not None:
                auth.login(request, user)
            else:
                messages.info(request, 'Login Unsuccessful')
                return redirect('/')
            return redirect('/cust')

        if u1 in b:
            user = auth.authenticate(username=u1, password=p1)
            if user is not None:
                auth.login(request, user)
            else:
                messages.info(request, 'Login Unsuccessful')
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
    secret_key = 'XlLJvJ8Kv8YqvgYo602K2SKWS9U2'
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
        st = s.upper()
        cn = c.upper()
        url = 'https://appyflow.in/api/verifyGST?gstNo=' + g + '&key_secret=' + secret_key
        x = requests.get(url).json()
        if 'error' in x.keys():
            if x['error']:
                messages.info(request, 'GST Details not matching')
                return redirect('/')
        else:
            tname = x['taxpayerInfo']['lgnm'].upper()
            st1 = x['taxpayerInfo']['pradr']['addr']['stcd'].upper()
            pin = x['taxpayerInfo']['pradr']['addr']['pncd']
            if str(st) == str(st1) and str(cn) == str(tname) and str(p) == str(pin):
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
            else:
                messages.info(request, 'GST Details not matching')
                return redirect('/')
    return render(request, 'register/seller_regis.html')
