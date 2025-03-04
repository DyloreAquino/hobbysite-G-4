from django.urls import path

from .views import index, ArticleDetailView, ArticleListView

urlpatterns = [
    path('', index, name ='index'),
    path('wiki/articles', ArticleListView.as_view(), name='wiki-list'),
    path('wiki/article/<int:pk>', ArticleDetailView.as_view(), name='wiki-detail')
]

app_name = "wiki"