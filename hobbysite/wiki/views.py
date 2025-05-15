from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArticleForm, ArticleUpdateForm
from .forms import CommentForm, ArticleImageForm
from django.urls import reverse_lazy
from django.shortcuts import render, reverse, redirect
from .models import Article, ArticleCategory, Comment


class ArticleListView(ListView):
    """
    List view for the articles
    """

    model = Article
    template_name = 'wiki/article_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        categories = ArticleCategory.objects.all()
        remove = []
        author = self.request.user
        if hasattr(author, 'profile'):
            for category in categories:
                if (
                    category.wiki_articles.exclude(author=author.profile).first()
                    is None
                ):
                    remove.append(category.name)

        categories = ArticleCategory.objects.exclude(name__in=remove)
        ctx['categories'] = categories
        return ctx


class ArticleDetailView(LoginRequiredMixin, DetailView):
    """
    Detail view for the articles
    """

    model = Article
    template_name = 'wiki/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.wiki_comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = self.request.user.profile
            comment.article = article
            comment.save()
            return redirect(
                reverse('wiki:article_detail', kwargs={'pk': article.pk}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """
    Create view for the articles
    """

    model = Article
    template_name = 'wiki/article_create.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('wiki:article_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update view for the articles
    """

    model = Article
    template_name = 'wiki/article_update.html'
    form_class = ArticleUpdateForm

    def get_success_url(self):
        return reverse_lazy(
            'wiki:article_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class ArticleAddImageView(LoginRequiredMixin, UpdateView):
    """
    Add image view for the articles
    """

    model = Article
    form_class = ArticleImageForm
    template_name = 'wiki/article_addimage.html'

    def get_success_url(self):
        return reverse_lazy(
            'wiki:article_detail', kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = ArticleImageForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = ArticleImageForm(request.POST, request.FILES)
        if form.is_valid():
            article_image = form.save(commit=False)
            article_image.article = Article.objects.get(pk=self.kwargs['pk'])
            article_image.save()
            return redirect(self.get_success_url())
        else:
            self.object_list = self.get_queryset(**kwargs)
            ctx = self.get_context_data(**kwargs)
            ctx['form'] = form
            return self.render_to_response(ctx)
