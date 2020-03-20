from django.shortcuts import render, get_object_or_404, redirect
from seller.models import ProductData
from carts.models import PCart, Quantity
from django.db.models import Sum
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from MiniProjectFinal.settings import MEDIA_ROOT


# Create your views here.
def showcart(request):
    num_res = PCart.objects.filter(user=request.user.email).count()
    if num_res == 0:
        p = PCart(user=request.user.email)
        p.save()
    p1 = PCart.objects.get(user__iexact=request.user.email)
    total = 0
    x = list(p1.p_name.values())
    y = list(p1.quant.values())
    for i, j in zip(x, y):
        total += int(i['p_price']) * int(j['min_q'])
    return render(request, 'carts/showcart.html', {'prod': p1, 'total': total})


def removecart(request, object_id, object_id1):
    num_res = PCart.objects.filter(user=request.user.email).count()
    if num_res == 0:
        p = PCart(user=request.user.email)
        p.save()
    p1 = PCart.objects.get(user__iexact=request.user.email)
    q1 = get_object_or_404(ProductData, id=object_id)
    q2 = get_object_or_404(Quantity, id=object_id1)
    p1.p_name.remove(q1)
    p1.quant.remove(q2)
    p1.save()
    return redirect('/cart')


def check(request):
    saving = MEDIA_ROOT + r'\uploads\Invoice.pdf'
    c = canvas.Canvas(filename=saving, pagesize=A4, bottomup=False)
    c.drawString(10, 10, 'ajsj')
    return redirect('/')
