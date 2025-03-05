"""Views file."""
from .models import Commission
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class CommissionListView(ListView):
    """List view of commissions."""

    model = Commission
    template_name = 'commissions/commissions_list.html'


class CommissionDetailView(DetailView):
    """Detail view of commissions."""

    model = Commission
    template_name = 'commissions/commissions_detail.html'
