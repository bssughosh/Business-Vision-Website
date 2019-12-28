from django.shortcuts import render

# Create your views here.
def c1(request):
    return render(request, 'customer/c1.html')