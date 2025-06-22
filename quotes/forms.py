from django import forms
from .models import Stock 

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker'] #as there is only one field in the DB
        