from django import forms
from django.core.exceptions import ValidationError

from location.models import LocationMaster

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from crispy_forms.layout import Div
from crispy_forms.layout import Fieldset
from crispy_forms.bootstrap import TabHolder
from crispy_forms.bootstrap import Tab

class LocationMasterCreateForm1(forms.ModelForm):

    class Meta:
        model = LocationMaster
        fields = ("organisation_id", "store_id", "area", "zone",
                  "aisle", "bay", "level", "sequence",
                  "max_volume", "max_weight", "max_height",
                  "max_number_of_items")

class LocationMasterDetailForm(forms.ModelForm):
    """
       ItemMasterCreateForm
    """
    def    __init__(self,    *args,    **kwargs):
        super(LocationMasterCreateForm,    self).__init__(*args,    **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id_location_create_form'
        self.helper.form_name = 'id_location_create_form'
        self.helper.form_action = ''
        self.helper.form_method = 'POST'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
            TabHolder(
                Tab('Location Primary Details',
                    'dsp_location',
                    ),
                 Tab(
                     'Store   Info  ',
                     'organisation_id',
                     'store_id',
                     )

                 ),
                 Div(Submit('submit',    'Create',    css_class='btn    btn-default'),css_class='col-lg-offset-3    col-lg-9',),
            )

    class Meta:
        model = LocationMaster
        fields = ("organisation_id", "store_id", "area", "zone",
                  "aisle", "bay", "level", "sequence",
                  "max_volume", "max_weight", "max_height",
                  "max_number_of_items")

class LocationMasterCreateForm(forms.ModelForm):
    """
       ItemMasterCreateForm
    """
    def    __init__(self,    *args,    **kwargs):
        super(LocationMasterCreateForm,    self).__init__(*args,    **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id_location_create_form'
        self.helper.form_name = 'id_location_create_form'
        self.helper.form_action = ''
        self.helper.form_method = 'POST'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
            TabHolder(
                Tab('Location Primary Details',
                    'area',
                    'zone',
                    'aisle',
                    'bay',
                    'level',
                    'sequence',
                     ),
                 Tab(
                    'Location Capacity Details',
                    'max_volume',
                    'max_weight',
                    'max_height',
                    'max_number_of_items',
                     ),
                 Tab(
                     'Store   Info  ',
                     'organisation_id',
                     'store_id',
                     )

                 ),
                 Div(Submit('submit',    'Create',    css_class='btn    btn-default'),css_class='col-lg-offset-3    col-lg-9',),
            )

    class Meta:
        model = LocationMaster
        fields = ("organisation_id", "store_id", "area", "zone",
                  "aisle", "bay", "level", "sequence",
                  "max_volume", "max_weight", "max_height",
                  "max_number_of_items")

class  LocationSearchForm(forms.Form):
    """
    ItemSearchForm
    """
    def __init__(self,    *args,    **kwargs):
        super(LocationSearchForm,    self).__init__(*args,    **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id_location_search_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
                        Fieldset( 'Location Search Criteria',
                          'organisation_id',
                          'store_id',
                        ),
                        #Submit('submit',    'Submit',    css_class='btn    btn-default'),
                        Div(Submit('submit',    'Search',    css_class='btn    btn-default'),css_class='col-lg-offset-3    col-lg-9',),
                    )

    organisation_id = forms.CharField(label = 'Organization Id',required = False)
    store_id = forms.CharField(label = 'Store ID',required=False)