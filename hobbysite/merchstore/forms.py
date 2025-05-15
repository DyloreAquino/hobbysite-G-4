from django import forms
from .models import Transaction, Product


class TransactionForm(forms.ModelForm):
    """
    A form for transactions
    """

    class Meta:
        model = Transaction
        fields = ['amount']


class ProductCreateForm(forms.ModelForm):
    """
    A form for creating products
    """

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """Initializes the form to have owner as non-editable field"""

        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            profile = user.profile
            self.fields['owner'].initial = profile
            self.fields['owner'].disabled = True


class ProductUpdateForm(forms.ModelForm):
    """
    A form for updating product details
    """

    class Meta:
        model = Product
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        """Initializes the form to have status as non-editable field"""

        super().__init__(*args, **kwargs)

        if self.instance.stock == 0:
            self.fields['status'].initial = self.instance.OUTOFSTOCK
        else:
            self.fields['status'].initial = self.instance.AVAILABLE
        self.fields['status'].disabled = True
