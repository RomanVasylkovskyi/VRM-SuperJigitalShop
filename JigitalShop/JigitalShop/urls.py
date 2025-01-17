"""
URL configuration for JigitalShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

import MainPage.views as main_views
import Store.views as store_views

urlpatterns = [
    path('admin/', admin.site.urls , name='admin'),
    path('', main_views.main_page_view, name='main_page_view'),
    path('store', store_views.item_list, name='store'),
    path('product/<int:id>/', store_views.product_detail, name='product_detail'),
    path('', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', views.ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    
    # Review URLs
    path('product/<int:pk>/review/new/', views.ReviewCreateView.as_view(), name='review-create'),
    path('review/<int:pk>/update/', views.ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review-delete'),
]
