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
from django.urls import path

import MainPage.views as main_views
import Store.views as store_views

app_name = 'store'

urlpatterns = [
    path('admin/', admin.site.urls , name='admin'),
    path('', main_views.main_page_view, name='main_page_view'),
    path('store', store_views.item_list, name='store'),
    path('editstore', store_views.admin_store, name='edit_store'),
    path('product/<int:id>/', store_views.product_detail, name='product_detail'),
    path('add/', store_views.add_product, name='add_product'),
    path('delete/<int:pk>/', store_views.delete_product, name='delete_item'),
]