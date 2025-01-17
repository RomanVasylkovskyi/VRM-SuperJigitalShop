from django.shortcuts import render,get_object_or_404, redirect
from Store.models import Product
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Review
from django.contrib import messages

# Create your views here.
def item_list(request):
    items = Product.objects.all()
    return render(request, 'main_store.html', {'items': items})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_details.html', {'product': product})

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    ordering = ['-created_at']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all().order_by('-created_at')
        return context

class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'price', 'photo', 'description', 'manufacturer', 'rate']
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        messages.success(self.request, 'Продукт успішно створено')
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'price', 'photo', 'description', 'manufacturer', 'rate']

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Продукт успішно оновлено')
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Продукт успішно видалено')
        return super().delete(request, *args, **kwargs)

# Review CRUD
class ReviewCreateView(CreateView):
    model = Review
    template_name = 'reviews/review_form.html'
    fields = ['text']

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        messages.success(self.request, 'Відгук успішно додано')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.kwargs['pk']})

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'reviews/review_form.html'
    fields = ['text']

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.object.product.pk})

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.object.product.pk})

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Відгук успішно видалено')
        return super().delete(request, *args, **kwargs)