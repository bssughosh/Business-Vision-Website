from django.shortcuts import render
from seller.models import ProductData
from carts.models import PCart


# Create your views here.
def showcart(request):
    num_res = PCart.objects.filter(user=request.user.email).count()
    if num_res == 0:
        p = PCart(user=request.user.email)
        p.save()
    p1 = PCart.objects.get(user__iexact=request.user.email)
    print(p1.quant.values())
    return render(request, 'carts/showcart.html', {'prod': p1.p_name.values(), 'quant': p1.quant.values()})
