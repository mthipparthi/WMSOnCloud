from django import forms
from django.core.exceptions import ValidationError

from inventory.models import LocationInventory

class LocationInventoryUpdateForm(forms.ModelForm):
    
    class Meta:
        model = LocationInventory
        fields = ("dsp_location", "dsp_sku", "inventory_qty", "last_sell_datetime")


class LocationInventorySearchForm(forms.Form):
    class Meta:
        model = LocationInventory
        fields =    ("dsp_location",  'dsp_sku')