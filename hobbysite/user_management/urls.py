from django.urls import path

from .views import ProfileUpdateView

urlpatterns = [
    path('username', ProfileUpdateView.as_view(), name='username'),
]

app_name = "user_management"
