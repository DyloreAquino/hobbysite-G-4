from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ThreadCategory, Thread, Comment
from .forms import ThreadForm, ThreadUpdateForm, CommentForm

class ThreadListView(ListView):
    model = Thread
    template_name = 'forum/thread_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        categories = ThreadCategory.objects.all()
        remove = []
        
        author = self.request.user
        if hasattr(author, 'profile'):            
            for category in categories:     
                if category.threads.exclude(author=author.profile).first() == None:
                    remove.append(category.name)
            
            categories = ThreadCategory.objects.exclude(name__in=remove)

        context['categories'] = categories
        return context


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread_detail.html'
    context_object_name = 'thread'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()  
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        thread = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = self.request.user.profile
            comment.thread = thread
            comment.save()
            return redirect(reverse('forum:thread-detail', kwargs={'pk': thread.pk}))
        
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    template_name = 'forum/thread_create.html'
    form_class = ThreadForm
    
    def get_success_url(self):
        return reverse('forum:thread-list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    template_name = 'forum/thread_update.html'
    form_class = ThreadUpdateForm
    
    def get_success_url(self):
        return reverse_lazy('forum:thread-detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        form.instance.author = self.request.user.profile        
        return super().form_valid(form)
