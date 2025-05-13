from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArticleForm, CommentForm
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'wiki/article_list.html'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'wiki/article_detail.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'wiki/article_create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('wiki:article-list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'wiki/article_update.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy('wiki:article-detail', kwargs={'pk': self.kwargs['pk']})
