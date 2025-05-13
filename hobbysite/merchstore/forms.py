from django import forms
from .models import Transaction, Product


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            profile = user.profile
            self.fields['owner'].initial = profile
            self.fields['owner'].disabled = True

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        print(self.instance.stock)
        print(self.instance.OUTOFSTOCK)
        print(self.instance.status)
        
        if self.instance.stock == 0:
            self.fields['status'].initial = self.instance.OUTOFSTOCK
        else:
            self.fields['status'].initial = self.instance.AVAILABLE
        self.fields['status'].disabled = True
    
