"""Urls file."""
from django.urls import path
from . import views
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
    path('list',
         CommissionListView.as_view(),
         name='commissions-list'),
    path('detail/<int:pk>',
         CommissionDetailView.as_view(),
         name='commissions-detail'),
     path('add/', 
          views.handle_commission_add_page,
          name='commission-add')
]

app_name = "commissions"
