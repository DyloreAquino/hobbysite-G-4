"""Views file."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import (render,
                              redirect)
from django.urls import reverse

from .forms import CommissionForm, JobForm, JobAppForm
from .models import Commission


class CommissionListView(ListView):
    """List view of commissions."""

    model = Commission
    template_name = 'commissions/commissions_list.html'


class CommissionDetailView(LoginRequiredMixin, DetailView):
    """Detail view of commissions."""

    model = Commission
    template_name = 'commissions/commissions_detail.html'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = JobAppForm()
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = JobAppForm(request.POST)
        if form.is_valid():
            job_app = form.save(commit=False)
            job_app.applicant = self.request.user.profile

            job_app.save()

        return self.render_to_response(self.get_context_data(form = form))


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


class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    """Update View of Commissions"""

    model = Commission
    template_name = 'commissions/commissions_update.html'
    form_class = CommissionForm
