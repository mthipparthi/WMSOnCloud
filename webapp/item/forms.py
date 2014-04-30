from django import forms
from django.core.exceptions import ValidationError

from item.models import ItemMaster

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from crispy_forms.layout import Div
from crispy_forms.layout import Fieldset
from crispy_forms.bootstrap import TabHolder
from crispy_forms.bootstrap import Tab

class ItemMasterUpdateForm1(forms.ModelForm):

    class Meta:
        model = ItemMaster
        fields = ("item_name", "item_barcode", "item_description", "style",
                  "size", "country_of_origin", "unit_price", "retail_price",
                  "wholesale_price", "declaration_cost", "unit_weight",
                  "unit_height", "unit_volume", "item_category")

class ItemMasterUpdateForm(forms.ModelForm):
    """
       ItemMasterUpdateForm
    """
    def    __init__(self,    *args,    **kwargs):
        super(ItemMasterUpdateForm,    self).__init__(*args,    **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id_create_item_form'
        self.helper.form_name = 'id_create_item_form'
        self.helper.form_action = ''
        self.helper.form_method = 'POST'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
            TabHolder(
                Tab('Item Description',
                    'item_name',
                    'item_barcode',
                    'item_description',
                    'style',
                    'size',
                    'country_of_origin',
                    'item_category',
                    ),
                 Tab(
                    'Cost',
                    'unit_price',
                    'retail_price',
                    'wholesale_price',
                    'declaration_cost',
                     ),
                 Tab(
                     'Weight   Info',
                     'unit_height',
                     'unit_weight',
                     'unit_volume',
                     )

                 ),
                 Div(Submit('submit',    'Save',    css_class='btn    btn-default'),css_class='col-lg-offset-3    col-lg-9',),
            )

    class Meta:
        model = ItemMaster
        fields = ("item_name", "item_barcode", "item_description", "style",
                  "size", "country_of_origin", "unit_price", "retail_price",
                  "wholesale_price", "declaration_cost", "unit_weight",
                  "unit_height", "unit_volume", "item_category")


class ItemSearchForm1(forms.Form):
    class Meta:
        model = ItemMaster
        fields =    ("item_name",  'item_barcode' , 'item_description')

class  ItemSearchForm(forms.Form):
    """
    ItemSearchForm
    """
    def __init__(self,    *args,    **kwargs):
        super(ItemSearchForm,    self).__init__(*args,    **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id_item_search_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
                        Fieldset( 'Item Search Criteria',
                          'item_name',
                          'item_barcode',
                          'item_description',
                        ),
                        #Submit('submit',    'Submit',    css_class='btn    btn-default'),
                        Div(Submit('submit',    'Search',    css_class='btn    btn-default'),css_class='col-lg-offset-3    col-lg-9',),
                    )

    item_name = forms.CharField(label = 'Item Name',required = False)
    item_barcode = forms.CharField(label = 'Item Barcode',required=False)
    item_description = forms.CharField(label = 'Item Description',max_length=30,required=False)
