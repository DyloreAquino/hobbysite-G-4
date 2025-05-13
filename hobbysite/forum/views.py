from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ThreadCategory, Thread, Comment

class ThreadListView(ListView):
    model = Thread
    template_name = 'forum/thread_list.html'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = ThreadCategory.objects.all()
        return ctx

class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread_detail.html'


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    template_name = 'forum/thread_detail.html'
    

class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    template_name = 'forum/thread_detail.html'
