from django.shortcuts import render,get_object_or_404, redirect
from Store.models import Product
from Store.form import ProductForm, ReviewForm

# Create your views here.

def item_list(request):
    items = Product.objects.all()
    return render(request, 'main_store.html', {'items': items})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = product.reviews.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', id=product.id)
    else:
        form = ReviewForm()
    return render(request, 'product_details.html', {'product': product, 'reviews': reviews, 'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# def edit_product(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('store:product_details', id=id)
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'edit_product.html', {'form': form})

# def delete_product(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('store:main_page_view')
#     return render(request, 'delete_product.html', {'product': product})