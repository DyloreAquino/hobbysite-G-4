from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ArticleListView(ListView):
    pass


def index(request):
    return HttpResponse('Hello World! This is the Wiki app')
