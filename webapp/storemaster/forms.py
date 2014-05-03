from django import forms
from django.core.exceptions import ValidationError

from storemaster.models import StoreMaster

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from crispy_forms.layout import Div
from crispy_forms.layout import Fieldset
from crispy_forms.bootstrap import TabHolder
from crispy_forms.bootstrap import Tab

class StoreMasterForm(forms.ModelForm):
    """
       StoreMasterForm
    """
    def    __init__(self,    *args,    **kwargs):
        super(StoreMasterForm,    self).__init__(*args,    **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id_store_master_create_form'
        self.helper.form_name = 'id_store_master_create_form'
        self.helper.form_action = ''
        self.helper.form_method = 'POST'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
            TabHolder(
                Tab('Store Primary Deatils',
                    'store_id',
                    'store_name',
                    'oraganisation_id',
                    ),
                 Tab(
                    'Address            ',
                    'address_1',
                    'address_2',
                    'suburb',
                    'state',
                    'country',
                    'post_code',
                    'phone_nbr',
                     ),
                 Tab(
                     'Store Features ',
                     'dsitribution_centre_flag',
                     'rcv_without_shipment',
                     'locations_exist',
                     'local_currency',
                     'display_local_currency',
                     'create_user_id',
                     'receive_with_lpn',
                     'putaway_tasks_needed',
                     'picking_tasks_enabled',
                     'store_order_allocation_enabled',
                     'cash_sale_return_period',
                     'credit_sale_return_period',
                     )

                 ),
                 Div(Submit('submit',    'Save',    css_class='btn    btn-default'),css_class='col-lg-offset-3    col-lg-9',),
            )

    class Meta:
        model = StoreMaster

        fields = ("store_id","store_name","oraganisation_id","address_1",
                "address_2","suburb","state","country","post_code","phone_nbr",
                "dsitribution_centre_flag","rcv_without_shipment","locations_exist","local_currency",
                "display_local_currency","create_user_id","receive_with_lpn",
                "putaway_tasks_needed","picking_tasks_enabled","store_order_allocation_enabled",
                "cash_sale_return_period","credit_sale_return_period")

