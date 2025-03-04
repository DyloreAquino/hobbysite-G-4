from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ProductType, Product

class ProductListView(ListView):
    model = Product
    template_name = 'forum/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'forum/product_detail.html'