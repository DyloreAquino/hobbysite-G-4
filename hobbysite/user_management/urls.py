from django.urls import path

from .views import ProfileUpdateView

urlpatterns = [
    path('<str:user__username>', ProfileUpdateView.as_view(), name='username'),
]

app_name = "user_management"
