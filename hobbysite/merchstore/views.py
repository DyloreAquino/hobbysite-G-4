from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

from .models import Product, Transaction
from .forms import TransactionForm, ProductCreateForm, ProductUpdateForm


class ProductListView(ListView):
    """
    ListView for the Product
    """

    model = Product
    template_name = 'merchstore/product_list.html'


class ProductDetailView(DetailView):
    """
    DetailView for the Product
    """

    model = Product
    template_name = 'merchstore/product_detail.html'

    def get_context_data(self, **kwargs):
        """Passes the TransactionForm as a form into the DetailView"""

        context = super().get_context_data(**kwargs)
        context['form'] = TransactionForm()
        return context

    def post(self, request, *args, **kwargs):
        """Handles form submission"""

        self.object = self.get_object()
        form = TransactionForm(request.POST)

        if not self.request.user.is_authenticated:
            return redirect(f"/accounts/login?next={self.request.path}")

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.buyer = self.request.user.profile
            transaction.product = self.object
            transaction.status = Transaction.ONCART

            if transaction.amount > self.object.stock:
                form.add_error('amount',
                               f"Only {self.object.stock} units available.")
                print(form.errors)
                return self.render_to_response(self.get_context_data(form=form))

            transaction.save()

            self.object.stock -= transaction.amount
            if self.object.stock == 0:
                self.object.status = self.object.OUTOFSTOCK
            self.object.save()

            return redirect('merchstore:cart')
        return self.render_to_response(self.get_context_data(form=form))


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    CreateView for the Product
    """

    model = Product
    template_name = 'merchstore/product_create.html'
    form_class = ProductCreateForm
    success_url = reverse_lazy('merchstore:product_list')

    def get_form_kwargs(self):
        """Allows the form to access user"""

        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """Places profile as the owner of the product"""

        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    UpdateView for the Product
    """

    model = Product
    template_name = 'merchstore/product_update.html'
    form_class = ProductUpdateForm

    def get_success_url(self):
        """Redirects to product detail after form submission"""

        return reverse_lazy('merchstore:product_detail',
                            kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        """Does checks for status of product after submission"""

        if form.instance.stock != 0:
            form.instance.status = form.instance.AVAILABLE
        else:
            form.instance.status = form.instance.OUTOFSTOCK
        return super().form_valid(form)


class CartView(LoginRequiredMixin, ListView):
    """
    CartView for the Transactions
    """

    model = Transaction
    template_name = 'merchstore/cart.html'

    def get_context_data(self, **kwargs):
        """Logic for proper displaying of categorized transactions"""

        context = super().get_context_data(**kwargs)

        categorized_transactions = {}
        for transaction in context['object_list']:
            owner = transaction.product.owner
            if transaction.buyer == self.request.user.profile:
                if owner not in categorized_transactions:
                    categorized_transactions[owner] = []
                categorized_transactions[owner].append(transaction)

        context['grouped_transactions'] = categorized_transactions.items()
        return context


class TransactionListView(LoginRequiredMixin, ListView):
    """
    ListView for the Transactions
    """

    model = Transaction
    template_name = 'merchstore/transactions.html'

    def get_context_data(self, **kwargs):
        """Logic for proper displaying of categorized transactions"""

        context = super().get_context_data(**kwargs)

        categorized_transactions = {}
        for transaction in context['object_list']:
            buyer = transaction.buyer
            if transaction.product.owner == self.request.user.profile:
                if buyer not in categorized_transactions:
                    categorized_transactions[buyer] = []
                categorized_transactions[buyer].append(transaction)

        context['grouped_transactions'] = categorized_transactions.items()
        return context
