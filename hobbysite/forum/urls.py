from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('products/list', ProductListView.as_view(), name='product-list'),
    path('product/detail/<int:pk>', ProductDetailView.as_view(), name='product-detail')
]

app_name = 'forum'