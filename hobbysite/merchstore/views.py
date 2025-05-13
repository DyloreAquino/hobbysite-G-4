from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

from .models import Product
from .forms import TransactionForm, ProductForm, ProductUpdateForm

class ProductListView(ListView):
    model = Product
    template_name = 'merchstore/product_list.html'
    
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'merchstore/product_detail.html'
    form_class = TransactionForm
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'merchstore/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('merchstore:product_list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)
    
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'merchstore/product_update.html'
    form_class = ProductUpdateForm
    
    def get_success_url(self):
        return reverse_lazy('merchstore:product_detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        if form.instance.stock != 0:
            form.instance.status = form.instance.AVAILABLE
            
        else:
            form.instance.status = form.instance.OUTOFSTOCK
        
        return super().form_valid(form)
