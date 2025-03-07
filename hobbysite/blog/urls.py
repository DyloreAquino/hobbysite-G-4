from django.urls import path

from .views import index, ArticleDetailView, ArticleListView

urlpatterns = [
    path('articles', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>', ArticleDetailView.as_view(),
         name='article_detail')
]

app_name = "blog"
