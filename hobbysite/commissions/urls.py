"""Urls file."""
from django.urls import path
from . import views
from .views import (
    CommissionListView,
    CommissionDetailView,
    CommissionUpdateView)

urlpatterns = [
    path('list',
         CommissionListView.as_view(),
         name='commissions-list'),
    path('detail/<int:pk>',
         CommissionDetailView.as_view(),
         name='commissions-detail'),
    path('<int:pk>/edit',
         CommissionUpdateView.as_view(),
         name='commissions-update'),
    path('add/',
         views.handle_commission_add_page,
         name='commission-add')
]

app_name = "commissions"
