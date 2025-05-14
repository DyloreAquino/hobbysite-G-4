"""Views file."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CommissionAddForm, JobAddForm
from .models import Commission, Job


class CommissionListView(ListView):
    """List view of commissions."""

    model = Commission
    template_name = 'commissions/commissions_list.html'


class CommissionDetailView(LoginRequiredMixin, DetailView):
    """Detail view of commissions."""

    model = Commission
    template_name = 'commissions/commissions_detail.html'


@login_required
def handle_commission_add_page(request):
    kwargs = {'user': request.user}

    if request.method == 'POST':
        comm_form = CommissionAddForm(request.POST, **kwargs)
        job_form = JobAddForm(request.POST)

        if comm_form.is_valid():
            comm_form.instance.author = request.user.profile
            comm_form.save()
            pk = comm_form.instance.id
        
        if job_form.is_valid():
            job_form.instance.commission = request.POST.instance
            job_form.save()

        return redirect(reverse('commissions:commissions-detail', args=[pk]))
    else:
        comm_form = CommissionAddForm(**kwargs)
        job_form = JobAddForm()

    return render(request, 'commissions/commissions_create.html', {
        'comm_form': comm_form,
        'job_form': comm_form,
    })

"""
class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    template_name = 'commissions/commissions_create.html'
    form_class = CommissionAddForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['formset'] = JobFormSet()
        ctx['comm_form'] = CommissionAddForm()
        return ctx

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, comm_form):
        comm_form.instance.author = self.request.user.profile
        return super().form_valid(comm_form)
"""
