from django.shortcuts import render
from seller.models import ProductData
from accounts.models import UserData
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from accounts.models import SellerData


# Create your views here.
def search(request):
    query = request.GET.get('q', None)
    x = ProductData.objects.none()
    if query is not None:
        lookups = Q(p_name__icontains=query) | Q(p_desc__icontains=query)
        x = ProductData.objects.filter(lookups).distinct()
        return render(request, 'search/search-display.html', {'prods': x, 'tot': len(x)})
    return render(request, 'search/search-display.html', {'prods': x, 'tot': len(x)})
