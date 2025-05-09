from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'wiki/wiki_list.html'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'wiki/wiki_detail.html'
