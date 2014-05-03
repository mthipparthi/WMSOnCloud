from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from crispy_forms.layout import Div
from crispy_forms.layout import Fieldset
from crispy_forms.bootstrap import TabHolder
from crispy_forms.bootstrap import Tab

from inbound.models import Supplier
from inbound.models import PurchaseOrder

                 
class SupplierUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(SupplierUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id_create_supplier_form'
        self.helper.form_name = 'id_create_supplier_form'
        self.helper.form_action = ''
        self.helper.form_method = 'POST'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
                    'Create/Update Supplier',
                    "name",
                    "address_1",
                    "address_2",
                    "city",
                    "country",
                    "post_code",
                    "phone_number",
                    Div( Submit('submit', 'Save', css_class='btn btn-default'),css_class='col-lg-offset-3  col-lg-9'
                    ),
            )
        
    class Meta:
        model = Supplier
        fields = ( "name", "address_1", "address_2", "city",
                  "country", "post_code", "phone_number")


class SupplierListForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(SupplierListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id_create_supplier_form'
        self.helper.form_name = 'id_create_supplier_form'
        self.helper.form_action = ''
        self.helper.form_method = 'POST'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        
    class Meta:
        model = Supplier
        fields = ( "name", "address_1", "address_2", "city",
                  "country", "post_code", "phone_number")                  
                  
        
class PurchaseOrderUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PurchaseOrder
        fields = ("organisation_id", "supplier_id",  "expected_arrival_date")

        
        