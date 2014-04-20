from django import forms
from django.core.exceptions import ValidationError

from location.models import LocationMaster

class LocationMasterUpdateForm(forms.ModelForm):
    
    class Meta:
        model = LocationMaster
        fields = ("organisation_id", "store_id", "area", "zone",
                  "aisle", "bay", "level", "sequence",
                  "max_volume", "max_weight", "max_height",
                  "max_number_of_items")
