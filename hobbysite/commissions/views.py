"""Views file."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CommissionAddForm, JobAddForm
from .models import Commission


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
            job_form.instance.commission = comm_form.instance
            job_form.save()

        return redirect(reverse('commissions:commissions-detail', args=[pk]))
    else:
        comm_form = CommissionAddForm(**kwargs)
        job_form = JobAddForm()

    return render(request, 'commissions/commissions_create.html', {
        'comm_form': comm_form,
        'job_form': job_form,
    })
