"""Views file."""
from .models import Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class CommentListView(ListView):
    """List view of comments."""

    model = Comment
    template_name = 'commissions/comment_list.html'


class CommentDetailView(DetailView):
    """Detail view of comments."""

    model = Comment
    template_name = 'commissions/comment_detail.html'
