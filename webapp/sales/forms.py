from django import forms
from django.core.exceptions import ValidationError

from sales.models import SellTransaction
from sales.models import SellTransactionDtl

class SellTransactionUpdateForm(forms.ModelForm):
    
    class Meta:
        model = SellTransaction
        fields = ("organisation_id", "invoice_number")
     