from usermaster.models import UserMaster
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from crispy_forms.layout import Div
from crispy_forms.layout import Fieldset
from crispy_forms.bootstrap import TabHolder
from crispy_forms.bootstrap import Tab

# import the logging module
import logging

from rsccore.forms import RSCBaseForm

#    Create    your    models    here.

class    UserLoginForm3(forms.Form):
    """
    UserLoginForm
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    enterprise_id = forms.CharField(max_length=30,required=True)

class    UserLoginForm(forms.Form):
    """
    UserLoginForm
    """
    def __init__(self,    *args,    **kwargs):
        super(UserLoginForm,    self).__init__(*args,    **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id_user_login_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.label_class = 'col-lg-6'
        self.helper.field_class = 'col-lg-12'
        self.helper.layout = Layout(
                        Fieldset( 'User Login',
                          'email',
                          'password',
                          'enterprise_id',
                        ),
                        #Submit('submit',    'Submit',    css_class='btn    btn-default'),
                        Div(Submit('submit',    'Submit',    css_class='btn    btn-default'),css_class='col-lg-offset-3    col-lg-9',),
                    )

    email = forms.EmailField(label = 'Email Address',required = True)
    password = forms.CharField(label = 'Password',required=True)
    enterprise_id = forms.CharField(label = 'Enterprise ID',max_length=30,required=True)



class    UserLoginForm1(forms.ModelForm):
    """
    UserLoginForm
    """
    def __init__(self,    *args,    **kwargs):
        super(UserLoginForm1,    self).__init__(*args,    **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id_user_search_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.label_class = 'col-lg-6'
        self.helper.field_class = 'col-lg-12'
        self.helper.layout = Layout(
                        Fieldset( 'User Login',
                          'email',
                          'password',
                          'enterprise_id',
                        ),
                        #Submit('submit',    'Submit',    css_class='btn    btn-default'),
                        Div(Submit('submit',    'Submit',    css_class='btn    btn-default'),css_class='col-lg-offset-3    col-lg-9',),
                    )
    class Meta:
        model = UserMaster
        fields = ['email','password','enterprise_id']

class    NoFormTagCrispyFormMixin(object):
    @property
    def helper(self):
        if not hasattr(self,    '_helper'):
            self._helper = FormHelper()
            self._helper.form_tag = False
        return self._helper

class    UserCreationForm(RSCBaseForm):
    """
       UserCreationForm
    """
    def    __init__(self,  *args,  **kwargs):
        logger = logging.getLogger(__name__)
        logger.debug("UserCreationForm Initialisation begins")
        super(UserCreationForm,    self).__init__(*args,    **kwargs)

        print "Helper setting - User creation form"
        self.helper.form_id = 'id_user_creation_form'
        self.helper.form_name = 'id_user_creation_form'
        self.helper.form_action = '/usermaster/createuser/'
        self.helper.layout = Layout(
            TabHolder(
                Tab('Mandatory    Info',
                    'email',
                    'password',
                    'is_active',
                    ),
                 Tab(
                    'Basic    Info',
                    'title',
                    'first_name',
                    'last_name',
                    'job_title',
                    'date_joined',
                    'date_expiry',
                     ),
                 Tab(
                     'Store    Info',
                     'store_id',
                     )
                 ),
                 Div(Submit('submit',    'Submit',    css_class='btn    btn-default'),css_class='col-lg-offset-3    col-lg-9',),
            )

    def clean(self):
        logger = logging.getLogger(__name__)
        logger.debug("Clean method is initiated")
        return super(UserCreationForm, self).clean()

    class Meta:
        model = UserMaster
        fields = ['title','first_name','last_name',
                  'email','password','store_id',
                  'job_title','date_joined',
                   'date_expiry','is_active']


class    UserUpdateForm(forms.ModelForm):
    """
    UserUpdateForm
    """
    class Meta:
        model = UserMaster
        fields = ['title','first_name','last_name',
                  'email','enterprise_id','store_id',
                  'job_title','date_joined','date_expiry',
                  'is_active']

class    UserSearchForm(forms.Form):
    """
    UserSearchForm
    """
    def __init__(self,    *args,    **kwargs):
        super(UserSearchForm,    self).__init__(*args,    **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        #self.helper.form_id = 'id_UserSearchForm'
        self.helper.form_method = 'POST'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
                        Fieldset( 'User Search Criteria',
                          'email',
                          'last_name',
                          'enterprise_id',
                          'store_id',
                        ),
                        Submit('submit',    'Search',    css_class='btn    btn-default'),
                    )

    email = forms.EmailField(label = 'Email Address',required = False)
    last_name = forms.CharField(label = 'Last Name',required=False)
    enterprise_id = forms.CharField(label = 'Enterprise ID',max_length=30,required=False)
    store_id = forms.CharField(label = 'Store ID',max_length=30,required=False)

class    UserDetailForm(forms.ModelForm):
    """
       UserDetailForm
    """
    def    __init__(self,    *args,    **kwargs):
        super(UserDetailForm,    self).__init__(*args,    **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
            TabHolder(
                Tab('Mandatory    Info',
                    'email',
                    'password',
                    'is_active',
                    ),
                 Tab(
                    'Basic    Info',
                    'title',
                    'first_name',
                    'last_name',
                    'job_title',
                    'date_joined',
                    'date_expiry',
                     ),
                 Tab(
                     'Store    Info',
                     'enterprise_id',
                     'store_id',
                     )

                 ),
                 Div(Submit('submit',    'Submit',    css_class='btn    btn-default'),css_class='col-lg-offset-3    col-lg-9',),
            )

    class Meta:
        model = UserMaster
        fields = ['title','first_name','last_name',
                  'email','password','enterprise_id',
                   'store_id','job_title','date_joined',
                   'date_expiry','is_active']