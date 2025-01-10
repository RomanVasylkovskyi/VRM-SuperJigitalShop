from django.shortcuts import render,get_object_or_404
from Store.models import Product

# Create your views here.
def item_list(request):
    items = Product.objects.all()
    return render(request, 'main_store.html', {'items': items})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_details.html', {'product': product})
