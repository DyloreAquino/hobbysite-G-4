from django.urls import path

from .views import homepage

urlpatterns = [
    path('', homepage, name="homepage"),
]

app_name = "homepage"