"""Views file."""
from .models import Commission
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseFormSet, formset_factory

from .forms import CommissionAddForm, JobAddForm


class CommissionListView(ListView):
    """List view of commissions."""

    model = Commission
    template_name = 'commissions/commissions_list.html'


class CommissionDetailView(LoginRequiredMixin, DetailView):
    """Detail view of commissions."""

    model = Commission
    template_name = 'commissions/commissions_detail.html'


class CommissionCreateView(LoginRequiredMixin, CreateView):
    """Create view of commission"""
    model = Commission
    template_name = 'commissions/commissions_create.html'
    form_class = CommissionAddForm

    def get_context_data(self, **kwargs):
        JobFormSet = formset_factory(JobAddForm, extra=3, can_delete=True)
        ctx = super().get_context_data(**kwargs)
        ctx['formset'] = JobFormSet()
        return ctx

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
