from django import forms
from django.core.exceptions import ValidationError

from item.models import ItemMaster

class ItemMasterUpdateForm(forms.ModelForm):
    
    class Meta:
        model = ItemMaster
        fields = ("item_name", "item_barcode", "item_description", "style",
                  "size", "country_of_origin", "unit_price", "retail_price",
                  "wholesale_price", "declaration_cost", "unit_weight",
                  "unit_height", "unit_volume", "item_category")
 

class ItemSearchForm(forms.Form):
    class Meta:
        model = ItemMaster
        fields =    ("item_name",  'item_barcode' , 'item_description')
