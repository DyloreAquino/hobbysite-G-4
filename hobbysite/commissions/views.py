"""Views file."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import (render,
                              redirect,
                              get_object_or_404)
from django.urls import reverse

from .forms import CommissionForm, JobForm
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
    """
    Allows for multiple forms to be
    rendered onto a single page
    Takes place of commission add view
    """
    kwargs = {'user': request.user}

    if request.method == 'POST':
        comm_form = CommissionForm(request.POST, **kwargs)
        job_form = JobForm(request.POST)

        if comm_form.is_valid():
            comm_form.instance.author = request.user.profile
            comm_form.save()
            pk = comm_form.instance.id
        
        if job_form.is_valid():
            job_form.instance.commission = comm_form.instance
            job_form.save()

        return redirect(reverse('commissions:commissions-detail', args=[pk]))
    else:
        comm_form = CommissionForm(**kwargs)
        job_form = JobForm()

    return render(request, 'commissions/commissions_create.html', {
        'comm_form': comm_form,
        'job_form': job_form,
    })


def handle_commission_update(request, pk):
    """
    Allows for commission update handling
    of multiple forms at once
    """
    ctx = {}
    
    commission = get_object_or_404(Commission, id=pk)

    comm_form = CommissionForm(request.POST or None, instance=commission)
    comm_form.fields['author'].disabled = True

    jobs = commission.job.all()

    for job in jobs:
        job_form = JobForm(request.POST or None, instance=job)

    if comm_form.is_valid():
        comm_form.save()
        return redirect(reverse('commissions:commissions-detail', args=[pk]))
    
    if job_form.is_valid():
        job_form.save()
        return redirect(reverse('commissions:commissions-detail', args=[pk]))
    
    ctx["commission"] = commission
    ctx["comm_form"] = comm_form
    ctx["jobs"] = jobs
    ctx["job_form"] = job_form

    return render(request, "commissions/commissions_update.html", ctx)
