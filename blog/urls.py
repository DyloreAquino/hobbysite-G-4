from django.contrib import admin
from django.urls import path, include

from .views import (
    ArticleDetailView,
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleAddImageView,
)


urlpatterns = [
    path('articles', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>', ArticleDetailView.as_view(),
         name='article_detail'),
    path('article/add', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/edit',
         ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/add_image',
         ArticleAddImageView.as_view(), name='article_addimage'),

]

app_name = "blog"
