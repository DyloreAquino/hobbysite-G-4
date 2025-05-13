"""Urls file."""
from django.urls import path
from .views import (
    CommissionListView, CommissionDetailView,
    CommissionCreateView
)

urlpatterns = [
    path('list',
         CommissionListView.as_view(),
         name='commissions-list'),
    path('detail/<int:pk>',
         CommissionDetailView.as_view(),
         name='commissions-detail'),
     path('add/', 
          CommissionCreateView.as_view(),
          name='commission-add')
]

app_name = "commissions"
